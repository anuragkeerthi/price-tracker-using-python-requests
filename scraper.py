import requests
from bs4 import BeautifulSoup

#Paste the URL of the Product you wish
URL = 'https://www.amazon.in/Lenovo-Windows-Graphics-Phantom-82AU00G8IN/dp/B08GG87CG3/ref=sr_1_4?crid=4PCHQFJE72V8&dchild=1&keywords=lenovo+legion&qid=1600882364&s=computers&sprefix=lenovo+le%2Ccomputers%2C332&sr=1-4'

headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

# Get the id from the Webpage, by clicking f12 and inspecting the element
title = soup.find(id = "productTitle").get_text().strip()
price = soup.find(id = "priceblock_ourprice").get_text().strip()
converted_price = float(price[2:].replace(',',''))
print(converted_price)


