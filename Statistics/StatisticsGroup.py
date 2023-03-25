from Statistics.Statistic import Statistic
from Utils import get_string_list

class StatisticsGroup():

    def __init__(self, path_obj, name):
        self.repo = path_obj.repo
        self.path_obj = path_obj
        self.name = name
        self.statistics = []
        self.statistic_names = []

    def generate_for_file(self):
        self.file_contents = self.path_obj.file_contents
        self.generate_statistics()
        self.set_statistic_names()
        self.set_output_values()

    def set_statistic_names(self):
        self.statistic_names = [statistic.name for statistic in self.statistics]

    def generate_for_folder(self, group_name):
        self.set_statistic_functions_type_dict()
        statistics_dict = self.get_statistics_dict(group_name)
        self.set_statistics_from_statistics_dict(statistics_dict)
        self.set_output_values()

    def set_statistic_functions_type_dict(self):
        self.statistic_functions_type_dict = {"Sum": self.get_statistic_sum,
                                              "Mean": self.get_statistic_mean}

    def get_statistics_dict(self, group_name):
        statistics_dict = self.initialise_statistics_dict(group_name)
        statistics_dict = self.populate_statistics_dict(statistics_dict, group_name)
        return statistics_dict

    def initialise_statistics_dict(self, group_name):
        statistics_list = self.path_obj.children[0].statistic_groups[group_name].statistics
        statistics_dict = {statistic.name: [] for statistic in statistics_list}
        return statistics_dict

    def populate_statistics_dict(self, statistics_dict, group_name):
        for child in self.path_obj.children:
            for statistic in child.statistic_groups[group_name].statistics:
                statistics_dict[statistic.name].append(statistic)
        return statistics_dict

    def set_statistics_from_statistics_dict(self, statistics_dict):
        self.statistics = [self.get_statistic_from_statistic_list(statistic_list)
                           for statistic_list in statistics_dict.values()]
        self.set_statistic_names()

    def get_statistic_from_statistic_list(self, statistic_list):
        statistic_type = statistic_list[0].type
        get_statistic_function = self.statistic_functions_type_dict[statistic_type]
        statistic = get_statistic_function(statistic_list)
        return statistic

    def get_statistic_sum(self, statistic_list):
        name = statistic_list[0].name
        new_statistic = Statistic(self.path_obj, name, "Sum")
        new_statistic.sum = sum([statistic.sum for statistic in statistic_list])
        return new_statistic
        
    def get_statistic_mean(self, statistic_list):
        pass

    def set_output_values(self):
        for statistic in self.statistics:
            statistic.set_output_value()

    def __str__(self):
        string = (f"Name: {self.name}\n"
                  f"Associated path name: {self.path_obj.name}\n"
                  f"Statistics: {get_string_list(self.statistic_names)}\n")
        return string
