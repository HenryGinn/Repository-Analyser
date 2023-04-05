import math

from Repo.Statistics.StatisticsGroup import StatisticsGroup
from Repo.Statistics.Statistic import Statistic

class LineLength(StatisticsGroup):

    name = "Line Length"
    range_limits = [1, 10, 20, 30, 40, 50, 60, 70, 80]

    def __init__(self, path_obj):
        StatisticsGroup.__init__(self, path_obj, self.name)

    def generate_statistics(self):
        self.preprocess_file_contents()
        if len(self.file_contents_no_blanks) == 0:
            self.generate_statistics_trivial()
        else:
            self.generate_statistics_non_trivial()

    def generate_statistics_trivial(self):
        self.set_ranges()
        categories = [self.get_category(index)
                      for index in self.range_limits]
        print(categories)
        self.statistics = [self.get_trivial_percentage_statistic(category)
                           for category in categories]

    def generate_statistics_non_trivial(self):
        self.set_longest_longest()
        self.initialise_length_dict()
        self.populate_length_dict()
        self.create_statistics()

    def preprocess_file_contents(self):
        self.file_contents_no_blanks = [line for line in self.file_contents
                                        if line.strip(" ") != ""]
        self.total_lines = len(self.file_contents_no_blanks)

    def set_longest_longest(self):
        self.longest_length = max([len(line)
                                   for line in self.file_contents_no_blanks])

    def initialise_length_dict(self):
        self.set_ranges()
        line_length_limit = max(self.longest_length, self.range_limits[-1]) + 1
        self.length_categories = {index: self.get_category(index)
                                  for index in range(1, line_length_limit)}
        self.length_dict = {category: 0 for category in self.length_categories.values()}

    def set_ranges(self):
        pairs_iterable = zip(self.range_limits[:-1], self.range_limits[1:])
        self.ranges = [list(range(start, stop))
                       for start, stop in pairs_iterable]

    def get_category(self, index):
        for length_range in self.ranges:
            if index in length_range:
                return f"{length_range[0]}-{length_range[-1]}"
        return f"{self.range_limits[-1]}+"

    def populate_length_dict(self):
        for line in self.file_contents_no_blanks:
            category = self.length_categories[len(line)]
            self.length_dict[category] += 1

    def create_statistics(self):
        self.statistics = [self.get_statistic(category, count)
                           for category, count in self.length_dict.items()]
        
    def get_statistic(self, category, count):
        statistic = Statistic(self.path_obj, category, "Percentage")
        statistic.partial = count
        statistic.total = self.total_lines
        return statistic
