# routes/admin.py
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.producto import Producto
from extensions import db
import time
import os
from werkzeug.utils import secure_filename
from PIL import Image

from functools import wraps

import uuid




admin_bp = Blueprint('admin', __name__)

CATEGORIAS = ["Entrantes","Hamburguesas", "Raciones", "Bocadillos", "Postres", "Bebidas"]
TIPOS = ["tapa", "media", "racion", "plato"]

UPLOAD_FOLDER = "static/uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Configuración técnica de imagen
MAX_IMAGE_WIDTH = 800
IMAGE_QUALITY = 85  # Equilibrio perfecto entre peso y nitidez

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}

def allowed_file(filename):
    ext = os.path.splitext(filename)[1].lower().replace(".", "")
    return ext in ALLOWED_EXTENSIONS


def procesar_y_guardar_imagen(file):
    if not file or file.filename == "":
        return None

    if not allowed_file(file.filename):
        return None

    filename = secure_filename(file.filename)
    base_name = os.path.splitext(filename)[0]
    base_name = base_name.replace(" ", "_").lower()

    unique_id = uuid.uuid4().hex
    final_filename = f"{base_name}_{unique_id}.jpg"

    ruta_guardado = os.path.join(UPLOAD_FOLDER, final_filename)

    try:
        # 🔍 Verificar que es imagen real
        img = Image.open(file)
        img.verify()

        # 🔄 Resetear puntero
        file.seek(0)

        # 🔁 Reabrir para procesar
        img = Image.open(file)

        # 🎨 Convertir SIEMPRE a RGB (más limpio y consistente)
        img = img.convert("RGB")

        # 📏 Redimensionar si es necesario
        if img.width > MAX_IMAGE_WIDTH:
            w_percent = MAX_IMAGE_WIDTH / float(img.width)
            h_size = int(img.height * w_percent)
            img = img.resize((MAX_IMAGE_WIDTH, h_size), Image.Resampling.LANCZOS)

        # 💾 Guardar optimizada
        img.save(ruta_guardado, "JPEG", optimize=True, quality=IMAGE_QUALITY)

        return final_filename

    except Exception as e:
        print(f"Error procesando imagen: {e}")
        return None

#Proteger ruta login

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if not session.get("admin"):
            return redirect("/admin/login")
        return f(*args, **kwargs)
    return wrap

@admin_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "1234":
            session["admin"] = True
            return redirect(url_for("admin.productos"))

    return render_template("admin/login.html")



@admin_bp.route("/productos")
@login_required
def productos():
    categoria = request.args.get("categoria")

    if categoria:
        productos = Producto.query.filter_by(categoria=categoria).all()
    else:
        productos = Producto.query.all()

    return render_template(
        "admin/productos.html",
        productos=productos,
        categorias=CATEGORIAS,
        tipos=TIPOS,
        timestamp=int(time.time())
    )

@admin_bp.route("/add", methods=["POST"])
@login_required
def add_producto():
    # Recogida de datos con limpieza básica
    nombre = request.form.get("nombre", "").strip()
    precio_raw = request.form.get("precio", "0").replace(",", ".")
    
    try:
        precio = float(precio_raw)
    except ValueError:
        flash("⚠️ El precio no tiene un formato válido.")
        return redirect(url_for("admin.productos"))

    tipo = request.form.get("tipo") or None
    categoria = request.form.get("categoria") or None

    # --- PROCESAMIENTO DE IMAGEN ---
    file = request.files.get("imagen")
    filename = procesar_y_guardar_imagen(file) # <--- Aquí ocurre la magia

    # --- PERSISTENCIA ---
    try:
        nuevo = Producto(
            nombre=nombre,
            precio=precio,
            categoria=categoria,
            tipo=tipo,
            imagen=filename, # Guardamos el nombre del archivo optimizado o None
            disponible=True  # por defecto visible
        )
        db.session.add(nuevo)
        db.session.commit()
        flash(f"✅ '{nombre}' añadido correctamente.")
    except Exception as e:
        db.session.rollback()
        # Si la DB falla, deberíamos borrar la imagen que acabamos de guardar
        if filename:
            path = os.path.join(UPLOAD_FOLDER, filename)
            if os.path.exists(path):
                os.remove(path)
        flash("❌ Error al guardar en la base de datos.")
        print(f"Error DB: {e}")

    return redirect(url_for("admin.productos"))
@admin_bp.route("/update/<int:id>", methods=["POST"])
@login_required
def update_producto(id):
    producto = Producto.query.get(id)
    
    if not producto:
        flash("Producto no encontrado ❌")
        return redirect(url_for("admin.productos"))

    action = request.form.get("action")

    # 🔴 ACCIÓN: ELIMINAR
    if action == "eliminar":
        if producto.imagen:
            old_path = os.path.join(UPLOAD_FOLDER, producto.imagen)
            if os.path.exists(old_path):
                os.remove(old_path)
        
        db.session.delete(producto)
        db.session.commit()
        flash("Producto e imagen eliminados correctamente 🗑️")
        return redirect(url_for("admin.productos"))

    # 🟢 ACCIÓN: ACTUALIZAR

    # 1. Gestión de nueva imagen (🔥 ORDEN CORRECTO)
    imagen_nueva = request.files.get("imagen")
    if imagen_nueva and imagen_nueva.filename != "":

        # 👉 Primero procesamos la nueva
        filename = procesar_y_guardar_imagen(imagen_nueva)

        if filename:
            # 👉 SOLO si la nueva se creó bien, borramos la antigua
            if producto.imagen:
                old_path = os.path.join(UPLOAD_FOLDER, producto.imagen)
                if os.path.exists(old_path):
                    os.remove(old_path)

            producto.imagen = filename
        else:
            flash("⚠️ Error procesando la nueva imagen, se mantiene la anterior.")

    # 2. Validación y limpieza de datos
    producto.nombre = request.form.get("nombre", "").strip()
    
    precio_raw = request.form.get("precio", "0").replace(",", ".")
    try:
        producto.precio = float(precio_raw)
    except ValueError:
        flash("⚠️ Precio inválido, se mantuvo el anterior.")

    producto.categoria = request.form.get("categoria") or None
    producto.tipo = request.form.get("tipo") or None

    # 3. Flags y lógica de negocio
    producto.destacado = "destacado" in request.form
    producto.fuera_carta = "fuera_carta" in request.form
    producto.disponible = "disponible" in request.form

    # 🧠 Solo un plato del día
    if "plato_dia" in request.form:
        Producto.query.update({Producto.plato_dia: False})
        producto.plato_dia = True
    else:
        producto.plato_dia = False

    # Lógica por categoría
    if producto.categoria == "Bebidas":
        producto.tipo = None

    # 4. Guardado en DB
    try:
        db.session.commit()
        flash("Producto actualizado con éxito 💾")
    except Exception as e:
        db.session.rollback()
        flash("❌ Error crítico al actualizar.")
        print(f"Error: {e}")

    return redirect(url_for("admin.productos"))


@admin_bp.route("/reset_disponibles", methods=["POST"])
@login_required
def reset_disponibles():
    try:
        Producto.query.update({Producto.disponible: True})
        db.session.commit()
        flash("🔄 Todos los productos están disponibles otra vez")
    except Exception as e:
        db.session.rollback()
        flash("❌ Error al resetear productos")
        print(e)

    return redirect(url_for("admin.productos"))