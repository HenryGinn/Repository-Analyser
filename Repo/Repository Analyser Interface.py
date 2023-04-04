from FolderStructure.Repo import Repo

#repo_path = "/home/henry/Documents/Python/Einstein's Riddle Solver 5"
#repo_path = "/home/henry/Documents/Python/Games and Puzzles/Einstein's Riddle/Versions/Einstein's Riddle Solver 5"
repo_path = "/home/henry/Documents/Physics Internship/Optomechanics-Data-Analysis"
repo = Repo(repo_path)
repo.setup_repository()
repo.create_results_folders()
repo.create_statistics()
