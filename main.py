from xml.etree import ElementTree as et
filename = "product-blank-schema.xml"
tree = et.parse(filename)
tree.find('.//id').text = '1234567'
tree.write("prueba" + filename)
