import os

class CatalogueFolder():

    def __init__(self, catalogue, path):
        self.catalogue = catalogue
        self.path = path
        self.name = os.path.basename(path)
        self.children = []
        self.repositories = []
        self.contains_repositories = False

    def set_parent_folder(self):
        parent_path = os.path.dirname(self.path)
        self.parent_folder = self.catalogue.folders[parent_path]
        self.parent_folder.children.append(self)

    def add_repository(self, repository):
        self.repositories.append(repository)
        self.contains_repositories = True
        self.set_parent_folder_contains_repositories()

    def set_parent_folder_contains_repositories(self):
        self.parent_folder.contains_repositories = True
        if self.parent_folder.path != self.catalogue.path:
            self.parent_folder.set_parent_folder_contains_repositories()

    def __str__(self):
        string = (f"Path: {self.path}, Contains Repos: {self.contains_repositories}")
        return string
