import os
import subprocess

os.system("dotnet.exe build")

p = subprocess.Popen("\\"bin/Debug/net8.0/PLACEHOLDER.exe\\"", creationflags=subprocess.CREATE_NEW_CONSOLE)