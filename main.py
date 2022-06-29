from xml.etree import ElementTree as et
filename = "category-blank-schema.xml"
tree = et.parse(filename)
tree.find('.//id').text = '1/1/2011'
tree.write("copy" + filename)
