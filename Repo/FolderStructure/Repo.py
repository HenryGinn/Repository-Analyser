import os
import sys

from FolderStructure.Folder import Folder
from FolderStructure.File import File

class Repo():

    space = "  "

    def __init__(self, path):
        self.path = path
        self.repo_name = os.path.basename(path)
        self.set_files_and_folders()

    def set_files_and_folders(self):
        self.set_files()
        self.set_folders()
        self.set_path_structure()
        self.set_max_name_width()
        self.base_folder.update_indented_strings()
        
    def set_files(self):
        self.files = []
        for directory, sub_directories, files in os.walk(self.path, topdown=False):
            self.files += [File(self, directory, file) for file in files
                           if self.check_if_python(file)]
    
    def check_if_python(self, path):
        return path.endswith(".py")

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
        parent_folder.children.append(folder)

    def set_child_folder_paths(self):
        for folder in self.folders:
            folder.child_folder_paths = [child_folder.path
                                         for child_folder in folder.child_folders]

    def set_folder_files(self):
        for file in self.files:
            parent_folder = self.path_folder_lookup[file.parent_path]
            parent_folder.files.append(file)
            parent_folder.children.append(file)

    def set_max_name_width(self):
        file_name_widths = [len(file.indented_string) for file in self.files]
        folder_name_widths = [len(folder.indented_string) for folder in self.folders]
        self.max_name_width = max(max(file_name_widths), max(folder_name_widths))

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
        self.base_folder.create_summary_statistics()
        self.create_statistics_files()

    def create_statistics_files(self):
        for statistic_group_name in self.base_folder.statistic_groups:
            statistic_group_path = os.path.join(self.repo_results_path,
                                                f"{statistic_group_name} Statistics.txt")
            self.write_to_statistics_file(statistic_group_name, statistic_group_path)

    def write_to_statistics_file(self, statistic_group_name, statistic_group_path):
        with open(statistic_group_path, "w") as statistics_file:
            self.write_statistics_file_headers(statistic_group_name, statistics_file)
            self.base_folder.write_to_statistics_file(statistic_group_name, statistics_file)

    def write_statistics_file_headers(self, statistic_group_name, statistics_file):
        self.write_directory_column_header(statistics_file)
        self.write_statistic_column_header(statistic_group_name, statistics_file)

    def write_directory_column_header(self, statistics_file):
        directory_column_header = "Directory Name"
        directory_column_indent = (self.max_name_width - len(directory_column_header)) * " "
        statistics_file.writelines(f"{directory_column_header}{directory_column_indent}{self.space}")

    def write_statistic_column_header(self, statistic_group_name, statistics_file):
        for statistic in self.base_folder.statistic_groups[statistic_group_name].statistics:
            column_width = max(len(statistic.name) + 1, statistic.min_column_width)
            indent = (column_width - len(statistic.name)) * " "
            statistics_file.writelines(f"{indent}{statistic.name}")
        statistics_file.writelines("\n")
        
    def output_files(self):
        print("\nOutputting files")
        for file in self.files:
            print(file)

    def output_folders(self):
        print("\nOutputting folders")
        for folder in self.folders:
            print(folder)
