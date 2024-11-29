from flask import Flask, jsonify
import requests

app = Flask(__name__)

INVENTORY_URL = "http://inventory_service:5001/productos"

@app.route("/reporte", methods=["GET"])
def generar_reporte():
    try:
        respuesta = requests.get(INVENTORY_URL)
        productos = respuesta.json()
        total_productos = len(productos)
        total_stock = sum(p["stock"] for p in productos)
        return jsonify({"total_productos": total_productos, "total_stock": total_stock})
    except Exception as e:
        return f"Error generando el reporte: {str(e)}", 500

if __name__ == "__main__":
    app.run(port=5003)
