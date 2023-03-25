from FolderStructure.Path import Path
from Utils import get_string_list

class Folder(Path):

    def __init__(self, repo, path):
        Path.__init__(self, repo, path)
        self.set_path_history()
        self.child_folders = []
        self.files = []
        self.children = []

    def create_summary_statistics(self):
        self.set_sub_folder_summary_statistics()
        self.set_file_summary_statistics()
        self.set_folder_summary_statistics()

    def set_sub_folder_summary_statistics(self):
        for folder in self.child_folders:
            folder.create_summary_statistics()

    def set_file_summary_statistics(self):
        for file in self.files:
            file.create_summary_statistics()

    def set_folder_summary_statistics(self):
        self.statistic_groups = []
        self.set_folder_summary_statistics_from_files()
        self.set_folder_summary_statistics_from_child_folders()

    def set_folder_summary_statistics_from_files(self):
        if len(self.files) > 0:
            self.statistic_groups += [self.get_statistic_group_file_obj(statistics_group_file)
                                      for statistics_group_file in self.files[0].statistic_groups.values()]

    def get_statistic_group_from_files(self, statistics_group_file):
        self.statistics_group = statistics_group_file.__class__(self)
        self.statistics_group.generate_from_folder(statistics_group_file.name)

    def set_folder_summary_statistics_from_child_folders(self):
        if len(self.child_folders) > 0:
            self.statistic_groups += [self.get_statistic_group_folder_obj(statistics_group_child_folder)
                                      for statistics_group_file in self.child_folders[0].statistic_groups.values()]

    def get_statistic_group_folder_obj(self, statistics_group_child_folder):
        pass

    def write_to_statistics_file(self, statistics_file):
        statistics_file.writelines(f"{self.indented_string}\n")
        self.write_to_statistics_file_files(statistics_file)
        self.write_to_statistics_file_child_folders(statistics_file)

    def write_to_statistics_file_files(self, statistics_file):
        for file in self.files:
            file.write_to_statistics_file(statistics_file)

    def write_to_statistics_file_child_folders(self, statistics_file):
        for folder in self.child_folders:
            folder.write_to_statistics_file(statistics_file)

    def __str__(self):
        string = (f"Path: {self.path}, Level: {self.level}\n"
                  f"Child Folders: {get_string_list(self.child_folder_paths)}\n"
                  f"Files: {get_string_list(self.files)}\n")
        return string
