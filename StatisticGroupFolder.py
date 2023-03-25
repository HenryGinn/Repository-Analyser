from StatisticGroup import StatisticGroup
from Statistic import Statistic

class StatisticGroupFolder(StatisticGroup):

    def __init__(self, path_obj, name):
        StatisticGroup.__init__(self, path_obj, name)

    def process_paths_statistics(self):
        self.create_statistics_paths()
        self.create_statistics()

    def create_statistics_paths(self):
        self.initialise_statistics_paths()
        self.populate_statistics_paths()

    def initialise_statistics_paths(self):
        self.statistic_names = self.paths_statistics[0].statistic_names
        self.statistics_paths = {statistic_name: []
                                 for statistic_name in self.statistic_names}

    def populate_statistics_paths(self):
        for paths_statistic in self.paths_statistics:
            for statistic in paths_statistic.statistics:
                self.statistics_paths[statistic.name].append(statistic)

    def create_statistics(self):
        self.statistics = [self.get_statistic(statistic_paths)
                           for statistic_paths in self.statistics_paths.values()]

    def get_statistic(self, statistic_list):
        name = statistic_list[0].name
        statistic_type = statistic_list[0].type
        self.statistic = Statistic(self.path_obj, name, statistic_type)
        self.statistic.set_statistic_from_statistic_list(statistic_list)

