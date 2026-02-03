from fastapi import FastAPI
from models import Products
app = FastAPI()

@app.get("/")
def greet():
    return {"name":"Hassan Waheed Ali"}

products = [
    Products(id = 1, name = "Logitech Mouse",  description ="Gaming Mouse",  price =499.99, quantity= 50),
    Products(id = 4, name = "Hitech Kyeboard", description = "Gaming Keyboard",  price =699.99, quantity= 10),
    Products(id = 3, name = "View Sonic LCD", description = "Amuled display 120Hz",  price =800.00, quantity= 50)
]
@app.get("/products")
def fetch_products():
    return products

@app.get("/products/{id}")
def fetch_by_id(id:int):
    for product in products:
        if id == product.id:
            return product
    return "Warning : Product not found please check data base"

@app.post("/product")
def add_product(product:Products):
    products.append(product)
    return {"product":product,"Message":"Product has been added" }




