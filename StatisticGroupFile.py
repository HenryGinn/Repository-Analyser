from StatisticGroup import StatisticGroup

class StatisticGroupFile(StatisticGroup):

    def __init__(self, path_obj, name):
        StatisticGroup.__init__(self, path_obj, name)

    def set_statistic_names(self):
        self.statistic_names = [statistic.name for statistic in self.statistics]
