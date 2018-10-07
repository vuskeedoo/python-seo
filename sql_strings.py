import sqlite3
from parsing_json import JsonResponse

class SQLstring():
	
	database = "snowball.sqlite3"
	
	def get_connection(self):
		connection = sqlite3.connect(self.database)
		return connection

	def get_cursor(self, conn):
		cursor = conn.cursor()
		return cursor

	def get_insert_tuple(self, json_data):
		self.json_data = json_data
		self.key_id = 0
		insert_list = []
		for value in json_data[next(iter(json_data))]["related"]:
			key = value["key"]
			country_code = value["country_code"]
			search_volume = value["search_volume"]
			cpc = value["cpc"]
			competition = value["competition"]
			sql_tuple = (key, country_code, search_volume, cpc, competition)
			insert_list.append(sql_tuple)
		return insert_list

	def insert_sql(self, json_list):
		self.sql_tuple = json_list
		sql = """INSERT INTO results(key, country_code, search_volume, cpc, competition) VALUES (%s,%s,%d,%f,%f) """ % self.sql_tuple
		print(sql)
		return

	def print_sql(self, t):
		for v in t:
			print(type(v))
		return

sql = SQLstring()
json_response = JsonResponse()

json_data = json_response.json_response()

for j in json_data[next(iter(json_data))]["related"]:
	sql_tuple = sql.get_insert_tuple(json_data)

print(sql_tuple)

for i in sql_tuple:
	sql.insert_sql(i)

connection = sql.get_connection()
print("Got connection.")

cursor = sql.get_cursor(connection)
print("Got cursor.")

connection.close()
print("Closed connection.")