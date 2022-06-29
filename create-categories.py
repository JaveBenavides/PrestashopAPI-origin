import requests
from xml.etree import ElementTree as ET

categories = [
    ("BROCHA PROFESIONAL", 15),
    ("FUNDA PARA SET DE BROCHAS", 15),
    ("COSMETIQUERAS", 15),
    ("BRILLO LABIAL", 10),
    ("BRILLO LABIAL FRUTAS", 10),
    ("DELINEADOR RETRACTIL LABIOS", 10),
    ("LABIAL HUMECTANTE", 10),
    ("LABIAL INTENSITY", 10),
    ("LABIAL MATTE", 10),
    ("LABIAL MAGICO", 10),
    ("SACAPUNTAS DUO INTENSITY", 15),
    ("SACAPUNTAS TINTA LINE", 15),
    ("TINTA MATTE", 10),
    ("TINTALINE LABIOS", 10),
    ("TINTAS", 10),
    ("DELINEADOR LIQUIDO", 11),
    ("DELINEADOR RETRACTIL OJOS", 11),
    ("LAPIZ PARA CEJAS", 11),
    ("MASCARA DE PESTANAS EXPLOSIVE", 11),
    ("PLUMIN DELINEADOR", 11),
    ("PLUMIN DELINEADOR PARA CEJAS", 11),
    ("POLVO PARA CEJAS", 11),
    ("PRIMER PARA OJOS", 11),
    ("SOMBRA CUARTETO", 11),
    ("SOMBRA EN POLVO", 11),
    ("SOMBRA INDIVIDUAL COMPACTA", 11),
    ("SOMBRA OCTETO", 11),
    ("SOMBRA QUINTETO", 11),
    ("TINTALINE OJOS", 11),
    ("PROBADORES", 16),
    ("BRONCEADOR PROFESIONAL", 13),
    ("CONTORNEADOR", 13),
    ("CORRECTOR", 13),
    ("CORRECTOR EN BARRA PROFESIONAL", 13),
    ("CORRECTOR LIQUIDO", 13),
    ("ESPONJAS", 13),
    ("GLITTER", 13),
    ("ILUMINADORES", 13),
    ("KIT ILUMINADORES Y BRONCEADORE", 13),
    ("KIT MAQUILLAJE MI TIERRA", 13),
    ("KIT MAQUILLAJE OCASION", 13),
    ("MAQUILLAJE COMPACTO", 13),
    ("MAQUILLAJE LIQUIDO", 13),
    ("POLVO FIJADOR", 13),
    ("PRIMER", 13),
    ("RUBOR PROFESIONAL REDONDO", 13),
    ("ESMALTE 15 ML", 12),
    ("ESMALTE METALICO 12 ML", 12),
    ("ESMALTE MINI 5 ML", 12),
    ("LIMA 3 PASOS", 12),
    ("LIMA NEGRA", 12),
    ("MINI LIMA NEGRA", 12),
    ("TRATAMIENTOS PROFESIONALES", 12),
    ("XIOMARA", 12),
]
FILENAME = "category-blank-schema.xml"
KEY = "I7YVA346QJZZVH1PLGFF9FSJ642A6DDZ"
HOST = "@bissusonora.com/api/categories/"
URL = "http://" + KEY + HOST
HEADERS = {"Content-Type": "application/xml"}


def create_category(data):
    with open("COPYcategory-blank-schema.xml") as xml:
        print(xml)
        r = requests.post(URL, data=xml, headers=HEADERS)
        print(r.content)


tree = ET.parse(FILENAME)
for cat in categories:
    id_parent = cat[1]
    tree.find('.//id_parent').text = str(id_parent)
    tree.find('.//active').text = str(1)
    tree.find('.//name/language').text = cat[0].title()
    tree.find('.//link_rewrite/language').text = cat[0].lower().replace(" ", "-")
    tree.write("COPY" + FILENAME)
    create_category(ET.tostring(tree.getroot()))
