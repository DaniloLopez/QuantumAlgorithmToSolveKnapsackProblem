from modules.util.generalValue import SEPARATOR
import sys
sys.path.append('../')
import os
import numpy as np
from os import scandir, getcwd
from datetime import datetime
import modules.util.generalValue as general

def get_path():
    return os.getcwd()

def get_info_time():
    return datetime.now().strftime("%d%m%Y_%H%M%S")

def get_result_file_name():
    return (
        get_path() + SEPARATOR + "solutions" + SEPARATOR + "result_" + 
        get_info_time() + ".txt"
    )    

def fill_spaces(value, length):
    return str(value).ljust(length)[:length]

def get_list_files_folder(path = getcwd()):
    """list existing files in a given path"""
    return [arch.name for arch in scandir(path) if arch.is_file()]

def get_line_header(iterations) -> str:
    return f"Number of iterations: {iterations} \n"

def get_attr_value(attr, value, init=False):
    line = "\"" if init else ",    \""    
    return line + attr + "\": " + str(value)

def get_line_result_format(knapsack, list_fitness, list_efos, list_times, 
                        times_found_ideal, iterations, best_solution):
    line = "\t\"knapsack\": "
    line += str(knapsack)
    line += "\n\t\"best_solution\": "
    line += str(best_solution)
    line += "\n\t\"metadata\": {"
    line += get_attr_value("TIMES_FOUND_IDEAL", times_found_ideal, init=True)
    line += get_attr_value("FITNESS_LIST", list_fitness)
    line += get_attr_value("EFOS_LIST", list_efos)
    line += get_attr_value("AVERAGE_TIME", str(round((sum(list_times) * 100) / iterations, 2)))    
    line += " }"
    
    return line

def get_line_result(obj_kp, profits_solution, weights_solution, 
                    num_exact_solution, num_iterations, times):    
    line =  str(obj_kp.n_items + " ")
    line += str(obj_kp.capacity + " ")
    line += str(obj_kp.objective + " ")
    line += str(np.max(profits_solution) + " ")
    line += str(np.min(profits_solution) + " ")
    line += str(np.max(weights_solution) + " ")
    line += str(np.min(weights_solution) + " ")
    line += str(sum(weights_solution) / len(weights_solution) + " ")
    line += str(num_exact_solution + " ")
    line += str(num_iterations - num_exact_solution + " ")
    line += str(str((num_exact_solution*100) / num_iterations)+"%" + " ")
    line += str(max(times) + " ")
    line += str(min(times) + " ")
    line += str(sum(times)/len(times) + " ")
    return line

def generate_full_name_file(id, type, difficult, nitems, range):
    return (general.FOLDER_DATASET_GENERATED + SEPARATOR + difficult + 
            SEPARATOR + "t" + str(type) + "_d" +str(difficult) + 
            "_n" + str(nitems) + "_r" + str(range) + ".txt")

def build_commnad_line_text_generate(type, difficult, nitems, range, 
                                instance, S=1000):
    """
    type: 1=uncorrelated., 2=weakly corr., 3=strongly corr., 4=subset sum.
    difficult: difficult.
    nitems: number of items.
    range: range of coefficients.
    instance: instance no.
    S: number of tests in series (typically 1000).
    """
    return (str(id.n_items) + " " + str(id.range) + " " + str(id.type_corr) + 
            " " + str(instance) + " " + str(S) + " " + 
            generate_full_name_file(type, difficult, nitems, range))

def if_print_text(object, condition=True):
    if condition:
        print(object)