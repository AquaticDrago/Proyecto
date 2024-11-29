from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de datos simulada
productos = [
    {"id": 1, "nombre": "Laptop", "stock": 15},
    {"id": 2, "nombre": "Teclado", "stock": 50},
]

@app.route("/productos", methods=["GET"])
def obtener_productos():
    return jsonify(productos)

@app.route("/productos/<int:producto_id>", methods=["GET"])
def obtener_producto(producto_id):
    producto = next((p for p in productos if p["id"] == producto_id), None)
    return jsonify(producto) if producto else ("Producto no encontrado", 404)

@app.route("/productos", methods=["POST"])
def agregar_producto():
    nuevo_producto = request.json
    productos.append(nuevo_producto)
    return jsonify(nuevo_producto), 201

@app.route("/productos/<int:producto_id>", methods=["PUT"])
def actualizar_producto(producto_id):
    producto = next((p for p in productos if p["id"] == producto_id), None)
    if not producto:
        return "Producto no encontrado", 404
    producto.update(request.json)
    return jsonify(producto)

@app.route("/productos/<int:producto_id>", methods=["DELETE"])
def eliminar_producto(producto_id):
    global productos
    productos = [p for p in productos if p["id"] != producto_id]
    return "Producto eliminado", 204

if __name__ == "__main__":
    app.run(port=5001)
