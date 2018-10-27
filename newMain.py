import requests
import json
import pprint
from PIL import Image
from io import BytesIO
from html.parser import HTMLParser

class IMG_SCRUBBER():
	query = {
		'action' : 'query',
		'prop' : 'images',
		'titles' : 'title',
		'imlimit' : 10,
		'format' : 'json',
		'formatversion' : 2,
	}
	
	index = 0
	cache = []
	img_url = ''
	base_sight = 'https://commons.wikimedia.org/wiki/'
	
	@classmethod
	def setTitle(cls):
		ui = input('What image would you like?')
		cls.query{'titles'} = ui
		return
	
	@classmethod
	def setNumber(cls):
		ui = ''
		while type(ui) != type(0):
			ui = input("Enter a number between 1 and 10")
			if type(ui) != type(0):
				print("Error: Not a number")
			else if int(ui) - 1  in range (10):
				cls.img_index = ui
			else:
				ui = ''
				print('Error: Not in Range')
		return
	
	@classmethod	
	def runQuery(cls):
		r = requests.get('https://en.wikipedia.org/w/api.php', params=cls.query) # Query the main wiki API for a list of images
		dict = json.loads(r.content) # Convert the responce to easily parsable Json
		for i in dict['query']['pages'][0]['images']:
			if i['title'].endswith(('.jpg', '.JPG', '.jpeg')):
				cls.cache.append(i['title']) # Add every jpeg file name to a list of images
		
		r = requests.get(base_site + cls.cache[cls.index]) # Query the General Wiki page of a given image specified by the index of imageCache
		bCache = r.content # Caches the binary from the GET request
		bCache = str(bCache).lstrip("b'")
		
		parser = MyParser()
		parser.feed(bCache)
		im = requests.get(cla.url) # Querys the url of the Image
		Image.open(BytesIO(im.content)).show() # Converts the binary to an image and opens it
		
class MyParser(HMTMLParser):
	# Searches for an image tag that has the same name as the desired Image
	def handle_starttag(self, tag, attrs):
		if tag == 'img':
            print(tag)
            for i in attrs:
                if i[0] == 'alt' and i[1] == IMG_SCRUBBER.cache[IMG_SCRUBBER.index]:
                    for a in attrs:
                        if a[0] == 'src':
                            IMG_SCRUBBER.img_url = a[1]
                            
                            
            

    def handle_endtag(self, tag):
        return super().handle_endtag(tag)

    def handle_data(self, tag):
         return super().handle_data(tag)
		
	


if __name__ == '__main__':
	IMG_SCRUBBER.setTitle()
	IMG_SCRUBBER.setNumber()
	
	