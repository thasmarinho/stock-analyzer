import requests
from bs4 import BeautifulSoup as bs
from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    base_url = "https://www.fundamentus.com.br/detalhes.php?papel="
    stock = "ITSA4"
    url = base_url + stock

    fundamentus_r = requests.get(url)
    fundamentus_soup = bs(fundamentus_r.text, 'html.parser')

    #print(fundamentus_soup.prettify())
    #print(fundamentus_soup.findAll('span'))
    #print(fundamentus_soup.findAll('span', {'class': 'txt'}))

    #for link in fundamentus_soup.findAll('span', {'class': 'txt'}):
    #    print(link.text)

    price_per_stock_unit = fundamentus_soup.find('td', {'class':'data destaque w3'}).text
    return price_per_stock_unit

if __name__ == '__main__':
    app.run(debug=True)
