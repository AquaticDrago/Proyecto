class Producto:
    def __init__(self, id, nombre, stock):
        self.id = id
        self.nombre = nombre
        self.stock = stock

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "stock": self.stock,
        }
