###import the necessary packages####

import requests
from bs4 import BeautifulSoup
#import this package if you have encoding errors
#import sys
#sys.setdefaultencoding('utf8')


### extract the HTML into text 

r = requests.get('https://www.imdb.com/title/tt0071853/')

r_unparsed = r.text

### now make some Soup using Beautiful Soup and XML parser
b = BeautifulSoup(r_unparsed,'lxml')


### extract the title and save it into a variable

### if there was more than 1 title

### extract the description and save it into a variable


### extract the Rating eg: R and save into a variable


### create a function that extracts this information of any IMDB movie of your choosing
### ^ into the form of a dictionary 
