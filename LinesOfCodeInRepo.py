import os

def output_line_count(path, level):
    if directory_contains_python_files(path):
        print(f"{indent * level}{os.path.basename(path)}")
        for directory in os.listdir(path):
            new_path = os.path.join(path, directory)
            process_path(new_path, level + 1)

def directory_contains_python_files(path):
    if os.path.isdir(path) is False:
        if path_is_python_file(path):
            return True
    else:
        contains_python = False
        for directory in os.listdir(path):
            new_path = os.path.join(path, directory)
            contains_python = directory_contains_python_files(new_path)
            if contains_python:
                return True
        return contains_python

def process_path(path, level):
    if os.path.isdir(path):
        output_line_count(path, level)
    elif path_is_python_file(path):
        output_python_file_line_count(path, level)

def path_is_python_file(path):
    return (path.endswith(".py"))

def output_python_file_line_count(path, level):
    level_indent = indent * level
    name = os.path.basename(path)
    line_count = get_line_count(path)
    space = get_space(level_indent, name, line_count)
    print(f"{level_indent}{name}: {space}{line_count}")

def get_line_count(path):
    with open(path, "r") as file:
        lines = [line.strip() for line in file]
    line_count = len(lines)
    global total_line_count, total_blank_line_count
    total_line_count += line_count
    total_blank_line_count += lines.count("")
    return line_count

def get_space(level_indent, name, line_count):
    space_count = display_width - len(level_indent + name + str(line_count))
    check_spaces_non_negative(space_count)
    space = " " * space_count
    return space

def check_spaces_non_negative(space_count):
    if space_count < 0:
        raise ValueError("Space is negative, increase display_width")
    
display_width = 60
indent = "  "

total_line_count = 0
total_blank_line_count = 0
repo_path = "/home/henry/Documents/Python/My Programs/Projects/Puzzles/Einstein's Riddle/Einstein's Riddle Solver 5"
output_line_count(repo_path, 0)

print((f"\nTotal: {total_line_count}\n"
       f"Blank lines: {total_blank_line_count}\n"
       f"Non-blank lines: {total_line_count - total_blank_line_count}\n"))
