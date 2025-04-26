
# > EXEMPLO
# - Obtendo produtos do Mercado Livre a partir de uma busca realizada pelo usuário

import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'

produto_nome = input('Qual produto você deseja? ')

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.find_all('div', attrs={'class': 'ui-search-result__wrapper'})