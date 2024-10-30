import scrape

import requests
from bs4 import BeautifulSoup


pagina_start = 'https://www.olx.ro/auto-masini-moto-ambarcatiuni/autoturisme/'

response = requests.get(pagina_start)
soup = BeautifulSoup(response.text, 'html.parser')

lista_anunturi = soup.find_all('div', class_='css-1apmciz')

for tag_anunt in lista_anunturi:
    hyperlink_tag= tag_anunt.find('a', class_='css-z3gu2d')
    hyperlink = hyperlink_tag.get("href")
    if hyperlink.startswith('/d/oferta/'):
        link_anunt = 'https://www.olx.ro' + hyperlink
        scrape.get_data(link_anunt)