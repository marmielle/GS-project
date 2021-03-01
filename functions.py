# scraping attempt 2 - better -> structured text

import requests
from bs4 import BeautifulSoup, NavigableString
url = 'https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32014L0065&from=EN'
bs = BeautifulSoup(requests.get(url).text, 'html.parser')


def get_articles(body_tag, navi_obj):
    data = dict.fromkeys((i.get_text() for i in body_tag.find_all('p', class_='ti-art')), None)
    data['Title'] = []

    delimiter = 'Title'
    for tag in body_tag:
        if isinstance(tag, navi_obj):
            continue

        if 'class' in tag.attrs and 'ti-art' in tag.attrs['class']:
            if tag.name == 'p':
                delimiter = tag.get_text()
                data[delimiter] = []
                continue
        if tag.name in ('table', 'p'):
            try:
                data[delimiter].append(tag.get_text().replace('\n', ' ').strip())
            except TypeError:
                continue
    return data

result = get_articles(bs.body, NavigableString)
for article in result:
    if result[article]:
        print(article)
        for par in result[article]:
            print(par)
        print('-'*30)