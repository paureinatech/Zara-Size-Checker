from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import winsound
import os
import time

# Configuración de opciones de Chrome para que no muestre logs extraños
options = webdriver.ChromeOptions()
options.add_argument("--disable-background-timer-throttling") 
options.add_argument("--disable-features=PlatformMonitor") 
options.add_argument("--log-level=3")
options.add_argument("--disable-logging")

# Inicialización del navegador
driver = webdriver.Chrome(
    service=ChromeService(os.path.join(os.path.dirname(ChromeDriverManager().install()), "chromedriver.exe")),
    options=options
)

# Se escribe el link al artículo
driver.get('https://www.zara.com/es/es/blazer-satinada-oversize-p08900366.html?v1=388142376&v2=2417363')

# Se escribe la talla que se quiere
talla_elegida = 'm'

# Se almacena el id de la talla
id_talla = {'xs': 0, 's': 1, 'm': 2, 'l': 3, 'xl': 4, 'xxl':5}
num = id_talla.get(talla_elegida.lower(), "Entrada no válida")

try:
    while 1:
        # El bloque de las tallas se ubica dentro de un elemento <ul> por lo tanto se busca que ese elemento contenga el id que se quiere
        ul_element = driver.find_element(By.CSS_SELECTOR, 'ul.size-selector-sizes.size-selector-sizes--grid-gap')


        # Se traen los bloques de elementos li que son los de las tallas
        li_elements = ul_element.find_elements(By.TAG_NAME, 'li')
        
        # Se guarda el elemento que corresponda a la talla seleccionada
        talla = li_elements[num]

        # Se guarda el atributo <class> que indica si está fuera de stock o no
        class_name = talla.get_attribute('class')
    
        # Si no aparece el texto out-of-stock significa que hay talla
        if "unavailable" not in class_name:
            for i in range(10):
                # Imprime 10 veces el texto
                print("TALLA " + talla_elegida.upper() + " DISPONIBLE")

                time.sleep(2)
                # Se reproducen 10 pitidos
                winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        else:
            print("--- No hay talla disponible")
            # Se duerme al proceso x segundos           
            time.sleep(20)

        # Se actualiza la página
        print("------- Actualizando web -------- \n")
        driver.refresh()


except NoSuchElementException as e:
    print("No se encontró el elemento " + str(e))

#except Exception as e:
#   print("Error: " + str(e))

# Cierra el navegador
driver.quit()