class Cliente:
    def __init__(self, nombre: str, cedula: str, numero_mesa: int):
        # Atributos del cliente
        self.nombre = nombre
        self.cedula = cedula
        self.numero_mesa = numero_mesa

    def mostrar_informacion(self) -> str:
        # Retorna el nombre y cédula del cliente
        return f"Cliente: {self.nombre} | Cédula: {self.cedula}"

    def __str__(self) -> str:
        # Método para mostrar el cliente como texto
        return f"Cliente: {self.nombre} (Mesa {self.numero_mesa})"