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

driver.get('https://books.toscrape.com/')

#---------------ENCONTRANDO ELEMENTOS ATRAVÉS DE TAGS------------------------------

#-----  assim retorna o que está atribuído a title do elemento 54   -----
#resultado = driver.find_elements(By.TAG_NAME, 'a')[54].get_attribute('title') 

#-----  assim retorna o que está atribuído a title do elemento 54 até 94 de 2 em 2   -----
#resultado = driver.find_elements(By.TAG_NAME, 'a')[54:94:2][0].text 

#-----  assim retorna o que está escrito no link  -----
#resultado = driver.find_element(By.TAG_NAME,'a').text    

#print(resultado)


#title = driver.title
#print(title)

#--------------------CRIANDO UMA LISTA----------------------------------------------


#resultado = len(driver.find_elements(By.TAG_NAME, 'a')[54:94:2])
#print(resultado, 'livros')

#resultado = driver.find_elements(By.TAG_NAME, 'a')[54:94:2]
#for R in resultado:
#    print(R.text)

resultado = driver.find_elements(By.TAG_NAME, 'a')[54:94:2]
title = [title.get_attribute('title') for title in resultado]
#print(title)

#resultado[0].click()

estoque = []
for td in resultado:
    td.click()
    quantLivros = int(driver.find_element(By.CLASS_NAME, 'instock').text.replace('In stock (','').replace('available)', ''))
    #print(quantLivros)
    estoque.append(quantLivros)
    driver.back()
#print(estoque)



#tabela

# Ajustar o número máximo de caracteres exibidos por coluna
pd.set_option('display.max_colwidth', None)

df = {'titulo' : title, 'estoque': estoque}

tabela = pd.DataFrame(df)

print(tabela)

tabela.to_excel('estoque_produtos.xlsx', index=False)