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

	def output_kwrd(self, json_data):
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
json_response.output_kwrd(json_search)