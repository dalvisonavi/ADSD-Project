import sqlite3

connection = sqlite3.connect("northwind.db")

cursor = connection.cursor()

cursor.execute("select ProductID, ProductName from Products")

for product in ['Chai', 'Chang', 'Aniseed Syrup']:
    cursor.execute(f"insert into productList (ProductName) values ('{product}')")

connection.commit()
connection.close()
#print("done.")