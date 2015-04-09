
# built-ins
import pprint
import random

# site-packages
from wikitools import wiki
from wikitools import api
import pattern.en


site = wiki.Wiki("http://wikihow.com/api.php") 


params = {'action':'query', 'list':'random', 'rnlimit':'10', 'rnnamespace': '0'}
# params = {'action':'query', 'list':'allcategories'}

intros = [
    ("having trouble", True),
    ("need to", False),
    ("want to", False),
    ("looking to", False),
]

request = api.APIRequest(site, params)
result = request.query()

titles = map(lambda x: x['title'], result['query']['random'])

title = random.choice(titles).lower()

introData = random.choice(intros)
if (introData[1]):
    parsedTitle = title.split(' ')
    parsedTitle[0] = pattern.en.conjugate(parsedTitle[0], tense=pattern.en.PARTICIPLE, parse=True)
    title = ' '.join(parsedTitle)

quandary = "%s %s?" % (introData[0], title)
quandary = quandary.capitalize()
print quandary
