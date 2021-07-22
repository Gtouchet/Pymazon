import random

import faker
from faker import Faker

from src.controllers.cruds.productCrud.create import createProduct
from src.controllers.cruds.tagCrud.countAll import countAllTag
from src.models.product import Product
from src.models.tag import Tag


class GenerateDataProduct:
    def __init__(self):
        self.fake = Faker()

    def generateData(self, nbProduct):
        for i in range(nbProduct):
            tag = Tag.get(random.randint(1, countAllTag()))
            newProduct = Product()
            newProduct.name = tag.name + '-' + tag.category.name + '-' + self.fake.md5()
            newProduct.description = self.fake.text()
            newProduct.price = random.randint(1, 1335)
            newProduct.tag = tag.id
            newProduct.category = tag.category.id
            createProduct(newProduct)
