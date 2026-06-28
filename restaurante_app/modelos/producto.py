class Producto:
    def __init__(self, nombre: str, precio: float, disponible: bool):
        # Atributos del producto
        self.nombre = nombre
        self.precio = precio
        self.disponible = disponible

    def mostrar_informacion(self) -> str:
        # Retorna el nombre y precio
        return f"Producto: {self.nombre} | Precio: ${self.precio}"

    def __str__(self) -> str:
        # Método para mostrar el producto como texto
        estado = "Disponible" if self.disponible else "Agotado"
        return f"{self.nombre} - ${self.precio} ({estado})"