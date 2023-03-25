import os

from FolderStructure.Path import Path
from Statistics.LineCount import LineCount

class File(Path):

    def __init__(self, repo, parent_path, file_name):
        path = os.path.join(parent_path, file_name)
        Path.__init__(self, repo, path)
        self.parent_path = parent_path
        self.file_name = file_name
        self.set_path_history()

    def create_summary_statistics(self):
        self.set_file_contents()
        self.set_statistic_group_classes()
        self.generate_statistics()

    def set_file_contents(self):
        with open(self.path, "r") as file:
            self.file_contents = [line.strip("\n") for line in file]

    def set_statistic_group_classes(self):
        self.statistic_group_classes = [LineCount]

    def generate_statistics(self):
        self.statistic_groups = {group_class.name: self.generate_statistic_group(group_class)
                                 for group_class in self.statistic_group_classes}

    def generate_statistic_group(self, group_class):
        statistic_group = group_class(self)
        statistic_group.generate_from_file()
        return statistic_group

    def write_to_statistics_file(self, statistics_file):
        statistics_file.writelines(f"{self.indented_string}\n")

    def __str__(self):
        string = f"Path: {self.path}, Level: {self.level}"
        return string
