class Statistic():

    def __init__(self, path_obj, name, statistic_type):
        self.repo = path_obj.repo
        self.path_obj = path_obj
        self.name = name
        self.type = statistic_type
        self.set_functions()

    def set_functions(self):
        self.set_compute_folder_statistic_functions()
        self.set_output_value_functions()
        
    def set_compute_folder_statistic_functions(self):
        self.compute_folder_statistic_functions = {"Sum": self.folder_statistic_sum,
                                                   "Mean": self.folder_statistic_mean}

    def set_output_value_functions(self):
        self.output_value_functions = {"Sum": self.set_output_value_sum,
                                       "Mean": self.set_output_value_mean}

    def set_statistic_from_statistic_list(self, statistic_list):
        self.compute_folder_statistic_functions[self.type](statistic_list)

    def folder_statistic_sum(self, statistic_list):
        self.sum = sum([statistic.sum for statistic in statistic_list])
        
    def folder_statistic_mean(self, statistic_list):
        print("Mean")

    def set_output_value(self):
        self.output_value_functions[self.type]()
        self.set_output_string()

    def set_output_value_sum(self):
        self.value = self.sum

    def set_output_value_mean(self):
        self.value = None

    def set_output_string(self):
        column_width = max(self.repo.column_width, len(self.name) + 1)
        indent_length = column_width - len(str(self.value))
        indent = indent_length * " "
        self.output_string = f"{indent}{self.value}"

    def __str__(self):
        string = (f"Statistic name: {self.name}\n"
                  f"Statistic type: {self.type}\n"
                  f"Path name: {self.path_obj.name}\n")
        return string
