import os
import sys

class Catalogue():

    def __init__(self, path):
        self.path = path
        self.set_parent_results_path()
        self.identify_repositories()

    def set_parent_results_path(self):
        script_path = sys.path[0]
        parent_path = os.path.dirname(script_path)
        self.parent_results_path = os.path.join(parent_path, "Results")
        self.create_parent_results_folder()

    def create_parent_results_folder(self):
        if not os.path.exists(self.parent_results_path):
            print(f"Creating 'Results' folder at {self.parent_results_path}")
            os.mkdir(self.parent_results_path)
    
    def identify_repositories(self):
        for directory in os.listdir(self.path):
            print(directory)
