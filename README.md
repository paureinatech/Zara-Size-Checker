# Comprobador de Disponibilidad de Tallas - Zara

Este repositorio contiene un script en Python diseñado para verificar automáticamente la disponibilidad de tallas para una prenda específica en la tienda online de Zara. El script `check.py` revisa la página del producto cada 30 segundos y notifica con un pitido si la talla deseada está disponible.

## Pre-requisitos

Antes de ejecutar el script, asegúrate de tener instalado lo siguiente en tu sistema:

- **Python:** El script está escrito en Python, por lo que necesitarás tener Python instalado en tu máquina. Puedes descargar e instalar la última versión de Python desde [la página oficial de Python](https://www.python.org/downloads/).

- **ChromeDriver:** El script utiliza Selenium, que a su vez requiere de ChromeDriver para interactuar con las páginas web a través de Google Chrome. Puedes descargar la versión correspondiente de ChromeDriver según tu versión de Google Chrome desde [la página oficial de ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads).

## Instalación

1. **Clona el repositorio (o descarga únicamente el archivo python):**

    ```
    git clone [URL_DEL_REPOSITORIO]
    ```

2. **Instala las dependencias:**

    Navega al directorio del proyecto, abre una terminal e instala Selenium:

    ```
    pip install selenium
    ```

## Uso

Para ejecutar el script, sigue estos pasos:

1. **Configura el script:**

    Abre el archivo `check-size-of-product-zara.py` y configura las variables necesarias, como la URL del producto en la línea 12 y la talla que estás buscando.

2. **Ejecuta el script:**

    En la terminal, navega al directorio del proyecto y ejecuta el script con el siguiente comando:

    ```
    python check-size-of-product-zara.py
    ```

El script realizará la comprobación y te notificará cuando haya disponibilidad de la talla que estás buscando.

## Contribuciones

Las contribuciones son siempre bienvenidas. Si tienes alguna sugerencia o quieres contribuir al proyecto, siéntete libre de hacerlo.


---
> **Nota:** Este script está destinado únicamente a fines educativos. Asegúrate de respetar las políticas de Zara y no utilizar el script para actividades que puedan considerarse abuso o violación de los términos de servicio de la tienda.
