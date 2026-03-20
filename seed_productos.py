from app import app
from extensions import db
from models.producto import Producto

def cargar_productos():

    productos = [

        # 🍽️ ENTRANTES
        {"nombre": "Ensaladilla rusa", "precio": 6.0, "categoria": "Entrantes", "tipo": "tapa", "descripcion": "Casera con mayonesa suave"},
        {"nombre": "Croquetas caseras", "precio": 8.0, "categoria": "Entrantes", "tipo": "media", "descripcion": "De jamón ibérico"},
        {"nombre": "Patatas bravas", "precio": 7.0, "categoria": "Entrantes", "tipo": "racion", "descripcion": "Con salsa brava y alioli"},
        {"nombre": "Huevos rotos con jamón", "precio": 9.5, "categoria": "Entrantes", "tipo": "racion", "descripcion": "Con jamón serrano y patatas"},
        {"nombre": "Tabla de quesos", "precio": 12.0, "categoria": "Entrantes", "tipo": "racion", "descripcion": "Selección de quesos nacionales"},

        # 🍔 HAMBURGUESAS
        {"nombre": "Hamburguesa clásica", "precio": 10.0, "categoria": "Hamburguesas", "tipo": "plato", "descripcion": "Carne, lechuga y tomate"},
        {"nombre": "Hamburguesa BBQ", "precio": 12.0, "categoria": "Hamburguesas", "tipo": "plato", "descripcion": "Con salsa barbacoa y bacon"},
        {"nombre": "Hamburguesa doble", "precio": 14.0, "categoria": "Hamburguesas", "tipo": "plato", "descripcion": "Doble carne y doble queso"},
        {"nombre": "Hamburguesa vegana", "precio": 11.0, "categoria": "Hamburguesas", "tipo": "plato", "descripcion": "Base vegetal con verduras"},
        {"nombre": "Hamburguesa trufa", "precio": 13.5, "categoria": "Hamburguesas", "tipo": "plato", "descripcion": "Con mayonesa de trufa"},

        # 🥪 BOCADILLOS
        {"nombre": "Bocadillo de lomo", "precio": 6.5, "categoria": "Bocadillos", "tipo": "media", "descripcion": "Con pimientos"},
        {"nombre": "Bocadillo de pollo", "precio": 6.5, "categoria": "Bocadillos", "tipo": "media", "descripcion": "Pollo a la plancha"},
        {"nombre": "Bocadillo de calamares", "precio": 7.5, "categoria": "Bocadillos", "tipo": "media", "descripcion": "Clásico madrileño"},
        {"nombre": "Bocadillo vegetal", "precio": 5.5, "categoria": "Bocadillos", "tipo": "media", "descripcion": "Lechuga, tomate y huevo"},

        # 🍟 RACIONES
        {"nombre": "Calamares fritos", "precio": 10.0, "categoria": "Raciones", "tipo": "racion", "descripcion": "Rebozado crujiente"},
        {"nombre": "Alitas de pollo", "precio": 9.0, "categoria": "Raciones", "tipo": "media", "descripcion": "Con salsa BBQ"},
        {"nombre": "Nachos con queso", "precio": 8.5, "categoria": "Raciones", "tipo": "racion", "descripcion": "Con cheddar fundido"},
        {"nombre": "Costillas BBQ", "precio": 13.0, "categoria": "Raciones", "tipo": "racion", "descripcion": "A baja temperatura"},

        # 🍰 POSTRES
        {"nombre": "Tarta de queso", "precio": 5.0, "categoria": "Postres", "tipo": "plato", "descripcion": "Cremosa al horno"},
        {"nombre": "Brownie con helado", "precio": 5.5, "categoria": "Postres", "tipo": "plato", "descripcion": "Chocolate intenso"},
        {"nombre": "Flan casero", "precio": 4.5, "categoria": "Postres", "tipo": "plato", "descripcion": "Receta tradicional"},
        {"nombre": "Tiramisú", "precio": 5.5, "categoria": "Postres", "tipo": "plato", "descripcion": "Estilo italiano"},

        # 🥤 BEBIDAS
        {"nombre": "Coca-Cola", "precio": 2.5, "categoria": "Bebidas", "tipo": None, "descripcion": ""},
        {"nombre": "Cerveza", "precio": 2.2, "categoria": "Bebidas", "tipo": None, "descripcion": ""},
        {"nombre": "Agua", "precio": 1.5, "categoria": "Bebidas", "tipo": None, "descripcion": ""},
        {"nombre": "Vino tinto", "precio": 3.0, "categoria": "Bebidas", "tipo": None, "descripcion": ""},
        {"nombre": "Café", "precio": 1.2, "categoria": "Bebidas", "tipo": None, "descripcion": ""},
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