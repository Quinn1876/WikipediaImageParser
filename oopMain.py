# Created By Quinn Hodges

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
	
	img_index = 0
	cache = []
	img_url = ''
	base_site = 'https://commons.wikimedia.org/wiki/'
	
	@classmethod
	def setTitle(cls, i):
		ui = input('What image would you like? ')
		cls.query['titles'] = ui
		return
	
	@classmethod
	def setNumber(cls):
		ui = ''
		while type(ui) != type(0):
			ui = input("Enter a number between 1 and 10: ")
			try:
				ui = int(ui)
				if int(ui) - 1  in range (10):
					cls.img_index = ui
				else:
					ui = ''
					print('Error: Not in Range')
			except ValueError:
				print("Error: Not a number")
			
		return
	
	# Direct name input for Access from a non-consol UI
	@classmethod
	def setImageName(cls, name): 
		cls.query['titles'] = name
	
	@classmethod
	def setImageNumber(cls, number):
		cls.img_index = number
	
	@classmethod	
	def runFullQuery(cls):
		getImageList()
		openImage(getImage())
		
			
	@classmethod
	def getImageList(cls):
		del cls.cache
		cls.cache = []
		r = requests.get('https://en.wikipedia.org/w/api.php', params=cls.query) # Query the main wiki API for a list of images
		dict = json.loads(r.content) # Convert the responce to easily parsable Json
		for i in dict['query']['pages'][0]['images']:
			if i['title'].endswith(('.jpg', '.JPG', '.jpeg')):
				cls.cache.append(str(i['title'])) # Add every jpeg file name to a list of images
				
		return cls.cache
	
	@classmethod
	def getImage(cls):
		try:
			r = requests.get(cls.base_site + cls.cache[cls.img_index]) # Query the General Wiki page of a given image specified by the index of imageCache
			bCache = r.content # Caches the binary from the GET request
			bCache = str(bCache).lstrip("b'")
		
			parser = MyParser()
			parser.feed(bCache)
			im = requests.get(cls.img_url) # Querys the url of the Image
			return Image.open(BytesIO(im.content))
		except IndexError:
			print("Image not found")
			
	@classmethod
	def openImage(cls, img):
		img.show() # Converts the binary to an image and opens it
		
		
class MyParser(HTMLParser):
	# Searches for an image tag that has the same name as the desired Image
	def handle_starttag(self, tag, attrs):
		if tag == 'img':
			for i in attrs:
				if i[0] == 'alt' and i[1] == IMG_SCRUBBER.cache[IMG_SCRUBBER.img_index]:
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
	IMG_SCRUBBER.runFullQuery()
	
	