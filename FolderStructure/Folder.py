from FolderStructure.Path import Path
from Utils import get_string_list

class Folder(Path):

    def __init__(self, repo, path):
        Path.__init__(self, repo, path)
        self.set_path_history()
        self.child_folders = []
        self.files = []

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
        self.statistic_groups = {child_statistics_group.name: self.get_statistic_group_from_child_statistics_group(child_statistics_group)
                                 for child_statistics_group in self.children[0].statistic_groups.values()}

    def get_statistic_group_from_child_statistics_group(self, child_statistics_group):
        statistics_group = child_statistics_group.__class__(self)
        statistics_group.generate_for_folder(child_statistics_group.name)
        return statistics_group

    def write_to_statistics_file(self, statistic_group_name, statistics_file):
        self.output_statistics(statistic_group_name, statistics_file)
        for child in self.children:
            child.write_to_statistics_file(statistic_group_name, statistics_file)

    def __str__(self):
        string = (f"Path: {self.path}, Level: {self.level}\n"
                  f"Child Folders: {get_string_list(self.child_folder_paths)}\n"
                  f"Files: {get_string_list(self.files)}\n")
        return string
