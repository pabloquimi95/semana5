from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self):
        # Listas vacías que sirven para almacenar los objetos creados
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto) -> None:
        # Añade un objeto Producto a la lista
        self.productos.append(producto)

    def agregar_cliente(self, cliente) -> None:
        # Añade un objeto Cliente a la lista
        self.clientes.append(cliente)

    def mostrar_productos(self) -> None:
        # Recorre la lista de productos y los imprime uno por uno
        for producto in self.productos:
            print(producto)

    def mostrar_clientes(self) -> None:
        # Recorre la lista de clientes y los imprime uno por uno
        for cliente in self.clientes:
            print(cliente)