import requests
from bs4 import BeautifulSoup as bs

url = "https://www.fundamentus.com.br/detalhes.php?papel=ITSA4"

fundamentus_r = requests.get(url)
fundamentus_soup = bs(fundamentus_r.text, 'html.parser')

print(fundamentus_soup.prettify())
