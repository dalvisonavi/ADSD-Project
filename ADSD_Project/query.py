import sqlite3

connection = sqlite3.connect("northwind.db")

cursor = connection.cursor()

rows = cursor.execute("Select ProductID, ProductName from products")
rows = list(rows)

print(rows)

rows = [ {'ProductID' : row[0], 'ProductName' : row[1]} for row in rows ]

print(rows)