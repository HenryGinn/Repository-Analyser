class Statistic():

    def __init__(self, path_obj, name, statistic_type):
        self.repo = path_obj.repo
        self.path_obj = path_obj
        self.name = name
        self.type = statistic_type
        self.set_compute_folder_statistic_functions()

    def set_statistic_from_statistic_list(self, statistic_list):
        self.functions[self.type](statistic_list)

    def set_compute_folder_statistic_functions(self):
        self.functions = {"Sum": self.folder_statistic_sum,
                          "Mean": self.folder_statistic_mean}

    def folder_statistic_sum(self, statistic_list):
        self.sum = sum([statistic.sum for statistic in statistic_list])
        
    def folder_statistic_mean(self, statistic_list):
        print("Mean")

    def __str__(self):
        string = (f"Statistic name: {self.name}\n"
                  f"Statistic type: {self.type}\n"
                  f"Path name: {self.path_obj.name}\n")
        return string
