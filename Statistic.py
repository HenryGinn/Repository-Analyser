class Statistic():

    def __init__(self, repo, path_obj, name, statistic_type):
        self.repo = repo
        self.path_obj = path_obj
        self.name = name
        self.type = statistic_type

    def compute_folder_statistic(self):
        functions = self.get_compute_folder_statistic_functions()
        functions[self.type]()

    def get_compute_folder_statistic_functions(self):
        function = {"Sum": self.folder_statistic_sum,
                    "Mean": self.folder_statistic_mean}
        return functions

    def folder_statistic_sum(self):
        pass

    def folder_statistic_mean(self):
        pass
