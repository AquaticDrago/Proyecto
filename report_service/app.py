from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

# URLs de los microservicios
INVENTORY_URL = os.getenv("INVENTORY_SERVICE_URL", "http://localhost:5001/productos")

@app.route("/reporte", methods=["GET"])
def generar_reporte():
    try:
        # Llamada al microservicio de inventario
        respuesta = requests.get(INVENTORY_URL)
        productos = respuesta.json()
        total_productos = len(productos)
        total_stock = sum(p["stock"] for p in productos)
        return jsonify({
            "total_productos": total_productos,
            "total_stock": total_stock
        })
    except Exception as e:
        return f"Error generando el reporte: {str(e)}", 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
