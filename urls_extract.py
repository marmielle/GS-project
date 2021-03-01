# extracting links from the website

import requests
import re
from time import sleep
import os

save_dir = 'regulations/'
domain = 'http://eur-lex.europa.eu/'
page_base_url = 'https://eur-lex.europa.eu/search.html?instInvStatus=ALL&qid=1407932788225&type=advanced&lang=en&SUBDOM_INIT=EU_CASE_LAW&FM_CODED=REG&page='
hook_text = './legal-content/EN/TXT/HTML/?'
html_link_re = re.compile(r'./legal-content/EN/TXT/HTML/[^"]*')

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

for i in range(1, 10):
    response = requests.get(page_base_url + str(i))
    for path in re.findall(html_link_re, response.text):
        sleep(1)
        continua = 1

        urls = domain + path[2:]
        print(urls)
