#!c:/Python27/python
print "Content-type: text/html"
print
import os
import xml.etree.ElementTree as et

base_path = os.path.dirname(os.path.realpath(__file__))

#print base_path

xml_file = os.path.join(base_path, "sample.xml")

#print xml_file

tree = et.parse(xml_file)

root = tree.getroot()

# for child in root:
	# print child.tag, '<br>'
	
#for child in root:
#	print child.tag,child.attrib, '<br>'
	
for child in root:
	for element in child:
		print element.tag, ":", element.text, '<br>'