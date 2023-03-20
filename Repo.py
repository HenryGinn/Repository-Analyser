import os

class Repo():

    def __init__(self, path):
        self.path = path
        self.repo_name = os.path.basename(path)
        self.set_program_structure()

    def set_program_structure(self):
        self.folders = []
        self.files = []
        self.check_if_directories_contain_python(self.path)

    def check_if_directories_contain_python(self, path):
        contains_python = False
        contains_python = self.get_contains_python(path)
        return contains_python

    def get_contains_python(path):
        if os.path.isdir(path):
            contains_python = self.check_if_directories_contain_python_folder(path)
        else:
            contains_python = self.check_if_directories_contain_python_file(path)
        return contains_python

    def check_if_directories_contain_python_folder(self, path):
        pass

    def check_if_directories_contain_python_file(self, path):
        if path.endswith(".py"):
            self.files.append(path)
            return True
        else:
            return False
        
