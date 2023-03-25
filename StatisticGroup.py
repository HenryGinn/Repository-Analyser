class StatisticGroup():

    def __init__(self, path_obj, name):
        self.repo = path_obj.repo
        self.path_obj = path_obj
        self.name = name
        self.statistics = []
