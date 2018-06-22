import requests
from bs4 import BeautifulSoup


def get_prdouct_category_and_image(product_urls):
    print("coming here", len(product_urls))
    for url in product_urls:
        headers={"Accept" : "application/json, text/javascript, */*; q=0.01",
                                         "Referer": "https://www.blibli.com/p/canon-bg-e8-baterai-grip-original/ps--SUP-49229-00160?ds=SUP-49229-00160-00001&list=Product%20Listing%20Page",
                                         "Host": "www.blibli.com",
                                         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
                                         "Accept-Encoding":"gzip, deflate, br",
                                         "Accept-Language":"en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
                                         "X-Requested-With":"XMLHttpRequest"
                                         }
        # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
        r = requests.get(url,headers=headers)
        print (r.content)
        soup = BeautifulSoup(r.content, 'lxml')

        product_image_divs = soup.findAll("div")

        print(product_image_divs)
        product_imges = []
        for item in product_image_divs:
            image_div = item.findAll("div",{"class":"product__image-thumbnails--item"})[0]
            image_tag = image_div.find("img")
            url = image_tag.get("src")
            product_imges.append(url)

        print(product_imges)
        print("categoryies")
        category_divs = soup.findAll("div",{"class":"breadcrumb"})
        print(category_divs)
        for category in category_divs:
            cat = category.findAll("div",{"class":"breadcrumb__block"})
            print(cat)
            label = cat.findAll("span").text
            print(label)
