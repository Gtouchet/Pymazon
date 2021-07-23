from src.models.tag import Tag


def getTag(id):
    if id == 0:
        return Tag.select()
    else:
        return Tag.get_by_id(id)
        # return Tag.select().select_extend(Category).where(Tag.id == id)


