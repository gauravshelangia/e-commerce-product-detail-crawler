import requests
from bs4 import BeautifulSoup


def get_prdouct_category_and_image(product_urls):
    print("coming here", len(product_urls))
    for url in product_urls:
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'}
        r = requests.get(url,headers=headers)
        # print (r.content)
        soup = BeautifulSoup(r.content, "lxml")

        product_image_divs = soup.findAll("div",{"class":"product__image-thumbnails"})

        print(product_image_divs)
        product_imges = []
        for item in product_image_divs:
            image_div = item.findAll("div",{"class":"product__image-thumbnails--item"})[0]
            image_tag = image_div.find("img")
            url = image_tag.get("src")
            product_imges.append(url)

        print(product_imges)
        category_divs = soup.findAll("div",{"class":"breadcrumb"})
        for category in category_divs:
            cat = category.findAll("div",{"class":"breadcrumb__link"})[0]
            print(cat)
            label = cat.findAll("span").text
            print(label)
