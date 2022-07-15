import sqlite3


# def connect():
#     conn = sqlite3.connect("name.db")
#     cur = conn.cursor()
#     cur.execute(
#         "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,name text,R INTEGER,G INTEGER, B INTEGER,min  FLOAT ,max FLOAT )")
#     conn.commit()
#     conn.close()
#
#
# def insert(name,R,G,B,min,max):
#     conn = sqlite3.connect("name.db")
#     cur = conn.cursor()
#     cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?,?,?)", (name,R,G,B,min,max))
#     conn.commit()
#     conn.close()
# def view():
#     conn = sqlite3.connect("name.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM book")
#     rows = cur.fetchall()
#     conn.close()
#     return rows
# def update(id, name,R,G,B,min,max):
#     conn = sqlite3.connect("name.db")
#     cur = conn.cursor()
#     cur.execute("UPDATE book SET name=?,R=?,G=?,B=?,min=?,max=? WHERE id=?", (name,R,G,B,min,max, id))
#     conn.commit()
#     conn.close()
#
# connect()
# insert(name='Sensor 01',R=255,G=0,B=0,min=1,max=4)
# insert(name='Sensor 02',R=0,G=170,B=255,min=1,max=4)
# insert(name='Sensor 03',R=255,G=255,B=0,min=1,max=4)
# insert(name='Sensor 04',R=0,G=255,B=0,min=1,max=4)
# insert(name='Sensor 05',R=85,G=0,B=255,min=1,max=4)
# insert(name='Sensor 06',R=255,G=170,B=0,min=1,max=4)
# insert(name='Sensor 07',R=200,G=66,B=100,min=1,max=4)
# insert(name='Sensor 08',R=176,G=176,B=87,min=1,max=4)
# insert(name='Sensor 09',R=0,G=170,B=0,min=1,max=4)
# insert(name='Sensor 10',R=129,G=129,B=129,min=1,max=4)
# insert(name='Sensor 11',R=108,G=255,B=231,min=1,max=4)
# insert(name='Sensor 12',R=150,G=150,B=0,min=1,max=4)
# insert(name='Sensor 13',R=170,G=0,B=255,min=1,max=4)
# insert(name='Sensor 14',R=209,G=103,B=200,min=1,max=4)
# insert(name='Sensor 15',R=255,G=206,B=172,min=1,max=4)
# insert(name='Sensor 16',R=255,G=255,B=210,min=1,max=4)
# # update(1, '')