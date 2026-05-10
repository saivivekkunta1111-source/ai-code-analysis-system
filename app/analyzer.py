import os

SUPPORTED_EXTENSIONS = [
    ".py",
    ".js",
    ".ts",
    ".java",
    ".cpp",
    ".html",
    ".css",
    ".md"
]

def read_project_files(folder_path):

    all_code = ""

    for root, dirs, files in os.walk(folder_path):

        for file in files:

            if file.endswith(tuple(SUPPORTED_EXTENSIONS)):

                file_path = os.path.join(root, file)

                try:

                    with open(file_path, "r", encoding="utf-8") as f:

                        content = f.read()

                        all_code += f"\n\nFILE: {file_path}\n"

                        all_code += content

                except:

                    pass

    return all_code