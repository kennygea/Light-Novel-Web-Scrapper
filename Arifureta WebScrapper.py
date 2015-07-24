from lxml import html
import requests

volume_no = 8 #change volume number here!

volume = open('Arifureta - Volume ' + str(volume_no) + '.txt', 'w+')

volume.write("Arifureta - Volume " + str(volume_no))
volume.write('\n')
volume.write('\n')

number_of_chapters = 10 ##Change Number of Chapters to Parse here!

for i in xrange(1, number_of_chapters+1):

    volume.write("Chapter " + str(i))
    volume.write('\n')
    volume.write('\n')
    
    url = 'http://japtem.com/arifureta-volume-' +str(volume_no) + '-chapter-' + str(i) +'/'

    page = requests.get(url)

    tree = html.fromstring(page.text)
    content = tree.find_class("post-content")

    page_content = content[0].getchildren()

    for line in page_content:
        if line.text != None:
            volume.write(line.text.encode('utf8'))
            volume.write('\n')
            volume.write('\n')

volume.close()

