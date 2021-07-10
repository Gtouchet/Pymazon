from src.controllers.cruds.categoryCrud.get import getCategory
from src.controllers.cruds.tagCrud.create import createTag
from src.models.tag import Tag


class GenerateDataTag:

    def __init__(self):
        music = ['CD', 'Vinyles', 'Telechargement', 'Instruments']
        highTech = ['Téléphones', 'TV', 'Audio', 'Photo', 'GoogleHome']
        gaming = ['PS4', 'Xbox', 'Switch', '3DS', 'PC']
        livres = ['Ebooks', 'Kindle']
        sport = ['FanShop', 'Fitness', 'Cyclisme']
        automobiles = ['Piece-Auto', 'Outil-de-dépannage', 'GPS', 'Piece-Moto']
        self.listTag = [music, highTech, gaming, livres, sport, automobiles]

    def generateData(self):
        i = 0
        for tag in self.listTag:
            i = i + 1
            for name in tag:
                category = getCategory(i)
                newTag = Tag()
                newTag.name = name
                newTag.category = category
                createTag(newTag)

