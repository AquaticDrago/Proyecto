from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Simulación de base de datos en memoria
usuarios = [
    {"id": 1, "nombre": "Juan Pérez", "email": "juan@example.com"},
    {"id": 2, "nombre": "María López", "email": "maria@example.com"}
]

@app.route("/usuarios", methods=["GET"])
def obtener_usuarios():
    return jsonify(usuarios)

@app.route("/usuarios", methods=["POST"])
def agregar_usuario():
    data = request.json
    nuevo_usuario = {
        "id": len(usuarios) + 1,
        "nombre": data["nombre"],
        "email": data["email"]
    }
    usuarios.append(nuevo_usuario)
    return jsonify(nuevo_usuario), 201

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
