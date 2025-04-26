import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

# Acessando o site
response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# Encontrando os blocos de notícias
# HTML da notícia
noticias = site.find_all('div', attrs={'class': 'feed-post-body'})