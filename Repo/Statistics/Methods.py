class Methods():

    def __init__(self, file_contents):
        self.file_contents = file_contents

    def find_methods(self):
        self.methods = []
        stripped_lines = self.get_stripped_lines()
        self.set_space_indentations(stripped_lines)
        self.populate_methods(stripped_lines)

    def populate_methods(self, stripped_lines):
        for index, line in enumerate(self.file_contents):
            if stripped_lines[index].startswith("def "):
                self.add_method(index, line, stripped_lines)

    def get_stripped_lines(self):
        stripped_lines = [line.lstrip(" ")
                          for line in self.file_contents]
        return stripped_lines

    def set_space_indentations(self, stripped_lines):
        lines_iterable = zip(self.file_contents, stripped_lines)
        self.space_indentations = [len(line) - len(stripped_line)
                                   for line, stripped_line in lines_iterable]

    def add_method(self, index, line, stripped_lines):
        space_indentation = self.space_indentations[index]
        method_lines = [line]
        method_lines = self.populate_method_lines(index, method_lines, space_indentation)
        self.methods.append(method_lines)

    def populate_method_lines(self, index, method_lines, space_indentation):
        for line, indent in zip(self.file_contents[index + 1:], self.space_indentations[index + 1:]):
            if indent == space_indentation:
                break
            method_lines.append(line)
        return method_lines

    def set_method_lengths(self):
        self.method_lengths = [len(method) - 1 for method in self.methods]
        self.method_count = len(self.methods)
        self.set_longest_method()

    def set_longest_method(self):
        if self.method_count > 0:
            self.longest_method = max(self.method_lengths)
        else:
            self.longest_method = 0

    def set_method_name_lengths(self):
        self.method_name_lengths = [self.get_method_name_length(method[0])
                                    for method in self.methods]
        if len(self.method_name_lengths) > 0:
            self.longest_name_length = max([method_name_length
                                            for method_name_length in self.method_name_lengths])

    def get_method_name_length(self, method_first_line):
        bracket_index = method_first_line.index("(")
        method_name = method_first_line[:bracket_index]
        method_name = method_name.lstrip(" ").lstrip("def ")
        return len(method_name)
