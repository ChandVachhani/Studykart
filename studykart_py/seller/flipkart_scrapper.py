from bs4 import BeautifulSoup
import requests


def flipkart_money(product, price):
    product = product[0:1]
    price = price[0:1]
    all_product = []
    num = 1
    for i, j in zip(product, price):
        all_product.append([i.text, j.text])
    return all_product[0]


def flipkart_link(product):
    scarpping_url = 'https://www.flipkart.com/search?q='
    product = product.split()
    for i in product:
        scarpping_url += i
        scarpping_url += "+"
    scarpping_url = scarpping_url[:-1]
    return scarpping_url


def flipkart_data(product):
    scarpping_url = 'https://www.flipkart.com/search?q='
    product = product.split()
    for i in product:
        scarpping_url += i
        scarpping_url += "+"
    scarpping_url = scarpping_url[:-1]
    try:
        list = requests.get(scarpping_url)
        list = list.content
        soup = BeautifulSoup(list, 'lxml')
        product = soup.findAll('a', {'class': '_2cLu-l'})
        price = soup.findAll("div", {"class": "_1vC4OE"})

        if (len(product) == 0 or len(price) == 0):
            product = soup.findAll('div', {'class': "_3wU53n"})
            price = soup.findAll("div", {"class": "_1vC4OE _2rQ-NK"})

        if (len(product) > 0 and len(price) > 0):
            return flipkart_money(product, price)
        else:
            return -1
    except:
        return 'You are not connected to internet'

