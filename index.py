# O selenium vai abrir o navegador e buscar no html o que vai ser analisado.

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# a classe service vai iniciar uma instância do chrome webdriver
service = Service()
# com essa instância o código vai conseguir acessar o html no navegador

# para habilitar ainda tem mais duas linhas de código.

options = webdriver.ChromeOptions()
#webdriver.ChromeOptions define a preferência para o Chrome

driver = webdriver.Chrome(service=service , options=options)
# vai iniciar a instância do chrome webdriver com as options e services

# para buscar o site através da url e abrir

url = 'https://books.toscrape.com/'
driver.get(url)

# encontrando elementos através de tags
#resultado = driver.find_elements(By.TAG_NAME, 'a')
resultado = driver.find_element(By.TAG_NAME,'a').text
print(resultado)