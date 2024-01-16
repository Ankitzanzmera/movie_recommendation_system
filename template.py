from pathlib import Path
import os

project_name = "movie_recommendation_system"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/utils/logger.py",
    f"src/{project_name}/utils/exception.py",
    "app.py",
    "main.py",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    dirname, filename = os.path.split(filepath)
    # print(dirname,filename)

    if dirname != "":
        os.makedirs(dirname,exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w"):
            pass
    else:
        print("File Already Existed")

