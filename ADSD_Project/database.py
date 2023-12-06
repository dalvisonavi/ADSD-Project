import dataset

db = dataset.connect('sqlite:///northwind.db')

def get_products(id = None):
    productList_table = db['products']
    if id == None:
        rows = list_table.find()
    else:
        rows = productList_table.find(ProductID=ProductID)
    rows = [dict(row) for row in rows]
    return rows    
    