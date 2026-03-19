# models/producto.py
from extensions import db

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.String(255))
    precio = db.Column(db.Float)
    tipo = db.Column(db.String(50))  # tapa, racion, media, etc

    categoria = db.Column(db.String(50))  
    # entrantes, raciones, bocadillos, etc

    disponible = db.Column(db.Boolean, default=True)
    destacado = db.Column(db.Boolean, default=False)  # ⭐ sugerencias
    fuera_carta = db.Column(db.Boolean, default=False)
    plato_dia = db.Column(db.Boolean, default=False)
    imagen = db.Column(db.String(255))