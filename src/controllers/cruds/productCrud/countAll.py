from src.models.product import Product


def countAllProduct():
    return Product.select().count()