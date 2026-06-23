# Sistema de Gestión de Inventario

Proyecto desarrollado con Django para la gestión de productos, categorías y proveedores.

## Funcionalidades

* CRUD de Productos
* Gestión de Categorías
* Gestión de Proveedores
* Inicio y cierre de sesión
* Control de acceso por roles
* Protección de rutas mediante autenticación

## Tecnologías utilizadas

* Python
* Django
* SQLite
* Bootstrap

## Instalación

1. Clonar el repositorio:

git clone https://github.com/rodolfoavendano00-bit/sistema-inventario-django.git

2. Crear y activar entorno virtual.

3. Instalar dependencias:

pip install -r requirements.txt

4. Ejecutar migraciones:

python manage.py migrate

5. Iniciar servidor:

python manage.py runserver

## Roles del sistema

### Usuario anónimo

* Puede visualizar los productos.

### Usuario autenticado

* Puede visualizar productos.
* Puede crear productos.
* Puede editar productos.

### Administrador

* Puede visualizar productos.
* Puede crear productos.
* Puede editar productos.
* Puede eliminar productos.
