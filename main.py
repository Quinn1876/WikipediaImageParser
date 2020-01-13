import requests
import json
import pprint
from PIL import Image
from io import BytesIO
from html.parser import HTMLParser

imgURL = 0
IMG_INDEX = int(input('Enter the Number between 1 and 10: ')) - 1

class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            print(tag)
            for i in attrs:
                global imageCache
                global IMG_INDEX
                if i[0] == 'alt' and i[1] == imageCache[IMG_INDEX]:
                    for a in attrs:
                        if a[0] == 'src':
                            global imgURL
                            imgURL = a[1]
                            print(imgURL)
                            
            

    def handle_endtag(self, tag):
        return super().handle_endtag(tag)

    def handle_data(self, tag):
         return super().handle_data(tag)
            

base_site = 'https://commons.wikimedia.org/wiki/'

payload = {
    'action' : 'query',
    'prop' : 'images',
    'titles' : 'Canada',
    'imlimit' : 20,
    'format' : 'json',
    'formatversion' : 2,
    }
r = requests.get('https://en.wikipedia.org/w/api.php', params=payload) #Querys the Wikipedia API for the names of images og cats

#im = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Cat_poster_1.jpg/520px-Cat_poster_1.jpg')


dict = json.loads(r.content) # Convert Content to easily parsable Json 
imageCache = []
for i in dict['query']['pages'][0]['images']:
    if i['title'].endswith(('.jpg', '.JPG', '.jpeg')):
        imageCache.append(i['title']) # Add every jpeg file name to a list of images
        # print(i['title'])

fi = open('test.txt', 'w') # Write the names of the images to a text file
for i in imageCache:
    fi.write(i + '\n')
fi.close()

r = requests.get(base_site + imageCache[IMG_INDEX]) # Query the General Wiki page of a given image specified by the index of imageCache

rCache = r.content # gets the binary from the query(HTML)

#open("image.txt")

rCache = str(rCache)
rCache = str(rCache).lstrip("b'")
rCache.replace('\n', ' ')
#print(rCache)

parser = MyParser()

parser.feed(rCache)

print(imgURL)

if type(imgURL) == type(str('')):
    im = requests.get(imgURL)
    Image.open(BytesIO(im.content)).show()
else:
    print('false')

#i = Image.open(BytesIO(r.content))

#i.show()