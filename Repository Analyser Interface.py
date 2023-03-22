from Repo import Repo

repo_path = "/home/henry/Documents/Python/Einstein's Riddle Solver 5"
#repo_path = "/home/henry/Documents/Python/My Programs/Projects/Puzzles/Einstein's Riddle/Einstein's Riddle Solver 5"
repo = Repo(repo_path)
#repo.output_files()
#repo.output_folders()
repo.create_statistics()
