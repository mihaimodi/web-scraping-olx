import scrape

import requests
from bs4 import BeautifulSoup


pagina = 'https://www.olx.ro/auto-masini-moto-ambarcatiuni/autoturisme/'



while True:
    response = requests.get(pagina)
    soup = BeautifulSoup(response.text, 'html.parser')
    lista_anunturi = soup.find_all('div', class_='css-1apmciz')

    for tag_anunt in lista_anunturi:
        hyperlink_tag= tag_anunt.find('a', class_='css-z3gu2d')
        hyperlink = hyperlink_tag.get("href")
        if hyperlink.startswith('/d/oferta/'):
            link_anunt = 'https://www.olx.ro' + hyperlink
            scrape.get_data(link_anunt)

    lista_pagini = soup.find('ul', class_='pagination-list')
    link_pagina_urm = lista_pagini.find('a', {'data-testid': 'pagination-forward'})
    if link_pagina_urm:
        pagina_urm = 'https://www.olx.ro' + link_pagina_urm.get('href')
    else:
        break