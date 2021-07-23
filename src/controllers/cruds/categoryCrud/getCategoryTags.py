from src.models.tag import Tag


def getCategoryTags(category):
    return Tag.select().where(Tag.category == category).execute()