from pydantic import BaseModel


class ProductsCreate(BaseModel):
    name: str
    description: str
    price: float
    quantity: int


class Products(ProductsCreate):
    id: int
