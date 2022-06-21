import xml.etree.ElementTree as ET
from check_child_from_file import check_child_from_file

# Parsing the xml file from the directory
def parse(extract,file):
    tree = ET.parse(f'{extract}{file[0]}')
    root = tree.getroot()
    check_tag(root)

# Locate the root name from xml file                                           
def check_tag(root):
    Tag = root.tag
    #checks the tag ending with the keyword
    if Tag.endswith('diagramExchange'):
        print("\nTag :",Tag,"\n")
        check_child_from_file(root)
    else:
        raise ValueError('Incompatible Tag found:',Tag)
 