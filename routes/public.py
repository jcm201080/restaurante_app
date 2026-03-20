# routes/public.py
from flask import Blueprint, render_template,request, flash, redirect
from models.producto import Producto
import time
import smtplib
from email.mime.text import MIMEText

public_bp = Blueprint('public', __name__)
@public_bp.route("/")
def index():
    return render_template(
        "public/index.html",
        sugerencias=Producto.query.filter_by(destacado=True).all(),
        timestamp=int(time.time())
    )

@public_bp.route("/menu")
def menu():
    productos = Producto.query.filter(
        Producto.disponible == True,
        Producto.categoria != "Bebidas"
    ).all()

    sugerencias = Producto.query.filter_by(destacado=True, disponible=True).all()
    plato_dia = Producto.query.filter_by(plato_dia=True, disponible=True).first()
    fuera_carta = Producto.query.filter_by(fuera_carta=True, disponible=True).all()

    categorias = {}

    for p in productos:
        if p.categoria not in categorias:
            categorias[p.categoria] = []
        categorias[p.categoria].append(p)

    return render_template(
        "public/menu.html",
        productos=productos,
        categorias=categorias,
        sugerencias=sugerencias,
        plato_dia=plato_dia,
        fuera_carta=fuera_carta,
        timestamp=int(time.time())
    )


@public_bp.route("/menu_simple")
def menu_simple():
    productos = Producto.query.filter_by(disponible=True).all()

    categorias = {}

    for p in productos:
        if p.categoria not in categorias:
            categorias[p.categoria] = []
        categorias[p.categoria].append(p)

    return render_template(
        "public/menu_simple.html",
        categorias=categorias,
        timestamp=int(time.time())
    )


@public_bp.route("/bebidas")
def bebidas():
    bebidas = Producto.query.filter_by(categoria="Bebidas", disponible=True).all()

    categorias = {}

    for b in bebidas:
        tipo = b.tipo or "Otros"
        if tipo not in categorias:
            categorias[tipo] = []
        categorias[tipo].append(b)

    return render_template(
        "public/bebidas.html",
        categorias=categorias,
        timestamp=int(time.time())
    )





@public_bp.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        telefono = request.form.get("telefono")
        fecha = request.form.get("fecha")
        hora = request.form.get("hora")
        personas = request.form.get("personas")
        mensaje = request.form.get("mensaje")

        contenido = f"""
        Nueva reserva/contacto:

        Nombre: {nombre}
        Email: {email}
        Teléfono: {telefono}
        Fecha: {fecha}
        Hora: {hora}
        Personas: {personas}

        Mensaje:
        {mensaje}
        """

        try:
            msg = MIMEText(contenido)
            msg["Subject"] = "Nueva reserva web"
            msg["From"] = "tu_email@gmail.com"
            msg["To"] = "jmc201080@gmail.com"

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login("tu_email@gmail.com", "tu_password")
            server.send_message(msg)
            server.quit()

            flash("✅ Mensaje enviado correctamente")
        except Exception as e:
            print(e)
            flash("❌ Error al enviar")

        return redirect("/contacto")

    return render_template("public/contacto.html")