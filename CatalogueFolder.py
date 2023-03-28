class CatalogueFolder():

    def __init__(self, catalogue, path):
        self.catalogue = catalogue
        self.path = path
        self.children = []
        self.repositories = []
