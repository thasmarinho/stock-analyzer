from flask import render_template
from flask import request as r
import requests
from bs4 import BeautifulSoup as bs
from app import app

@app.route('/price')
def price():
    base_url = "https://www.fundamentus.com.br/detalhes.php?papel="
    stock = r.args.get('stock', default = 1, type = str)
    url = "https://www.fundamentus.com.br/detalhes.php?papel="+stock

    fundamentus_r = requests.get(url)
    fundamentus_soup = bs(fundamentus_r.text, 'html.parser')

    price_per_stock_unit = fundamentus_soup.find('td', {'class':'data destaque w3'}).text
    return render_template("index.html", stock_code = stock, price = price_per_stock_unit)

@app.route('/')
def index():
    return render_template("index.html", stock_code = "TEST", price = "0.00")
@app.route('/about')
def about():
    return render_template("about.html")
