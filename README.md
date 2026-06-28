# Sistema de Gestión de Restaurante (Semana 5)

Este proyecto es una aplicación modular en Python que simula el sistema de registro y gestión de un restaurante. Aplica los principios fundamentales de la **Programación Orientada a Objetos (POO)**, estructurando el código en paquetes y módulos separados para mantener un diseño limpio, escalable y organizado.

## 🚀 Características
* **Gestión de Productos:** Registro de platos y bebidas con nombre, precio y estado de disponibilidad.
* **Gestión de Clientes:** Registro de clientes con su nombre, cédula y número de mesa asignada.
* **Módulo de Servicios:** Control centralizado para agregar y listar de forma masiva tanto los productos como los clientes registrados.

## 📁 Estructura del Proyecto
El proyecto sigue una estructura de paquetes modulares:

```text
semana5/
└── restaurante_app/
    ├── modelos/
    │   ├── __init__.py
    │   ├── cliente.py
    │   └── producto.py
    ├── servicios/
    │   ├── __init__.py
    │   └── restaurante.py
    ├── main.py
    └── README.md