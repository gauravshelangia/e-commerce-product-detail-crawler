import requests
from bs4 import BeautifulSoup
from blibli_helper import

def get_product_detail_urls(url):
    url = "https://www.blibli.com/jual/mta-1410922?s=MTA-1410922"
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'}
    r = requests.get(url,headers=headers)

    soup = BeautifulSoup(r.content)

    product_detail_divs = soup.findAll("div",{"class":"large-4 medium-5 small-8 columns"})
    product_urls = []
    for item in product_detail_divs:
        url = item.findAll("a",{"class":"single-product"})[0]
        product_urls.apeend(url.get("href"))
    return product_urls
