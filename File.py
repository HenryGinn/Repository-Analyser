import os

from Path import Path

class File(Path):

    def __init__(self, repo, parent_path, file_name):
        path = os.path.join(parent_path, file_name)
        Path.__init__(self, repo, path)
        self.parent_path = parent_path
        self.file_name = file_name
        self.set_path_history()

    def create_summary_statistics(self):
        self.set_file_contents()
        self.set_line_count_statistics()

    def set_file_contents(self):
        with open(self.path, "r") as file:
            self.file_contents = [line.strip("\n") for line in file]

    def set_line_count_statistics(self):
        self.total_line_count = len(self.file_contents)
        self.blank_line_count = self.file_contents.count("")
        self.non_blank_line_count = self.total_line_count - self.blank_line_count

    def write_to_statistics_file(self, statistics_file):
        statistics_file.writelines(f"{self.indented_string}\n")

    def __str__(self):
        string = f"Path: {self.path}, Level: {self.level}"
        return string
