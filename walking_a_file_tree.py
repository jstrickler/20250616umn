import os

START_FOLDER = "."

FOLDERS_TO_SKIP = ['.git', 'cookiecutter-python-module', 'cookiecutter-python-package']

for folder, subfolders, files in os.walk(START_FOLDER):
    for folder_to_skip in FOLDERS_TO_SKIP:
        if folder_to_skip in subfolders:
            subfolders.remove(folder_to_skip)
    
    print(folder) 
    for file_name in files:
        if file_name.startswith('p') and file_name.endswith('.py'):
            file_path = os.path.join(folder, file_name)
            file_size = os.path.getsize(file_path)
            print(f"    {file_size:10d} {file_name} {file_path}")
