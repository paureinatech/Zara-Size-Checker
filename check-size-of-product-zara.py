from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import winsound

import time

# Talk is cheap, show me the code!

# Definimos el link del articulo sobre el que queremos tener la alerta
url_producto= 'https://www.zara.com/es/es/pantalon-ancho-piel-limited-edition-p05479326.html?v1=317792471&v2=2352556'
# Definimos la talla que nos interesa consultar 
talla_elegida = 'm'
# Definimos si estamos buscando usando el catalogo de tallas de pantalon de mujer, sino usará las tallas de pantalon de hombre (escribir si o no)
tallas_mujer = 'si'
# Se inicia la ventana del navegador
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Se escribe el link al artículo
driver.get(url_producto)



# Generamos las tablas de equivalencia de tallas numericas de pantalones y de medidas
id_talla = {'xs': 0, 's': 1, 'm': 2, 'l': 3, 'xl': 4, 'xxl':5, 'xxxl':6}
# Las tallas numericas de pantalones de mujer comienzan por talla 32 mientras que las de hombre por talla 34
id_talla_numerica = {'32': 0, '34': 1, '36': 2, '38': 3, '40': 4, '42':5, '44':6, '46': 7}

# Declaramos los parametros de nuestro proceso
process_sleep_time = 20
error_tallas = 'No se encontro la talla definida'
elemento_ul = 'ul[id*="product-size-selector"]'
elemento_li = 'li'
elemento_class = 'class'
Alarm_sound = "SystemHand"
print_talla = "TALLA "
print_disponible = " DISPONIBLE"
sin_existencias = "out-of-stock"
mensaje_actualizando = "------- Actualizando web -------- \n"
error_elemento_no_encontrado = "No se encontró el elemento "
confirmacion_talla_mujer = 'si'

# Se almacena el id de la talla, en caso de no ser encontrada como talla se comprueba como medida de pantalon
num = id_talla.get(talla_elegida.lower(), 999)

if num == 999 and tallas_mujer == confirmacion_talla_mujer.lower():
    num = id_talla_numerica.get(talla_elegida.lower(),error_tallas)

if num == 999 and tallas_mujer != confirmacion_talla_mujer.lower():
    num = id_talla_numerica.get(talla_elegida.lower(),error_tallas)-2


try:
    while 1:
        # El bloque de las tallas se ubica dentro de un elemento <ul> por lo tanto se busca que ese elemento contenga el id que se quiere
        ul_element = driver.find_element(By.CSS_SELECTOR, elemento_ul)

        # Se traen los bloques de elementos li que son los de las tallas
        li_elements = ul_element.find_elements(By.TAG_NAME, elemento_li)
        
        # Se guarda el elemento que corresponda a la talla seleccionada
        talla = li_elements[num]

        # Se guarda el atributo <class> que indica si está fuera de stock o no
        class_name = talla.get_attribute(elemento_class)
        
        # Si no aparece el texto out-of-stock significa que hay talla
        if sin_existencias not in class_name:
            for i in range(10):
                # Imprime 10 veces el texto
                print(print_talla + talla_elegida.upper() + print_disponible)

                # Se reproducen 10 pitidos
                winsound.PlaySound(Alarm_sound, winsound.SND_ALIAS)
        else:
            # Se duerme al proceso x segundos           
            time.sleep(process_sleep_time)

        # Se actualiza la página
        print(mensaje_actualizando)
        driver.refresh()


except NoSuchElementException as e:
    print(error_elemento_no_encontrado + str(e))

#except Exception as e:
#   print("Error: " + str(e))

# Cierra el navegador
driver.quit()
