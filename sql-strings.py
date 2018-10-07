import sqlite3

class SQLstring():
	
	database = "snowball.sqlite3"
	
	def get_connection(self):
		connection = sqlite3.connect(self.database)
		return connection

	def get_cursor(self, conn):
		cursor = conn.cursor()
		return cursor

	def set_database(self, db):
		return

sql = SQLstring()

connection = sql.get_connection()
print("Got connection.")

cursor = sql.get_cursor(connection)
print("Got cursor.")

connection.close()
print("Closed connection.")