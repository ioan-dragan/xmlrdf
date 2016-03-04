import json
with open('example.json') as data_file:
    content = json.loads(data_file.read())

from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring


def dict_to_xml(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        print val
        elem.append(child)
    return elem

for i in range(len(content['maps'])):
    #e = dict_to_xml('maps',content[i][0])
    print content['maps'][i]
    print tostring(dict_to_xml('id', content['maps'][i]))
    # print e
    #print tostring(e)
    