import math

from Repo.Statistics.StatisticsGroup import StatisticsGroup
from Repo.Statistics.Statistic import Statistic
from Repo.Statistics.Methods import Methods

class MethodNameLength(StatisticsGroup):

    name = "Method Name Length"
    range_limits = [1, 5, 10, 15, 25, 35]

    def __init__(self, path_obj):
        StatisticsGroup.__init__(self, path_obj, self.name)

    def generate_statistics(self):
        self.preprocess_file_contents()
        self.get_methods()
        if len(self.methods_obj.methods) == 0:
            self.generate_statistics_trivial()
        else:
            self.generate_statistics_non_trivial()

    def generate_statistics_trivial(self):
        self.set_ranges()
        categories = [self.get_category(index)
                      for index in self.range_limits]
        self.statistics = [self.get_trivial_percentage_statistic(category)
                           for category in categories]

    def generate_statistics_non_trivial(self):
        self.initialise_length_dict()
        self.populate_length_dict()
        self.create_statistics()

    def preprocess_file_contents(self):
        self.file_contents_no_blanks = [line for line in self.file_contents
                                        if line.strip(" ") != ""]
        self.total_lines = len(self.file_contents_no_blanks)

    def get_methods(self):
        if not hasattr(self.path_obj, "methods_obj"):
            self.methods_obj = Methods(self.file_contents_no_blanks)
            self.methods_obj.find_methods()
        self.methods_obj.set_method_name_lengths()

    def initialise_length_dict(self):
        self.set_ranges()
        line_length_limit = max(self.methods_obj.longest_name_length, self.range_limits[-1]) + 1
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
        for method_name_length in self.methods_obj.method_name_lengths:
            category = self.length_categories[method_name_length]
            self.length_dict[category] += 1

    def create_statistics(self):
        self.statistics = [self.get_statistic(category, count)
                           for category, count in self.length_dict.items()]
        
    def get_statistic(self, category, count):
        statistic = Statistic(self.path_obj, category, "Percentage")
        statistic.partial = count
        statistic.total = self.total_lines
        return statistic
