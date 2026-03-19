from app import app
from extensions import db
from models.producto import Producto

def cargar_productos():

    productos = [

        # 🍽️ ENTRANTES
        {"nombre": "Ensaladilla rusa", "precio": 6.0, "categoria": "Entrantes", "tipo": "tapa"},
        {"nombre": "Croquetas caseras", "precio": 8.0, "categoria": "Entrantes", "tipo": "media"},
        {"nombre": "Patatas bravas", "precio": 7.0, "categoria": "Entrantes", "tipo": "racion"},
        {"nombre": "Huevos rotos con jamón", "precio": 9.5, "categoria": "Entrantes", "tipo": "racion"},

        # 🍔 HAMBURGUESAS
        {"nombre": "Hamburguesa clásica", "precio": 10.0, "categoria": "Hamburguesas", "tipo": "plato"},
        {"nombre": "Hamburguesa BBQ", "precio": 12.0, "categoria": "Hamburguesas", "tipo": "plato"},
        {"nombre": "Hamburguesa doble", "precio": 14.0, "categoria": "Hamburguesas", "tipo": "plato"},
        {"nombre": "Hamburguesa vegana", "precio": 11.0, "categoria": "Hamburguesas", "tipo": "plato"},

        # 🥪 BOCADILLOS
        {"nombre": "Bocadillo de lomo", "precio": 6.5, "categoria": "Bocadillos", "tipo": "media"},
        {"nombre": "Bocadillo de pollo", "precio": 6.5, "categoria": "Bocadillos", "tipo": "media"},
        {"nombre": "Bocadillo de calamares", "precio": 7.5, "categoria": "Bocadillos", "tipo": "media"},

        # 🍟 RACIONES
        {"nombre": "Calamares fritos", "precio": 10.0, "categoria": "Raciones", "tipo": "racion"},
        {"nombre": "Alitas de pollo", "precio": 9.0, "categoria": "Raciones", "tipo": "media"},
        {"nombre": "Nachos con queso", "precio": 8.5, "categoria": "Raciones", "tipo": "racion"},

        # 🍰 POSTRES
        {"nombre": "Tarta de queso", "precio": 5.0, "categoria": "Postres", "tipo": "plato"},
        {"nombre": "Brownie con helado", "precio": 5.5, "categoria": "Postres", "tipo": "plato"},
        {"nombre": "Flan casero", "precio": 4.5, "categoria": "Postres", "tipo": "plato"},

        # 🥤 BEBIDAS (esto da MUCHA vida al menú)
        {"nombre": "Coca-Cola", "precio": 2.5, "categoria": "Bebidas", "tipo": "tapa"},
        {"nombre": "Cerveza", "precio": 2.2, "categoria": "Bebidas", "tipo": "tapa"},
        {"nombre": "Agua", "precio": 1.5, "categoria": "Bebidas", "tipo": "tapa"},
    ]

    for p in productos:
        producto = Producto(
            nombre=p["nombre"],
            precio=p["precio"],
            categoria=p["categoria"],
            tipo=p["tipo"],
            disponible=True
        )
        db.session.add(producto)

    db.session.commit()
    print("🔥 Productos cargados correctamente")


if __name__ == "__main__":
    with app.app_context():
        cargar_productos()