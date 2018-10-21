import sqlite3
from parsing_json import JsonResponse

class SQLString():
	
	database = "snowball.sqlite3"

	def get_connection(self):
		connection = sqlite3.connect(self.database)
		return connection

	def get_cursor(self, connection):
		cursor = connection.cursor()
		return cursor

	def get_insert_tuple(self, data):
		self.data = data

		query = self.get_search_key(data)

		insert_tuple = []

		for v in data[next(iter(data))]["related"]:
			cpc = v["cpc"]
			key = v["key"]
			competition = v["competition"]
			country_code = v["country_code"]
			search_volume = v["search_volume"]

			sql_tuple = (str(query), str(key), country_code, search_volume, cpc, competition)
			insert_tuple.append(sql_tuple)

		return insert_tuple

	def get_search_key(self, data):
		self.data = data
		self.keyword = data[next(iter(data))]["meta"]["keyword"]
		return self.keyword

	def insert_sql_string(self, data_list):
		self.sql_tuple = data_list
		sql = """INSERT INTO results(query, key, country_code, search_volume, cpc, competition) VALUES (\"%s\",\"%s\",\"%s\",%d,%f,%f)""" % self.sql_tuple
		return sql

	def insert_sql_key(self, key):
		self.key = key
		sql = """INSERT INTO keys(key) VALUES (\"%s\")""" % self.key
		return sql

	def get_rows(self, conn):
		cur = conn.cursor()
		cur.execute("SELECT * FROM results")
		data = cur.fetchall()
		for i in data:
			print(i)
		return