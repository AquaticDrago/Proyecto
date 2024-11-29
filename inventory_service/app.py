from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Simulación de base de datos en memoria
productos = [
    {"id": 1, "nombre": "Producto A", "stock": 50},
    {"id": 2, "nombre": "Producto B", "stock": 20},
    {"id": 3, "nombre": "Producto C", "stock": 100}
]

@app.route("/productos", methods=["GET"])
def obtener_productos():
    return jsonify(productos)

@app.route("/productos", methods=["POST"])
def agregar_producto():
    data = request.json
    nuevo_producto = {
        "id": len(productos) + 1,
        "nombre": data["nombre"],
        "stock": data["stock"]
    }
    productos.append(nuevo_producto)
    return jsonify(nuevo_producto), 201

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
