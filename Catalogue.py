import os
import sys

from CatalogueFolder import CatalogueFolder
from Repo.FolderStructure.Repo import Repo

class Catalogue():

    def __init__(self, path):
        self.path = path
        self.set_parent_results_path()
        self.repositories = []
        self.initialise_folders()
        self.identify_repositories(path)
        self.remove_folders_without_repositories(self.folders[self.path])

    def set_parent_results_path(self):
        script_path = sys.path[0]
        parent_path = os.path.dirname(script_path)
        self.parent_results_path = os.path.join(parent_path, "Results")
        self.create_parent_results_folder()

    def create_parent_results_folder(self):
        if not os.path.exists(self.parent_results_path):
            print(f"Creating 'Results' folder at {self.parent_results_path}")
            os.mkdir(self.parent_results_path)

    def initialise_folders(self):
        folder = CatalogueFolder(self, self.path)
        self.folders = {self.path: folder}
    
    def identify_repositories(self, path):
        for directory_name in os.listdir(path):
            directory_path = os.path.join(path, directory_name)
            self.process_directory_path(directory_path)

    def process_directory_path(self, directory_path):
        if os.path.isdir(directory_path):
            self.add_to_folder_list(directory_path)
            file_names = [file_name for file_name in os.listdir(directory_path)
                          if os.path.isfile(os.path.join(directory_path, file_name))]
            self.process_directory_path_folder(directory_path, file_names)

    def add_to_folder_list(self, directory_path):
        folder = CatalogueFolder(self, directory_path)
        folder.set_parent_folder()
        self.folders[directory_path] = folder

    def process_directory_path_folder(self, directory_path, file_names):
        if len(file_names) != 0:
            self.add_repository(directory_path)
        if "README.md" not in file_names:
            self.identify_repositories(directory_path)

    def add_repository(self, directory_path):
        repository = Repo(directory_path)
        if len(repository.folders) > 0:
            self.process_new_repository(repository)

    def process_new_repository(self, repository):
        repository.setup_repository()
        self.repositories.append(repository)
        folder = self.folders[repository.path]
        folder.add_repository(repository)

    def remove_folders_without_repositories(self, folder):
        for folder in self.folders.values():
            if not folder.contains_repositories:
                folder.parent_folder.children.remove(folder)

    def output_all_folders(self):
        base_folder = self.folders[self.path]
        self.output_folders(base_folder)

    def output_folders(self, folder):
        print(folder)
        for child_folder in folder.children:
            self.output_folders(child_folder)
