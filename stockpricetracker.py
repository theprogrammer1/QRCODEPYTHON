import requests
from bs4 import BeautifulSoup
url = 'https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
print(price)
# you will need to get the url from yahoo finance!
