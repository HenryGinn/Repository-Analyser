from Repo.Statistics.StatisticsGroup import StatisticsGroup
from Repo.Statistics.Statistic import Statistic

class LineCount(StatisticsGroup):

    name = "Line Count"

    def __init__(self, path_obj):
        StatisticsGroup.__init__(self, path_obj, self.name)

    def generate_statistics(self):
        self.set_total_line_count()
        self.set_blank_line_count()
        self.set_non_blank_line_count()

    def set_total_line_count(self):
        total_line_count_statistic = Statistic(self, "Total Lines", "Sum")
        total_line_count = len(self.file_contents)
        total_line_count_statistic.sum = total_line_count
        self.statistics.append(total_line_count_statistic)

    def set_blank_line_count(self):
        blank_line_count_statistic = Statistic(self, "Blank Lines", "Sum")
        blank_line_count = self.file_contents.count("")
        blank_line_count_statistic.sum = blank_line_count
        self.statistics.append(blank_line_count_statistic)

    def set_non_blank_line_count(self):
        non_blank_line_count_statistic = Statistic(self, "Non-Blank Lines", "Sum")
        non_blank_line_count = len(self.file_contents) - self.file_contents.count("")
        non_blank_line_count_statistic.sum = non_blank_line_count
        self.statistics.append(non_blank_line_count_statistic)

