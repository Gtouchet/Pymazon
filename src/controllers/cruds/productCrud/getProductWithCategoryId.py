from src.models.product import Product


def getProductWithCategoryId(id):
    return Product.select().where(Product.tag.category_id == id).execute()