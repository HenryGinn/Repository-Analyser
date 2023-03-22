import os

class Path():

    def __init__(self, repo, path):
        self.repo = repo
        self.path = path
        self.name = os.path.basename(path)

    def set_path_history(self):
        self.path_history = []
        self.reduce_level(self.path)
        self.level = len(self.path_history)
        self.set_indented_string()

    def reduce_level(self, path):
        if path != self.repo.path:
            new_path_tail, new_path_head = os.path.split(path)
            self.path_history.append(new_path_tail)
            self.reduce_level(new_path_tail)

    def set_indented_string(self):
        indent = self.level * self.repo.space
        self.indented_string = f"{indent}{self.name}"
