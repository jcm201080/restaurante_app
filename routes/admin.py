# routes/admin.py
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.producto import Producto
from extensions import db
import time
from flask import session
import os
from werkzeug.utils import secure_filename


admin_bp = Blueprint('admin', __name__)

CATEGORIAS = ["Entrantes", "Raciones", "Bocadillos", "Postres", "Bebidas"]
TIPOS = ["tapa", "media", "racion", "plato"]

UPLOAD_FOLDER = "static/uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)



#Proteger ruta login
def login_required(f):
    def wrap(*args, **kwargs):
        if not session.get("admin"):
            return redirect("/admin/login")
        return f(*args, **kwargs)
    wrap.__name__ = f.__name__
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
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    
    tipo = request.form.get("tipo") or None
    categoria = request.form.get("categoria") or None

    imagen = request.files.get("imagen")

    filename = None
    if imagen and imagen.filename != "":
        filename = secure_filename(imagen.filename)
        ruta = os.path.join(UPLOAD_FOLDER, filename)
        imagen.save(ruta)
    

    nuevo = Producto(
        nombre=nombre,
        precio=precio,
        categoria=categoria,
        tipo=tipo,
        imagen=filename
    )



    db.session.add(nuevo)
    db.session.commit()

    

    return redirect(url_for("admin.productos"))

@admin_bp.route("/update/<int:id>", methods=["POST"])
@login_required
def update_producto(id):
    producto = Producto.query.get(id)

    imagen = request.files.get("imagen")

    if imagen and imagen.filename != "":
        filename = secure_filename(imagen.filename)
        ruta = os.path.join(UPLOAD_FOLDER, filename)
        imagen.save(ruta)
        producto.imagen = filename

    if not producto:
        flash("Producto no encontrado ❌")
        return redirect(url_for("admin.productos"))

    # 👇 detectar acción
    action = request.form.get("action")

    # 🔴 ELIMINAR
    if action == "eliminar":
        db.session.delete(producto)
        db.session.commit()
        flash("Producto eliminado 🗑️")
        return redirect(url_for("admin.productos"))

    # 🟢 ACTUALIZAR
    producto.nombre = request.form.get("nombre")
    producto.precio = request.form.get("precio")
    producto.categoria = request.form.get("categoria") or None
    producto.tipo = request.form.get("tipo") or None

    producto.destacado = "destacado" in request.form
    producto.fuera_carta = "fuera_carta" in request.form

    # 🧠 SOLO UN PLATO DEL DÍA
    if "plato_dia" in request.form:
        Producto.query.update({Producto.plato_dia: False})
        db.session.commit()
        producto.plato_dia = True
    else:
        producto.plato_dia = False

    if producto.categoria == "Bebidas":
        producto.tipo = None

    db.session.commit()

    flash("Producto actualizado 💾")
    return redirect(url_for("admin.productos"))



