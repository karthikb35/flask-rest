import sqlite3
# from User import User
#
#
# a=[{'ac' : 1}, {'ac' : 2},{'3' : 1},{'4' : 1}]
# for aw in a :
#     if aw.get('ac') == 2:
#         a.remove(aw)
# a={'ac' : 1}
# a.update({'ax' : 2})
# print(a)
#
# b=[1,2,3,4]
# for e in b:
#     if e==2:
#         b.remove(e)
# print(b)

#
connection = sqlite3.connect('data.db')
cursor = connection.cursor()


#
create_cmd = "CREATE TABLE  if not exists items (id INTEGER PRIMARY KEY, name text, price float)"
cursor.execute(create_cmd)
connection.commit()
create_cmd = "CREATE TABLE  if not exists users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_cmd)
connection.commit()

connection.close()
#
# insert_query = "INSERT INTO users values (?, ?, ? )"
# user = (1, 'ka', 'br')
# cursor.execute(insert_query, user)
# users = [
#     (2, 'kq', 'bra'),
#     (3, 'kad', 'bcr')
# ]
# cursor.executemany(insert_query, users)
# connection.commit()
# for row in cursor.execute('select * from users'):
#     print(row)
# connection.close()
#
# u = User.get_by_id(4)
# if u:
#     print(u.username,u.password)