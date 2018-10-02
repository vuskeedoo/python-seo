import json
from restapi import Search

'''
response = Search()

# these three lines create an API call
data = response.keywords_related('superman','US')
data = str(data).replace("'","\"")
data = json.loads(data)
'''

# this line uses a file so that we do not use credits while debugging, etc.
data = json.loads(open('superman.json').read())

for v in data[next(iter(data))]["related"]:
	print(v["key"])
	print(v["country_code"])