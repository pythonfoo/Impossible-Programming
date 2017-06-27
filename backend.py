import random
import list_gen

project_filename = "Projektauswahl.txt"
language_filename = "Programmiersprachen.txt"
constraint_filename = "constraints.txt"
job_filename = "Aufgaben.txt"

def get_project():
    project_list = list_gen.lines_from_file(project_filename)
    project = random.choice(project_list)
    return project

def get_language():
    language_list = list_gen.lines_from_file(language_filename)
    language = random.choice(language_list)
    return language

def get_constraint():
    constraint_list = list_gen.lines_from_file(constraint_filename)
    constraint = random.choice(constraint_list)
    return constraint

def get_job(project, language, constraint):
    project = project.strip("\n")
    language = language.strip("\n")
    constraint = constraint.strip("\n")
    result = "Schreibe {0} in {1} {2}.".format(project, language, constraint)
    return result

def save_job(job_str):
    job_str += "\n\n"
    with open(job_filename, "a") as file_obj:
        file_obj.write(job_str)
    