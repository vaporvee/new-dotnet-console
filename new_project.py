import os
import re


new_project_name = input("Enter the new project name: ")
os.system("dotnet new console --name " + new_project_name + " --output " + new_project_name)


def apply_file_template(code, path):
    modified_code = re.sub("PLACEHOLDER", new_project_name, code)

    print(modified_code)

    with open(path, 'w') as file:
        file.write(modified_code)

csharp_code = """
namespace PLACEHOLDER
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hi mom");
            Console.ReadLine();
        }

    }
}
"""


python_code = """
import os
import subprocess

os.system("dotnet.exe build")

p = subprocess.Popen("\\"bin/Debug/net8.0/PLACEHOLDER.exe\\"", creationflags=subprocess.CREATE_NEW_CONSOLE)
"""

apply_file_template(csharp_code, new_project_name + "/Program.cs")
apply_file_template(python_code, new_project_name + "/build.py")
