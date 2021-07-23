from src.models.tag import Tag


def getTagWithName(name):
    return Tag.select().where(Tag.name == name).execute()