from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def main():
    # Creación de objetos de tipo Producto (platos)
    producto1 = Producto("Encebollado mixto", 5.50, True)
    producto2 = Producto("Chifle", 1.00, True)

    # Creación de objetos de tipo Cliente
    cliente1 = Cliente("Carlos López", "0999999999", 5)
    cliente2 = Cliente("Ana Torres", "1711111111", 2)

    # Instancia del servicio principal del restaurante
    restaurante = Restaurante()

    # Agregar los objetos creados a las listas
    restaurante.agregar_producto(producto1)
    restaurante.agregar_producto(producto2)
    restaurante.agregar_cliente(cliente1)
    restaurante.agregar_cliente(cliente2)

    # Mostrar la información en la consola
    print("=== PRODUCTOS REGISTRADOS ===")
    restaurante.mostrar_productos()
    
    print("\n=== CLIENTES REGISTRADOS ===")
    restaurante.mostrar_clientes()

# Punto de inicio del programa solicitado en la guía
if __name__ == "__main__":
    main()