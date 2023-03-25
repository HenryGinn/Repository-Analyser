from Path import Path
from StatisticGroupFolder import StatisticGroupFolder
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
        self.statistic_groups = []
        self.set_line_count_statistics()

    def set_line_count_statistics(self):
        line_count_statistics = StatisticGroupFolder(self, "Line Count")
        line_count_statistics.paths_statistics = [file.line_count_statistic
                                                  for file in self.files]
        line_count_statistics.paths_statistics += [folder.line_count_statistic
                                                   for folder in self.child_folders]
        line_count_statistics.process_paths_statistics()

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
        string = (f"\nPath: {self.path}, Level: {self.level}\n"
                  f"Child Folders: {get_string_list(self.child_folder_paths)}\n"
                  f"Files: {get_string_list(self.files)}")
        return string
