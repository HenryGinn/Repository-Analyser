class Statistic():

    min_column_width = 8

    def __init__(self, path_obj, name, statistic_type):
        self.repo = path_obj.repo
        self.path_obj = path_obj
        self.name = name
        self.type = statistic_type
        self.set_output_value_functions()

    def set_output_value_functions(self):
        self.output_value_functions = {"Sum": self.set_output_value_sum,
                                       "Mean": self.set_output_value_mean,
                                       "Percentage": self.set_output_value_percentage}

    def set_output_value(self):
        self.output_value_functions[self.type]()
        self.set_output_string()

    def set_output_value_sum(self):
        self.value = self.sum

    def set_output_value_mean(self):
        self.value = None

    def set_output_value_percentage(self):
        self.value = f"{round(100 * self.partial / self.total, 1)}%"

    def set_output_string(self):
        column_width = max(self.min_column_width, len(self.name) + 1)
        indent_length = column_width - len(str(self.value))
        indent = indent_length * " "
        self.output_string = f"{indent}{self.value}"

    def __str__(self):
        string = (f"Statistic name: {self.name}\n"
                  f"Statistic type: {self.type}\n"
                  f"Path name: {self.path_obj.name}\n")
        return string
