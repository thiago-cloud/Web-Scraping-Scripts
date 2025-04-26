
# > EXEMPLO
# - Obtendo produtos do Mercado Livre a partir de uma busca realizada pelo usuário

import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'

produto_nome = input('Qual produto você deseja? ')

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.find_all('div', attrs={'class': 'ui-search-result__wrapper'})

for produto in produtos:
    # Busca o título do produto (geralmente é um link com o nome do item)
    titulo = produto.find('a', attrs={'class': 'poly-component__title'})
    
    # Busca o link do produto (o mesmo elemento do título, pois o link está no <a>)
    link = produto.find('a', attrs={'class': 'poly-component__title'})

    # Busca a parte inteira do preço (antes da vírgula)
    real = produto.find('span', attrs={'class': 'andes-money-amount__fraction'})
    
    # Busca os centavos do preço (depois da vírgula), se existirem
    centavos = produto.find(
        'span',
        attrs={'class': 'andes-money-amount__cents andes-money-amount__cents--superscript-24'}
    )

    # Mostra a estrutura completa do produto em HTML (comentado por padrão)
    # print(produto.prettify())

    # Exibe o título do produto
    print('Título do produto: ', titulo.text)
    
    # Exibe o link para acessar o produto
    print('Link do produto: ', link['href'])

    # Verifica se os centavos foram encontrados
    if (centavos):
        # Exibe o preço no formato "reais,centavos"
        print('Preço do produto: R$', real.text + ',' + centavos.text)
    else:
        # Se não houver centavos, exibe apenas os reais
        print('Preço do produto: R$', real.text)
    
    # Linha em branco para separar os produtos visualmente
    print('\n\n')