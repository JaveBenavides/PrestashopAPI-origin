import pandas as pd
import requests
from xml.etree import ElementTree as ET


file_read = pd.read_csv(r'/home/bunker-2/Desktop/csv-complete.csv')
sub = pd.DataFrame(file_read, columns=['PRODUCTO', 'PRECIO-DE-LISTA', 'MAYOREO-ALTO-VOLUMEN','ID-PARENT','SUB-CATEGORY'])


FILENAME = "product-blank-schema.xml"
KEY = "I7YVA346QJZZVH1PLGFF9FSJ642A6DDZ"
HOST = "@bissusonora.com/api/products/"
URL = "http://" + KEY + HOST
HEADERS = HEADERS = {
    "Content-Type": "application/xml",
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    "Authorization": "Basic STdZVkEzNDZRSlpaVkgxUExHRkY5RlNKNjQyQTZERFo6"
}

# for row_number in sub.index:
    # print(sub['PRODUCTO'][row_number], + - + sub['ID-PARENT'][row_number])

def create_product():
    with open("pruebaproduct-blank-schema.xml") as xml:
        r = requests.post(URL, data=xml, headers=HEADERS)

tree = ET.parse(FILENAME)
for row_number in sub.index:
    if row_number == 1436:
        tree.find('.//price').text = str(sub['PRECIO-DE-LISTA'][row_number])
        tree.find('.//wholesale_price').text = str(sub['MAYOREO-ALTO-VOLUMEN'][row_number])
        tree.find('.//name/language').text = str(sub['PRODUCTO'][row_number])
        tree.find('.//id_category_default').text = str(int(sub['ID-PARENT'][row_number]))
        tree.find('.//category/id').text = str(int(sub['SUB-CATEGORY'][row_number]))
        tree.write("Prueba1" + FILENAME, encoding='utf8', method='xml', xml_declaration=True)
