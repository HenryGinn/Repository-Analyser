import os

from Utils import make_folder
from Plotting.Plots import Plots
from Plotting.Lines import Lines
from Plotting.Line import Line

class InfographicFile():

    def __init__(self, repo_obj, statistic_group_name):
        self.repo_obj = repo_obj
        self.statistic_group_name = statistic_group_name

    def create_infographic(self):
        plots_obj = self.get_plots_obj()
        path = os.path.join(self.repo_obj.repo_results_path, self.statistic_group_name)
        make_folder(path)
        plots_obj.parent_results_path = path
        plots_obj.plot()

    def get_plots_obj(self):
        lines_objects = [self.get_lines_obj(statistic)
                         for statistic in self.repo_obj.base_folder.statistic_groups[self.statistic_group_name].statistics]
        plots_obj = Plots(lines_objects, subplots=1)
        plots_obj.title = f"{self.statistic_group_name} Statistics for {self.repo_obj.repo_name}"
        return plots_obj

    def get_lines_obj(self, statistic):
        line_objects = [self.get_line_obj(statistic.name)]
        lines_obj = Lines(line_objects, "Qualitative", "bar")
        lines_obj.title = statistic.name
        lines_obj.y_label = {"Sum": None, "Mean": "Average", "Percentage": "%"}[statistic.type]
        return lines_obj

    def get_line_obj(self, statistic_name):
        x_values = [file_obj.name for file_obj in self.repo_obj.files]
        y_values = [[statistic.value for statistic in file_obj.statistic_groups[self.statistic_group_name].statistics
                     if statistic.name == statistic_name][0] for file_obj in self.repo_obj.files]
        line_obj = Line(x_values, y_values)
        return line_obj
