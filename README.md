
# Web Scraping Scripts em Python

Este repositório contém uma série de scripts em Python para web scraping, utilizando bibliotecas como `requests`, `BeautifulSoup`, `pandas` e `selenium`. O objetivo é demonstrar diferentes abordagens para extrair dados de websites populares, como notícias e produtos de e-commerce e também fazer automatizações de navegação.

## Scripts

### 1. `autoNews.py`

Este script faz o scraping de notícias do site G1 da Globo mas poderia ser qualquer outro site. Ele coleta o título, subtítulo e o link de cada notícia da página inicial e salva os dados em um arquivo Excel.

**Dependências:**
- `requests`
- `beautifulsoup4`
- `pandas`
- `openpyxl` (necessário para salvar os dados em Excel)

**Funcionamento:**
- Acessa a página principal do G1.
- Extraí as notícias utilizando o BeautifulSoup.
- Salva as informações em um arquivo `noticias.xlsx`.

**Exemplo de uso:**
```bash
python autoNews.py
```

### 2. `autoEcommerce.py`

Este script realiza uma busca no Mercado Livre com base em um produto fornecido pelo usuário. Ele coleta o título, link e preço dos produtos encontrados na busca.

**Dependências:**
- `requests`
- `beautifulsoup4`

**Funcionamento:**
- Solicita ao usuário um nome de produto.
- Realiza a busca no Mercado Livre.
- Exibe informações sobre os produtos encontrados.

**Exemplo de uso:**
```bash
python autoEcommerce.py
```

### 3. `webDriverSelenium.py`

Este script utiliza Selenium para automação no navegador Chrome, realizando navegação em uma página de portfólio e interações como pesquisa e exibição de detalhes.

**Dependências:**
- `selenium`

**Requisitos:**
- Instalar o Selenium: `pip install selenium`
- Baixar o [ChromeDriver](https://developer.chrome.com/docs/chromedriver/downloads) para o seu navegador Chrome.

**Funcionamento:**
- Acessa uma página de portfólio.
- Realiza ações como pesquisar por um termo, exibir detalhes de projetos e navegar pelas seções do site.

**Exemplo de uso:**
```bash
python webDriverSelenium.py
```

### 4. `webDriverSeleniumII.py`

Este script é uma variação do anterior, com funcionalidades similares, mas em um fluxo um pouco diferente. Ele navega por várias seções do portfólio, realiza uma pesquisa e exibe detalhes de contato.

**Dependências:**
- `selenium`

**Requisitos:**
- Instalar o Selenium: `pip install selenium`
- Baixar o [ChromeDriver](https://developer.chrome.com/docs/chromedriver/downloads) para o seu navegador Chrome.

**Funcionamento:**
- Acessa uma página de portfólio e executa uma série de navegações e interações com o conteúdo da página.

**Exemplo de uso:**
```bash
python webDriverSeleniumII.py
```

## Instalação

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/web-scraping-scripts.git
```

2. Navegue até o diretório do projeto:
```bash
cd web-scraping-scripts
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Requisitos

Este projeto utiliza as seguintes bibliotecas:
- `requests`
- `beautifulsoup4`
- `pandas`
- `selenium`

Certifique-se de ter o Python 3.x instalado em sua máquina.

