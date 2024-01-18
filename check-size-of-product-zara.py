from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import winsound

import time

# Se inicia la ventana del navegador
driver = webdriver.Chrome()

# Se escribe el link al artículo
driver.get('https://www.zara.com/es/es/plumifero-acolchado-semilargo-capucha-p08073203.html?v1=267165715&origin=shopcart')

try:
    while 1:
        # El bloque de las tallas se ubica dentro de un elemento <ul> por lo tanto se busca que ese elemento contenga el id que se quiere
        ul_element = driver.find_element(By.CSS_SELECTOR, 'ul[id*="product-size-selector"]')

        # Se traen los bloques de elementos li que son los de las tallas
        li_elements = ul_element.find_elements(By.TAG_NAME, 'li')
        
        # Se guarda el segundo elemento (1) que es la talla S
        talla_s = li_elements[1]

        # Se guarda el atributo <class> que indica si está fuera de stock o no
        class_name = talla_s.get_attribute('class')
        
        # Si no aparece el texto out-of-stock significa que hay talla
        if "out-of-stock" not in class_name:
            for i in range(10):
                # Imprime 10 veces el texto
                print("TALLA S DISPONIBLE")

                # Se reproducen 10 pitidos
                winsound.PlaySound("SystemHand", winsound.SND_ALIAS)

        # Se realiza lo mismo para talla M
        talla_m = li_elements[2]
        class_name2 = talla_m.get_attribute('class')
        if "out-of-stock" not in class_name2:
            for i in range(10):
                print("TALLA M DISPONIBLE")
                winsound.PlaySound("SystemHand", winsound.SND_ALIAS)

        # Se duerme al proceso 60 segundos           
        time.sleep(40)

        # Se actualiza la página
        print("------- Actualizando web -------- \n")
        driver.refresh()


except NoSuchElementException as e:
    print("No se encontró el elemento " + str(e))

# Cierra el navegador
driver.quit()
