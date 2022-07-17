import csv

# import pandas as pd
import requests
from xml.etree import ElementTree as ET

DATA_FILE = "BISSU CSV(1).csv"
# file_read = pd.read_csv(r'BISSU CSV(1).csv')
# sub = pd.DataFrame(file_read, columns=['PRODUCTO', 'PRECIO-DE-LISTA', 'MAYOREO-ALTO-VOLUMEN','ID-PARENT'])
rows = []
with open(DATA_FILE) as f:
    reader = csv.reader(f)
    next(reader)
    next(reader)
    for row in reader:
        rows.append([
            row[0],
            row[1],
            row[2],
            row[3]
        ])

FILENAME = "product-blank-schema.xml"
KEY = "I7YVA346QJZZVH1PLGFF9FSJ642A6DDZ"
HOST = "@bissusonora.com/api/products/"
URL = "http://" + KEY + HOST
HEADERS = {
    "Content-Type": "application/xml",
    'User-Agent': "PostmanRuntime/7.29.0",
    "Authorization": "Basic STdZVkEzNDZRSlpaVkgxUExHRkY5RlNKNjQyQTZERFo6",
    "Accept": "*/*",
    "Postman-Token": "387208ac-1103-45af-9266-c2d3c9eea34f",
    "Host": "bissusonora.com",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}


# for row_number in sub.index:
# print(sub['PRODUCTO'][row_number], + - + sub['ID-PARENT'][row_number])

def create_product():
    with open("Prueba2product-blank-schema.xml") as xml:
        print(xml)
        r = requests.post(URL, data=xml, headers=HEADERS)
        print(r.status_code)
        # print(r.content)
        print()


tree = ET.parse(FILENAME)
# for row_number in sub.index:
#     if row_number == 1:
#         tree.find('.//price').text = str(sub['PRECIO-DE-LISTA'][row_number])
#         tree.find('.//wholesale_price').text = str(sub['MAYOREO-ALTO-VOLUMEN'][row_number])
#         tree.find('.//name/language').text = str(sub['PRODUCTO'][row_number])
#         tree.find('.//id_category_default').text = str(int(sub['ID-PARENT'][row_number])) or ""
#         #tree.find('.//category/id').text = str(int(sub['SUB-CATEGORY'][row_number]))
#         tree.write("Prueba2" + FILENAME, encoding='utf8', method='xml', xml_declaration=True)
#         #create_product()
for row in rows[1:]:
    print(row[0])
    tree.find('.//name/language').text = row[0]
    tree.find('.//price').text = row[1]
    tree.find('.//wholesale_price').text = row[2]
    tree.find('.//id_category_default').text = row[3]
    # tree.find('.//category/id').text = str(int(sub['SUB-CATEGORY'][row_number]))
    tree.write("Prueba2" + FILENAME, encoding='utf8', method='xml')
    create_product()
