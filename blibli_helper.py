import requests
from bs4 import BeautifulSoup
import dryscrape
from dryscrape.driver.webkit import Driver
import csv
import webkit_server


def get_prdouct_category_and_image(product_urls):
    img_cat_data = []
    count = 0
    server = webkit_server.Server()
    server_conn = webkit_server.ServerConnection(server=server)
    driver = dryscrape.driver.webkit.Driver(connection=server_conn)
    session = dryscrape.Session(driver = driver)

    for url in product_urls:
        # headers={"Accept" : "application/json, text/javascript, */*; q=0.01",
        #                                  "Referer": "https://www.blibli.com/p/canon-bg-e8-baterai-grip-original/ps--SUP-49229-00160?ds=SUP-49229-00160-00001&list=Product%20Listing%20Page",
        #                                  "Host": "www.blibli.com",
        #                                  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
        #                                  "Accept-Encoding":"gzip, deflate, br",
        #                                  "Accept-Language":"en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
        #                                  "X-Requested-With":"XMLHttpRequest"
        #                                  }
        # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
        # r = requests.get(url,headers=headers)
        # print (r.content)
        print ("crawling in progress -> {} ".format(count))
        print(url)
        session.visit(url)
        response = session.body()
        # session.set_timeout(30)
        session.reset()
        soup = BeautifulSoup(response, 'lxml')
        print("data fetched")
        product_image_divs = soup.findAll("div", {"class":"product__image-thumbnails--item"})

        product_imges = []
        for item in product_image_divs:
            image_tag = item.findAll("img")
            if len(image_tag)!=0:
                image_tag = image_tag[0]
                url = image_tag.get("src")
                url=url.replace("thumbnail", "full",1)
                product_imges.append(url)

        # print("categoryies")
        category_divs = soup.findAll("div",{"class":"breadcrumb__block"})
        # print(category_divs)
        categories = []
        for category in category_divs:
            cat = category.findAll("a")[0].findAll("span")[0]
            categ = cat.text.encode("utf-8")
            categories.append(categ)

        image_category = {}
        image_category["image_urls"] = ",".join(product_imges)
        image_category["cat_label"] = "->".join(categories)
        img_cat_data.append(image_category)

        write_to_csv("image_data_set",image_category)
        count=count+1
    server.kill() # the crucial line!
    return img_cat_data

def write_to_csv(csv_file, dict_data):
    try:
        with open(csv_file, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["cat_label","image_urls"])
            writer.writeheader()
            writer.writerow(dict_data)
    except IOError as (errno, strerror):
            print("I/O error({0}): {1}".format(errno, strerror))
    return
