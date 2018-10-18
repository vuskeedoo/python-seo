import json
from restapi import Search

class JsonResponse():

	def json_response(self, key, cty):
		search = Search()
		json_data = search.keywords_related(key,cty)
		json_data = str(json_data).replace("'","\"")
		json_data = json.loads(json_data)
		return json_data

	def pretty_print(self, json_data):
		self.json_data = json_data
		print(json.dumps(json_data, sort_keys=False, indent=2))
		return

	def output_kwrd(self, json_data):
		self.json_data = json_data
		print("Searched for: \"%s\"" % json_data[next(iter(json_data))]["meta"]["keyword"])
		for v in json_data[next(iter(json_data))]["related"]:
			print(v["key"])
			print(v["country_code"])
			print(v["search_volume"])
			print(v["cpc"])
			print(v["competition"])
		return

# To test response
"""
json_response = JsonResponse()
json_search = json_response.json_response("spiderman", "CA")
json_response.pretty_print(json_search)
json_response.output_kwrd(json_search)
"""