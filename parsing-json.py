from pprint import pprint
import json

with open('seo.json') as seo_data:
    data = json.load(seo_data)

pprint(data)

print(type(data))
