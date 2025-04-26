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

# Extraindo informações de cada notícia
for noticia in noticias:
  # Título
  titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

  # print(titulo.text)
  # print(titulo['href']) # link da notícia

  # Subtítulo: div class="feed-post-body-resumo"
  subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})

  if (subtitulo):
    # print(subtitulo.text)
    lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
  else:
    lista_noticias.append([titulo.text, '', titulo['href']])


# Criando um DataFrame e exportando
news = pd.DataFrame(lista_noticias, columns=['Título', 'Subtítulo', 'Link'])

# Salvando no execel
# Para funcionar e necessário instalar o openpyxl
news.to_excel('noticias.xlsx', index=False)

# print(news)