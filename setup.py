import os

directories = [
    "data/raw",
    "data/processed",
    "notebooks",
    "src/data",
    "src/models",
    "src/utils",
    "src/config",
    "src/pipelines",
    "deployment",
]

files = {
    "src/data/preprocess.py": "",
    "src/data/feature_engineering.py": "",
    "src/models/train.py": "",
    "src/models/evaluate.py": "",
    "src/models/predict.py": "",
    "requirements.txt": "",
    "README.md": "",
    ".gitignore": "*.pyc\n__pycache__/\ndata/raw/\ndata/processed/",
}

def create_project_structure():
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    for file_path, content in files.items():
        with open(file_path, "w") as f:
            f.write(content)
    print("Project structure created successfully!")

if __name__ == "__main__":
    create_project_structure()
