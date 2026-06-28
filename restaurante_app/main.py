from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def main():
    # 1. Creación de objetos de tipo Producto (¡Tu nuevo menú ampliado!)
    producto1 = Producto("Encebollado mixto", 5.50, True)
    producto2 = Producto("Chifle", 0.50, True)  # Actualizado a 0.50
    producto3 = Producto("Pan", 0.25, True)     # Nuevo producto
    producto4 = Producto("Cola", 0.50, True)    # Nuevo producto

    # 2. Creación de objetos de tipo Cliente
    cliente1 = Cliente("Carlos López", "0999999999", 5)
    cliente2 = Cliente("Ana Torres", "1711111111", 2)

    # Instancia del servicio principal del restaurante
    restaurante = Restaurante()

    # 3. Agregar TODOS los objetos creados a las listas del restaurante
    restaurante.agregar_producto(producto1)
    restaurante.agregar_producto(producto2)
    restaurante.agregar_producto(producto3)  # Registramos el pan
    restaurante.agregar_producto(producto4)  # Registramos la cola
    
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