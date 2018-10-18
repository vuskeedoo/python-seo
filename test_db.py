from db_client import SQLString
from parsing_json import JsonResponse

sql = SQLString()
response = JsonResponse()

json_search = response.json_response("aquaman", "US")

print("Searched for: %s" % sql.get_search_key(json_search))

for data in json_search[next(iter(json_search))]["related"]:
	sql_insert_tuple = sql.get_insert_tuple(json_search)

for tup in sql_insert_tuple:
	insert_string = sql.insert_sql_string(tup)

connection = sql.get_connection()
print("Connected")

cursor = sql.get_cursor(connection)
print("Cursor")

cursor.execute(sql.insert_sql_key(sql.get_search_key(json_search)))
print("Keyword inserted.")

for tup in sql_insert_tuple:
	cursor.execute(sql.insert_sql_string(tup))

connection.commit()
print("Insert successful")

connection.close()
print("Closed connection")