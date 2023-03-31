import os
from Repo.FolderStructure.Infographic import Infographic

class Path():

    def __init__(self, repo, path):
        self.repo = repo
        self.path = path
        self.name = os.path.basename(path)
        self.children = []

    def set_path_history(self):
        self.path_history = []
        self.reduce_level(self.path)
        self.level = len(self.path_history)
        self.set_indented_string()

    def reduce_level(self, path):
        if path != self.repo.path:
            new_path_tail, new_path_head = os.path.split(path)
            self.path_history.append(new_path_tail)
            self.reduce_level(new_path_tail)

    def set_indented_string(self):
        pre_indent = self.level * self.repo.space
        self.indented_string = f"{pre_indent}{self.name}"

    def update_indented_strings(self):
        post_indent_width = self.repo.max_name_width - len(self.indented_string)
        post_indent = post_indent_width * " " + self.repo.space
        self.indented_string = f"{self.indented_string}{post_indent}"
        for child in self.children:
            child.update_indented_strings()

    def output_statistics(self, statistic_group_name, statistics_file):
        statistics_file.writelines(f"{self.indented_string}")
        for statistic in self.statistic_groups[statistic_group_name].statistics:
            statistics_file.writelines(statistic.output_string)
        statistics_file.writelines("\n")

    def create_infographics(self):
        self.infographic = Infographic(self)
        self.infographic.create_infographic()
