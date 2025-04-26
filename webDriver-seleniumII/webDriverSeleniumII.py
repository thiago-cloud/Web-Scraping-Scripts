import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep



# Configurações do navegador
options = Options()
options.add_experimental_option("detach", True)  # Impede o fechamento automático do navegador após a execução do script
options.add_argument('window-size=400,800')# Quando abrir o navegador a resolução será 400 x 800
# options.add_argument('--headless') # Executa o script no browser porém o navegador não abre fica oculto
browser = webdriver.Chrome(options=options)# Queero utilizar o google chrome com as options

# Página Home
browser.get('https://portfolio-v2-0-mu.vercel.app/')
# Espera o botão ser clicável antes de clicar
sleep(5)
label = browser.find_element(By.CSS_SELECTOR, "label[for='chk']")# Aciona o checbox
label.click()
sleep(5)# Após 5 segundos renderizando o site execute o código abaixo

# Página de Project
browser.get('https://portfolio-v2-0-mu.vercel.app/#projects')
sleep(5)

# Página de about
browser.get('https://portfolio-v2-0-mu.vercel.app/#about')
elemento = browser.find_element(By.ID, "toggle-details")
# Ativando botão experiências  
browser.execute_script("arguments[0].click();", elemento)
sleep(5)
# Desativando botão experiências  
elemento = browser.find_element(By.ID, "toggle-details")  
browser.execute_script("arguments[0].click();", elemento)
sleep(5)

# Página de contacts
browser.get('https://portfolio-v2-0-mu.vercel.app/#contacts')
sleep(5)
# Acionara o formulário disparando as validações
formulario = browser.find_element(By.TAG_NAME, "form")  
formulario.submit()

# Imprimindo no console o html da página ao abrir o browser
# site = BeautifulSoup(browser.page_source, 'html.parser')
# print(site.prettify())