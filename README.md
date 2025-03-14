# Proyecto Viveros

## Descripción
Sistema de gestión para viveros agrícolas desarrollado con Django 5.1. La aplicación permite administrar productores, fincas, viveros, labores y productos de control fitosanitario.

## Estructura del Proyecto
El proyecto está organizado en una aplicación principal llamada `gestion` que contiene los siguientes modelos:

- **Productor**: Gestiona información sobre los propietarios/productores
- **Finca**: Registra las propiedades asociadas a los productores
- **Vivero**: Gestiona los viveros ubicados en las fincas
- **Labor**: Registra las actividades realizadas en los viveros
- **ProductoControl**: Clase base para los productos de control
  - **ProductoControlHongo**: Productos para control de hongos
  - **ProductoControlPlaga**: Productos para control de plagas
  - **ProductoControlFertilizante**: Productos para fertilización

## Características

- Registro y gestión de productores con sus datos personales
- Administración de fincas asociadas a productores
- Seguimiento de viveros por finca con su tipo de cultivo
- Registro de labores realizadas en cada vivero
- Gestión de productos agroquímicos categorizados por tipo
- Pruebas unitarias para cada modelo

## Requisitos

- Python 3.x
- Django 5.1.6
- SQLite (configurado por defecto)

## Instalación

1. Clonar el repositorio
```bash
git clone https://github.com/username/viveros.git
cd viveros
```

2. Crear un entorno virtual e instalar dependencias
```bash
python -m venv venv
source venv/bin/activate  # En Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

3. Realizar migraciones
```bash
python manage.py migrate
```

4. Iniciar el servidor de desarrollo
```bash
python manage.py runserver
```

## Uso

El sistema está configurado con el panel de administración de Django. Después de iniciar el servidor, puedes acceder a:

- Panel de administración: http://localhost:8000/admin/

## Pruebas

Para ejecutar las pruebas unitarias:
```bash
python manage.py test gestion
```
