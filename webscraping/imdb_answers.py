###import the necessary packages####

import requests
from bs4 import BeautifulSoup
import json
#import this package if you have encoding errors
# import sys
# sys.setdefaultencoding('utf8')


### extract the HTML into text 

r = requests.get('https://www.imdb.com/title/tt0071853/')

r_unparsed = r.text

### now make some Soup using Beautiful Soup and XML parser
b = BeautifulSoup(r_unparsed,'lxml')


### extract the title and save it into a variable
title = b.title.text
print(title)

### if there was more than 1 title it would have to be

title = b.find_all('title')
print(title)

### extract the description and save it into a variable

desc = b.find('div','summary_text').text.strip()
print(desc)

### extract the Rating eg: R and save into a variable

# rating = b.find('script',type='application/ld+json').text.strip()
# print(rating)	



rating = json.loads(b.find('script', type='application/ld+json').text)['contentRating']


## create a function that extracts this information of any IMDB movie of your choosing
## ^ into the form of a dictionary 

def movie_info(id):
	r = requests.get('https://www.imdb.com/title/{0}/'.format(id))
	b = BeautifulSoup(r.text,'lxml')
	movie_dict = {}
	movie_dict[id] = {}
	movie_dict[id]['title'] = b.title.text
	movie_dict[id]['desc'] = b.find('div','summary_text').text.strip()
	movie_dict[id]['rating'] = json.loads(b.find('script', type='application/ld+json').text)['contentRating']
	return movie_dict

Adrift = movie_info('tt6306064')
print(Adrift)
