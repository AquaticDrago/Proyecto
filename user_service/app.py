from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = [
    {"id": 1, "nombre": "Admin", "rol": "admin"},
    {"id": 2, "nombre": "Empleado", "rol": "empleado"},
]

@app.route("/usuarios", methods=["GET"])
def obtener_usuarios():
    return jsonify(usuarios)

@app.route("/usuarios/<int:usuario_id>", methods=["GET"])
def obtener_usuario(usuario_id):
    usuario = next((u for u in usuarios if u["id"] == usuario_id), None)
    return jsonify(usuario) if usuario else ("Usuario no encontrado", 404)

@app.route("/usuarios", methods=["POST"])
def agregar_usuario():
    nuevo_usuario = request.json
    usuarios.append(nuevo_usuario)
    return jsonify(nuevo_usuario), 201

@app.route("/login", methods=["POST"])
def login():
    datos = request.json
    usuario = next((u for u in usuarios if u["nombre"] == datos["nombre"]), None)
    if usuario:
        return jsonify({"mensaje": "Login exitoso", "usuario": usuario})
    return "Credenciales incorrectas", 401

if __name__ == "__main__":
    app.run(port=5002)
