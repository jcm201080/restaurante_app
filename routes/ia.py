# routes/ia.py

from flask import Blueprint, request, jsonify
from models.producto import Producto

ia_bp = Blueprint('ia', __name__)

@ia_bp.route("/recomendar", methods=["POST"])
def recomendar():
    productos = Producto.query.filter_by(disponible=True).all()

    if not productos:
        return jsonify({"respuesta": "Hoy todo está tan bueno que no sé qué recomendar 😄"})

    nombres = [p.nombre for p in productos]

    respuesta = f"Hoy te recomiendo probar: {nombres[0]} 🔥"

    return jsonify({"respuesta": respuesta})