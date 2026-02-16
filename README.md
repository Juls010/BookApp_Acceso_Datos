![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092e20.svg?style=for-the-badge&logo=django&logoColor=white)
![Chart.js](https://img.shields.io/badge/chart.js-F5788D.svg?style=for-the-badge&logo=chart.js&logoColor=white)
# BookApp - Acceso a Datos

Este proyecto es una evolución de la aplicación `bookapp` inicial, centrada en el acceso avanzado a datos, análisis estadístico y visualización mediante **Django** y **Chart.js**.

## Funcionalidades

### 1. Gestión de Lista de Libros
* **Vista de Tabla**: Se ha transformado la lista antigua en una tabla limpia que incluye `title`, `pages`, `rating`, `status` y `published_date` 
* **Filtrado**: Se ha añadido un buscador para filtrar libros por título en tiempo real.
* **Ordenado**: Las cabeceras de la tabla son interactivas, permitiendo ordenar por cualquier campo de forma ascendente o descendente.
* **Paginación**: La lista está paginada (5 elementos por página) para mejorar la navegación y el rendimiento.

### 2. Panel de Estadísticas
* **Agregación de Datos**: Cálculo automático del libro con más/menos páginas y las notas medias de rating.
* **Gráficos Interactivos**:
    * **Gráfico de Tarta**: Distribución visual de los libros según su estado (`status`).
    * **Gráfico de Barras**: Frecuencia de libros agrupados por su puntuación (`rating`).

## Capturas de Pantalla

![Lista de Libros](https://res.cloudinary.com/dc4u0bzgh/image/upload/v1771235351/Captura_de_pantalla_2026-02-16_104739_xxwqvc.png)
*Figura 1: Vista de la tabla con filtrado, ordenado y paginación.*

![Panel de Estadísticas](https://res.cloudinary.com/dc4u0bzgh/image/upload/v1771235351/Captura_de_pantalla_2026-02-16_104809_rtkgbv.png)
*Figura 2: Análisis estadístico y visualizaciones con Chart.js.*

## Implementación Técnica
* **Vistas Basadas en Clases (CBV)**: Uso de `ListView` redefiniendo `get_queryset` para la lógica de filtrado y ordenación.
* **Agregados de Django**: Uso de funciones `Avg`, `Count`, `Max` y `Min` para el análisis de la base de datos.

## Instalación y Uso
1. Activa el entorno virtual: `.\env\Scripts\activate`
2. Instala Django: `pip install django`
3. Ejecuta las migraciones: `python manage.py migrate`
4. Lanza el servidor: `python manage.py runserver`

Proyecto para integración de datos y gráficas para Entorno Servidor.

Julia N.G 💕
