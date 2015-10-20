from lxml import html
from lxml import etree
import requests


def Death_March_Parser(vol_no, url):
    
    volume_no = vol_no
    volume = open('Death March - Volume ' + str(volume_no) + '.txt', 'w+')

    volume.write("Death March - Volume " + str(volume_no))
    volume.write('\n')
    volume.write('\n')

    page = requests.get(url)

    tree = html.fromstring(page.text)
    content = tree.find_class("post-body entry-content")

    page_content = content[0].getchildren()

    for line in page_content:
        if line.tail != None:
            volume.write(line.tail.encode('utf-8'))

    volume.close()



