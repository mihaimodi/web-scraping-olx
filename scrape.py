import requests
import json
from bs4 import BeautifulSoup

def get_data(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    script_tag = soup.find('script', {'id': 'olx-init-config'})

    script_content = script_tag.string.splitlines()[4]
    json_data_str = script_content.replace('window.__PRERENDERED_STATE__= ', '').strip().rstrip(';').strip('"')
    json_data_str = bytes(json_data_str, "utf-8").decode("unicode_escape")
    
    json_array = json.loads(json_data_str)
    pret = json_array['ad']['ad']['price']['regularPrice']['value']
    valuta = json_array['ad']['ad']['price']['regularPrice']['currencyCode']
    firma = json_array['ad']['breadcrumbs'][3]['label']
    date_anunt = json_array['ad']['ad']['params']
    nr_km = '?'; model = '?'; combustibil = '?'; capacitate_cilindrica = '?'; an = '?'
    for data in date_anunt:
        if data['key'] == 'rulaj_pana':
            nr_km = data['normalizedValue']
        elif data['key'] == 'model':
            model = data['value']
        elif data['key'] == 'year':
            an = data['normalizedValue']
        elif data['key'] == 'enginesize':
            capacitate_cilindrica = data['normalizedValue']
        elif data['key'] == 'petrol':
            combustibil = data['normalizedValue']
    print(firma + ' ' + model + ' ' + str(an))
    print(capacitate_cilindrica + ' cm3 ' + combustibil)
    print(str(nr_km) + ' km')
    print(str(pret) + ' ' + valuta)
