import math

from Repo.Statistics.StatisticsGroup import StatisticsGroup
from Repo.Statistics.Statistic import Statistic
from Repo.Statistics.Methods import Methods

class MethodLength(StatisticsGroup):

    name = "Method Length"
    longest_method = 7

    def __init__(self, path_obj):
        StatisticsGroup.__init__(self, path_obj, self.name)

    def generate_statistics(self):
        self.preprocess_file_contents()
        self.set_length_categories()
        self.generate_statistics_choice()

    def preprocess_file_contents(self):
        if not hasattr(self, "file_contents_no_blanks"):
            self.file_contents_no_blanks = [line for line in self.file_contents
                                            if line.strip(" ") != ""]
        self.total_lines = len(self.file_contents_no_blanks)

    def set_length_categories(self):
        self.length_categories = [str(length) for length in range(1, self.longest_method)]
        self.length_categories.append(f"{self.longest_method}+")

    def generate_statistics_choice(self):
        if len(self.file_contents_no_blanks) == 0:
            self.generate_statistics_trivial()
        else:
            self.generate_statistics_non_trivial()

    def generate_statistics_trivial(self):
        self.statistics = [self.get_trivial_percentage_statistic(category)
                           for category in self.length_categories]

    def generate_statistics_non_trivial(self):
        self.get_methods()
        self.initialise_dicts_and_lookups()
        self.populate_length_dict()
        self.create_statistics()

    def get_methods(self):
        if not hasattr(self.path_obj, "methods_obj"):
            self.methods_obj = Methods(self.file_contents_no_blanks)
            self.methods_obj.find_methods()

    def initialise_dicts_and_lookups(self):
        self.lengths_dict = {category: 0 for category in self.length_categories}
        self.methods_obj.set_method_lengths()
        self.category_lookup = {length: self.get_category(length)
                                for length in range(0, self.methods_obj.longest_method + 1)}

    def get_category(self, length):
        if length < self.longest_method:
            category = str(length)
        else:
            category = f"{self.longest_method}+"
        return category

    def populate_length_dict(self):
        for method_length in self.methods_obj.method_lengths:
            category = self.category_lookup[method_length]
            self.lengths_dict[category] += 1

    def create_statistics(self):
        self.statistics = [self.get_statistic(category, count)
                           for category, count in self.lengths_dict.items()]
        
    def get_statistic(self, category, count):
        statistic = Statistic(self.path_obj, category, "Percentage")
        statistic.partial = count
        statistic.total = self.methods_obj.method_count
        return statistic
