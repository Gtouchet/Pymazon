from src.controllers.cruds.productCrud.delete import deleteProduct
from src.controllers.cruds.purchaseCrud.deletePurchaseWithProductId import deletePurchaseWithProductId
from src.models.product import Product


def deleteProductWithTagId(id):
    products = Product.select().where(Product.tag_id == id).execute()

    for product in products:
        deletePurchaseWithProductId(product.id)
        deleteProduct(product)