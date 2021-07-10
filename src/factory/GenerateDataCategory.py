from faker import Faker

from src.controllers.cruds.categoryCrud.create import createCategory
from src.models.category import Category


class GenerateDataCategory:
    def __init__(self):
        self.nameCategory = ['Music', 'High-Tech', 'Jeux video', 'Livres', 'Sport', 'Automobile']

    def generateData(self):
        for name in self.nameCategory:
            newCategory = Category()
            newCategory.name = name
            createCategory(newCategory)