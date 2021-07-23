from src.models.category import Category


def getCategoryWithName(name):
    return Category.select().where(Category.name == name).execute()