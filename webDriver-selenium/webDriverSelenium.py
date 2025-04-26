# E necessário antes instalar o selenium
# pip install selenium
# Para o codigo python funcionar o no navegador e necessário fazer integração do código
# Isso será possivel ao instalar o driver de integração o link é: 
# https://developer.chrome.com/docs/chromedriver/downloads -> driver para o chrome 

# Importa as bibliotecas necessárias do Selenium e a função sleep para pausar a execução
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

# Configurações do navegador
options = Options()
options.add_experimental_option("detach", True)  # Impede o fechamento automático do navegador após a execução do script

# Inicializa o navegador Chrome com as opções configuradas
driver = webdriver.Chrome(options=options)

# Acessa a página inicial do portfólio
driver.get("https://portfolio-v2-0-mu.vercel.app/")
sleep(5)  # Aguarda 5 segundos para garantir que a página seja carregada completamente

# Navega até a seção de projetos do portfólio
driver.get("https://portfolio-v2-0-mu.vercel.app/#projects")
# Localiza o campo de pesquisa pelo ID 'searchInput'
elemento = driver.find_element(By.ID, 'searchInput')
# Insere o texto 'data' no campo de pesquisa
elemento.send_keys('data')
sleep(5)  

# Navega até a seção "Sobre" do portfólio
driver.get("https://portfolio-v2-0-mu.vercel.app/#about")
# Localiza o botão ou link com o ID 'toggle-details' (possivelmente para exibir mais informações)
elemento = driver.find_element(By.ID, 'toggle-details')
sleep(5)  

# Navega até a seção de contatos do portfólio
driver.get("https://portfolio-v2-0-mu.vercel.app/#contacts")
sleep(5)  

# Retorna à página inicial do portfólio
driver.get("https://portfolio-v2-0-mu.vercel.app/")