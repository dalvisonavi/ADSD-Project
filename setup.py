import sqlite3

connection = sqlite3.connect("inventory.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table item")
except:
    pass

cursor.execute("create table item(id integer primary key, description text)")

for item in ['Dutch Pastry', 'StrawBerry Shortcake', 'Blueberry Cheesecake', 'Pound Cake', 'Banana Bread']:
    cursor.execute(f"insert into item (description) values ('{item}')")

# cursor.execute("create table if not exists details(orderNumber integer, quantity num, cakeType text, foreign key (cakeType) references item(description))")

# for details in ['1', '4', 'StrawBerry Shortcake']:
#     cursor.execute(f"insert into details (orderNumber, quantity, cakeType) values ('{details}','{details}','{details}')")

connection.commit()
connection.close()
