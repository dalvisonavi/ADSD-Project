import sqlite3

connection = sqlite3.connect("inventory.db")

cursor = connection.cursor()

rows = cursor.execute("select * from item")
rows = list(rows)

print(rows)

rows = [ {'id':row[0], 'description':row[1],  'orderNumber':row[0], 'quantity':row[1], 'cakeType':row[2]} for row in rows ]

print(rows)
