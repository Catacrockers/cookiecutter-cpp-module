import sys
import os
import shutil

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

create_main = '{{cookiecutter.module_type}}' == 'bin'

if __name__ == "__main__":
    print("Posthook for {{ cookiecutter.project_name}}")

    if not create_main:
        remove('src/main.cpp')

    exit(0)
