import os
import re


new_project_name = input("Enter the new project name: ")
os.system("dotnet new console --name " + new_project_name + " --output " + new_project_name)


def apply_file_template(code, path):
    modified_code = re.sub("PLACEHOLDER", new_project_name, code)

    print(modified_code)

    with open(path, 'w') as file:
        file.write(modified_code)

csharp_template_file = open("templates/template.cs", 'r')
python_build_file = open("templates/build.py", 'r')

apply_file_template(csharp_template_file.read(), new_project_name + "/Program.cs")
apply_file_template(python_build_file.read(), new_project_name + "/build.py")
