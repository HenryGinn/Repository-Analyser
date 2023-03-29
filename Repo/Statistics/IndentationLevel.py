import math

from Repo.Statistics.StatisticsGroup import StatisticsGroup
from Repo.Statistics.Statistic import Statistic

class IndentationLevel(StatisticsGroup):

    name = "Indentation Level"
    max_indent_level = 5
    indent_level = 4

    def __init__(self, path_obj):
        StatisticsGroup.__init__(self, path_obj, self.name)

    def generate_statistics(self):
        self.preprocess_file_contents()
        self.initialise_indent_dict()
        self.populate_indent_dict()
        self.create_statistics_from_indent_dict()

    def preprocess_file_contents(self):
        self.file_contents_no_blanks = [line for line in self.file_contents
                                        if line.strip(" ") != ""]

    def initialise_indent_dict(self):
        self.indent_dict = {str(indent): 0 for indent in range(self.max_indent_level)}
        self.max_indent_key = f"{self.max_indent_level}+"
        self.indent_dict[self.max_indent_key] = 0

    def populate_indent_dict(self):
        if len(self.file_contents) > 0:
            self.populate_indent_dict_non_trivial()
        else:
            self.indent_dict["0"] = 1

    def populate_indent_dict_non_trivial(self):
        indents = self.get_indents()
        indents = self.remove_line_continuation_indents(indents)
        self.add_indents_to_indent_dict(indents)
    
    def get_indents(self):
        indents = [self.get_indent(line)
                   for line in self.file_contents_no_blanks]
        return indents

    def get_indent(self, line):
        spaces = len(line) - len(line.lstrip(" "))
        indent = math.ceil(spaces / self.indent_level)
        return indent

    def remove_line_continuation_indents(self, indents):
        for index in range(len(indents) - 1):
            if indents[index + 1] > indents[index] + 1:
                indents[index + 1] = indents[index]
        return indents

    def add_indents_to_indent_dict(self, indents):
        for indent in indents:
            self.process_indent(indent)

    def process_indent(self, indent):
        if indent < self.max_indent_level:
            self.indent_dict[str(indent)] += 1
        else:
            self.indent_dict[self.max_indent_key] += 1

    def create_statistics_from_indent_dict(self):
        self.total_lines = sum(self.indent_dict.values())
        self.statistics = [self.get_statistic(indent, line_count)
                           for indent, line_count in self.indent_dict.items()]

    def get_statistic(self, indent, line_count):
        statistic = Statistic(self.path_obj, indent, "Percentage")
        statistic.partial = line_count
        statistic.total = self.total_lines
        return statistic
