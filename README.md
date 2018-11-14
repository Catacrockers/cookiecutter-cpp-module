# cookiecutter-cpp-module

 This cookiecutter template create a CPP project (compatible with C) module. Generate an independent binary. It can be user standalone or include into samples folder at cookiecutter-cpp-project repository.

Note: This is the template README, this will not appear in the final project.

# Install

Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):

```
pip install -U cookiecutter
```

# Usage

## Project generation

Go to path where you want to generate a project and execute:

```
cookiecutter $(path_to_basic_folder)
```

* Note: It is possible to avoid set up input, using default values with ```--no-input``` option.
* Note II: It is possible to provide variables though command using ```$(key)=$(value)``` syntax with the command.
* Note III: It is possible to use a yaml with a configuration using option ```--config-file $(config_file).yaml```

Example using config file by default:

```
cookiecutter $(path_to_basic_folder) --config-file $(config_file).yaml --no-input
```

Example using from Github:

```
cookiecutter https://github.com/Catacrockers/cookiecutter-cpp-project.git
```
