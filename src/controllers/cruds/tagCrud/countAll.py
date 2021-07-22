from src.models.tag import Tag


def countAllTag():
    return Tag.select().count()
