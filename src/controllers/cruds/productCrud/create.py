from src.services.logger import Logger


def createProduct(product):
    Logger("CreateProduct", {
        "subject": "Create of " + product.name,
    })
    product.save()