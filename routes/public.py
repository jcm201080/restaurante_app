# routes/public.py
from flask import Blueprint, render_template
from models.producto import Producto
import time

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