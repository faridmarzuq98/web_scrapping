# Import library
from bs4 import BeautifulSoup

import requests

main_URL = "https://quotes.toscrape.com"
quotes = []
page_num = 1

while True:
    print('page_num: ', page_num)
    
    # Get URL and its contents
    URL = "https://quotes.toscrape.com/page/{}".format(page_num)
    r = requests.get(URL)
    
    soup = BeautifulSoup(r.content, 'html5lib')
    next_page = soup.div.nav.ul.find('li', attrs = {'class': 'next'})
    
    # Looking the content
    table = soup.find_all('div', attrs = {'class': 'row'})
    table_choosed = table[1]
    
    # Get the content
    itr = table_choosed.find_all('div', attrs = {'class': 'quote'})
    
    for row in itr:
        quote = {}
        quote['quote'] = row.find_all('span')[0].text
        quote['author'] = row.find_all('span')[1].small.text
        quote['author_bio'] = main_URL + row.find_all('span')[1].a['href']
        
        tags_itr = row.div.find_all('a')
        tags_list = []
        
        for row2 in tags_itr:
            tags_list.append(row2.text)
        
        quotes.append(quote)
        
    # End Page detection    
    if next_page is None:
        break
    else:
        page_num += 1
