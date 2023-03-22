import os
import sys

from Folder import Folder
from File import File

class Repo():

    space = "  "

    def __init__(self, path):
        self.path = path
        self.repo_name = os.path.basename(path)
        self.set_files_and_folders()
        self.create_results_folders()

    def set_files_and_folders(self):
        self.set_files()
        self.set_folders()
        self.set_path_structure()
        
    def set_files(self):
        self.files = []
        for directory, sub_directories, files in os.walk(self.path, topdown=False):
            self.files += [File(self, directory, file) for file in files
                           if self.check_if_python(file)]
    
    def check_if_python(self, path):
        return (path.endswith(".py"))

    def set_folders(self):
        self.set_paths_containing_python()
        self.folders = [Folder(self, path) for path in self.paths_containing_python]
        self.path_folder_lookup = {folder.path: folder for folder in self.folders}

    def set_paths_containing_python(self):
        self.paths_containing_python = []
        for file in self.files:
            self.paths_containing_python += file.path_history
        self.paths_containing_python = list(set(self.paths_containing_python))

    def set_path_structure(self):
        self.set_folder_structure()
        self.set_child_folder_paths()
        self.set_folder_files()

    def set_folder_structure(self):
        for folder in self.folders:
            if folder.level != 0:
                self.find_folder_parent(folder)
            else:
                self.base_folder = folder

    def find_folder_parent(self, folder):
        parent_path = folder.path_history[0]
        parent_folder = self.path_folder_lookup[parent_path]
        parent_folder.child_folders.append(folder)

    def set_child_folder_paths(self):
        for folder in self.folders:
            folder.child_folder_paths = [child_folder.path
                                         for child_folder in folder.child_folders]

    def set_folder_files(self):
        for file in self.files:
            parent_folder = self.path_folder_lookup[file.parent_path]
            parent_folder.files.append(file)

    def create_results_folders(self):
        self.set_parent_results_path()
        self.set_repo_results_path()

    def set_parent_results_path(self):
        script_path = sys.path[0]
        parent_path = os.path.dirname(script_path)
        self.parent_results_path = os.path.join(parent_path, "Results")
        self.create_parent_results_folder()

    def create_parent_results_folder(self):
        if not os.path.exists(self.parent_results_path):
            print(f"Creating 'Results' folder at {self.parent_results_path}")
            os.mkdir(self.parent_results_path)

    def set_repo_results_path(self):
        self.repo_results_path = os.path.join(self.parent_results_path,
                                              f"{self.repo_name} Results")
        self.create_repo_results_folder()

    def create_repo_results_folder(self):
        if not os.path.exists(self.repo_results_path):
            print(f"Creating '{self.repo_name} Results' folder at {self.repo_results_path}")
            os.mkdir(self.repo_results_path)
        
    def create_statistics(self):
        self.set_max_name_width()
        self.base_folder.create_summary_statistics()
        self.create_statistics_file()

    def set_max_name_width(self):
        file_name_widths = [len(file.indented_string) for file in self.files]
        folder_name_widths = [len(folder.indented_string) for folder in self.folders]
        self.max_name_width = max(max(file_name_widths), max(folder_name_widths))

    def create_statistics_file(self):
        self.statistics_summary_path = os.path.join(self.repo_results_path,
                                                    "Repo Statistics.txt")
        with open(self.statistics_summary_path, "w") as statistics_file:
            self.base_folder.write_to_statistics_file(statistics_file)
        
    def output_files(self):
        print("\nOutputting files")
        for file in self.files:
            print(file)

    def output_folders(self):
        print("\nOutputting folders")
        for folder in self.folders:
            print(folder)
