# Comprobador de Disponibilidad de Tallas - Zara

Este repositorio contiene un script en Python diseñado para verificar automáticamente la disponibilidad de tallas para una prenda específica en la tienda online de Zara. El script `check-size-of-product-zara.py` revisa la página del producto cada 30 segundos y notifica con un pitido si la talla deseada está disponible.

## Pre-requisitos

Antes de ejecutar el script, asegúrate de tener instalado lo siguiente en tu sistema:

- **Python:** El script está escrito en Python, por lo que necesitarás tener Python instalado en tu máquina. Puedes descargar e instalar la última versión de Python desde [la página oficial de Python](https://www.python.org/downloads/).


## Instalación

1. **Clona el repositorio (o descarga únicamente el archivo python):**

    ```
    git clone [URL_DEL_REPOSITORIO]
    ```

2. **Instala las dependencias:**

    Navega al directorio del proyecto, abre una terminal e instala Selenium y webdriver_manager:

    ```
    pip install selenium
    ```
    ```
    pip install webdriver_manager
    ```

## Uso

Para ejecutar el script, sigue estos pasos:

1. **Configura el script:**

    Abre el archivo `check-size-of-product-zara.py` y configura las variables necesarias, como la URL del producto en la línea 14 y la talla que estás buscando en la línea 17.

2. **Ejecuta el script:**

    En la terminal, navega al directorio del proyecto (Abre cmd, escribe "cd Downloads") y ejecuta el script con el siguiente comando:

    ```
    python check-size-of-product-zara.py
    ```

El script realizará la comprobación y te notificará cuando haya disponibilidad de la talla que estás buscando.

## Contribuciones

Las contribuciones son siempre bienvenidas. Si tienes alguna sugerencia o quieres contribuir al proyecto, siéntete libre de hacerlo.

## Dudas

Siéntete libre de preguntarme a través de mis redes sociales:

- LinkedIn - [Paula Iglesias Reina](https://www.linkedin.com/in/paula-iglesias-reina/)
- TikTok - [@paureinatech](https://www.tiktok.com/@paureinatech)

---
> **Nota:** Este script está destinado únicamente a fines educativos. Asegúrate de respetar las políticas de Zara y no utilizar el script para actividades que puedan considerarse abuso o violación de los términos de servicio de la tienda.
