from fastapi import FastAPI
from models import Products, ProductsCreate
from database import get_db_connection

app = FastAPI()

# Database connection
conn = get_db_connection()
cursor = conn.cursor()


@app.get("/")
def greet():
    return {"name": "Hassan Waheed Ali"}


products = []


@app.get("/products")
def fetch_products():
    try:
        query = "SELECT * FROM products"
        cursor.execute(query)
        products = cursor.fetchall()
        return products
    except Exception as e:
        conn.rollback()
        return {"message": "Failed to fetch products from database,", "error": str(e)}


@app.get("/products/{id}")
def fetch_by_id(id: int):
    try:
        query = "SELECT * FROM products WHERE id = %s"
        cursor.execute(query, (id,))
        product = cursor.fetchone()
        if product:
            return product
        return {"message": "Product not found", "id": id}
    except Exception as e:
        conn.rollback()
        return {"error": str(e)}


@app.post("/product")
def add_product(product: ProductsCreate):
    try:
        query = "INSERT INTO products (name, description,price,quantity) VALUES (%s,%s,%s,%s) RETURNING id"
        cursor.execute(
            query, (product.name, product.description, product.price, product.quantity)
        )
        product_id = cursor.fetchone()
        conn.commit()
        return {
            "product": product,
            "id": product_id,
            "Message": "Product has been added",
        }
    except Exception as e:
        conn.rollback()
        return {"error": str(e)}


@app.put("/product")
def update_product_data(product: Products):
    try:
        query = "UPDATE products SET name=%s, description=%s, price=%s, quantity=%s WHERE id=%s"
        cursor.execute(
            query,
            (
                product.name,
                product.description,
                product.price,
                product.quantity,
                product.id,
            ),
        )
        conn.commit()
        return {"Message": "Product has been updated!!!"}
    except Exception as e:
        conn.rollback()
        return {"error": str(e)}


@app.delete("/product/")
def delete_product(id: int):
    try:
        query = "DELETE FROM products WHERE id=%s"
        cursor.execute(query, (id,))
        if cursor.rowcount == 0:
            return {"message": "Product Not Found"}
        conn.commit()
        return {"message": "Product has been deleted"}
    except Exception as e:
        conn.rollback()
        return {"error": str(e)}
