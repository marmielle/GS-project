import bs4 as bs
import urllib.request as ur
import requests

url_list = [
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

texts=[]

for url in url_list:
    scraped_url = ur.urlopen(url)
    article = scraped_url.read()
    parsed_article = bs.BeautifulSoup(article,'lxml')
    paragraphs = parsed_article.find_all('p')
    text = ""
    for p in paragraphs:
        text += p.text
    texts.append(text)

print(len(texts))

str1 = ''.join(str(e) for e in texts)

str1.split('\n')

with open('text.txt','w') as file:
  file.write(str1)
