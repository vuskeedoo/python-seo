"""
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
"""
import json
from restapi import Search

class JsonResponse():

	def json_response(self):
		search = Search()
		json_data = search.keywords_related('the hulk','US')
		json_data = str(json_data).replace("'","\"")
		json_data = json.loads(json_data)
		return json_data

	def pretty_print(self, json_data):
		self.json_data = json_data
		print(json.dumps(json_data, sort_keys=False, indent=2))

	def debug(self, json_data):
		return

	def sql_string(self, json_data):
		self.json_data = json_data
		for v in json_data[next(iter(json_data))]["related"]:
			print(v["key"])
			print(v["country_code"])
			print(v["search_volume"])
			print(v["cpc"])
			print(v["competition"])
		return

json_response = JsonResponse()
json_search = json_response.json_response()
json_response.pretty_print(json_search)
print("------------------")
json_response.sql_string(json_search)