# scraping titles

import requests
from bs4 import BeautifulSoup, NavigableString

eu_links = [
    'https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32014L0065&from=EN',
    'https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32014R0596&from=EN',
    'https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32017R0590&from=EN',
    'https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32014R0600',
    'https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32014L0059',
    'https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R1712&from=EN',
    'https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A32012R0648',
    'https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32017R1443',
    'https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A32012R0648',
    'https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32015R2365',
    'https://eur-lex.europa.eu/eli/reg_del/2019/356/oj',
    'https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02013R0153-20160615', # doesn't export the title
    'https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32013R0148'
]


data = {}
html = requests.get('https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32014L0065&from=EN#d1e1592-349-1')
bs = BeautifulSoup(html.text, 'html.parser')


def get_title(link):
    html = requests.get(link)
    bs = BeautifulSoup(html.text, 'html.parser')
    return [i.get_text().replace('&nbsp;', '') for i in bs.body.find_all('p', {'class': 'doc-ti'})[:5] if not isinstance(i, NavigableString)]


for index, link in enumerate(eu_links):
    data[str(index) + ' title'] = '\n'.join(get_title(link))
with open('titles.txt', 'w') as file:

    for page in data:
        file.write(data[page])
        file.write('\n')
