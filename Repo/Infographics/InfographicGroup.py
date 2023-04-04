from Plotting.Plots import Plots
from Plotting.Lines import Lines
from Plotting.Line import Line

class InfographicGroup():

    def __init__(self, path_obj):
        self.path_obj = path_obj

    def create_infographic(self):
        plots_obj = self.get_plots_obj()
        plots_obj.parent_results_path = self.path_obj.repo.repo_results_path
        plots_obj.plot()

    def get_plots_obj(self):
        lines_objects = [self.get_lines_obj(statistic_group)
                         for statistic_group in self.path_obj.statistic_groups.values()]
        plots_obj = Plots(lines_objects, subplot_count = 6)
        plots_obj.title = self.path_obj.name.strip(".py")
        return plots_obj

    def get_lines_obj(self, statistic_group):
        line_objects = [self.get_line_obj(statistic_group)]
        lines_obj = Lines(line_objects, "Qualitative", "bar")
        lines_obj.title = statistic_group.name
        return lines_obj

    def get_line_obj(self, statistic_group):
        x_values = [statistic.name for statistic in statistic_group.statistics]
        y_values = [statistic.value for statistic in statistic_group.statistics]
        line_obj = Line(x_values, y_values)
        line_obj.angle = 0
        line_obj.ha = "centre"
        return line_obj
