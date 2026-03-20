# models/producto.py
from extensions import db

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255))
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    tipo = db.Column(db.String(20), default="racion")  # tapa, racion, media, etc

    categoria = db.Column(db.String(50))  
    # entrantes, raciones, bocadillos, etc

    disponible = db.Column(db.Boolean, default=True)
    destacado = db.Column(db.Boolean, default=False)  # ⭐ sugerencias
    fuera_carta = db.Column(db.Boolean, default=False)
    plato_dia = db.Column(db.Boolean, default=False)
    imagen = db.Column(db.String(255))

    # Timestamps: Vital para saber cuándo se actualizó la carta
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())