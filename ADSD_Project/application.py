from bottle import route, post, run, template, redirect, request
import database

route("/")
def get_index():
    redirect("/products")
    
route("/products")
def get_productList():
    product = database.get_products()
    return template ("product.tpl", product_list = product)

run(host = 'localhost', port = 8080)