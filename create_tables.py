import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table="CREATE TABLE users value( id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)
connection.commit()
connection.close()