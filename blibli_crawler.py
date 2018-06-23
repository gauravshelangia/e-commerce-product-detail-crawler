import requests
from bs4 import BeautifulSoup
from blibli_helper import get_prdouct_category_and_image
from blibli_utils import get_product_detail_urls
import csv
import time

url = "https://www.blibli.com/jual/"

with open('product_codes.txt') as f:
    lines = f.read().splitlines()

def WriteDictToCSV(csv_file,dict_data):
    try:
        with open(csv_file, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["cat_label","image_urls"])
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError as (errno, strerror):
            print("I/O error({0}): {1}".format(errno, strerror))
    return

total = len(lines)
count=1
for i in range(220,300):
    print("Running ==> {}/{}".format(i,total) )
    product_urls = get_product_detail_urls(url+lines[i]+"?s="+lines[i])
    img_cat_data = get_prdouct_category_and_image(product_urls)
    print("Completed ==> {}/{}".format(i,total) )
    time.sleep(3)
    count=count+1
