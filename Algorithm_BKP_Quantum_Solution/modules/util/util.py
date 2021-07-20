# -*- coding=utf-8 -*-

from modules.util.generalValue import SEPARATOR
import sys
import os
import numpy as np
from os import scandir, getcwd
import modules.util.generalValue as general

sys.path.append('../')
from datetime import datetime

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

def get_line_header(iterations):
    line =f"Number of iterations: {iterations} \n"
    line+="n-items | capacity | objective value | max profit | min profit | "
    line+="average profit | max capacity | min capacity | average capacity | "
    line+="exact solutions | NON exact solutions | success rate | "
    line+="max time   |   min time   |   average time"
    return line

def get_line_result_format(obj_kp, profits_solution, weights_solution, 
                            num_exact_solution, num_iterations, times):
    line =  fill_spaces(obj_kp.n_items(), 10)
    line += fill_spaces(obj_kp.capacity(), 11)
    line += fill_spaces(obj_kp.objective(), 17)
    line += fill_spaces(np.max(profits_solution), 13)
    line += fill_spaces(np.min(profits_solution), 13)
    line += fill_spaces(str(sum(profits_solution)/len(profits_solution)), 15)
    line += fill_spaces(np.max(weights_solution), 15)
    line += fill_spaces(np.min(weights_solution), 16)
    line += fill_spaces(sum(weights_solution) / len(weights_solution), 19)
    line += fill_spaces(num_exact_solution, 18)
    line += fill_spaces(num_iterations - num_exact_solution, 22)
    line += fill_spaces(str((num_exact_solution*100) / num_iterations)+"%", 17)
    line += fill_spaces("{0:.4f}".format(max(times)), 15)
    line += fill_spaces("{0:.4f}".format(min(times)), 15)
    line += fill_spaces("{0:.4f}".format(sum(times)/len(times)), 14)
    return line
    
def get_line_result(obj_kp, profits_solution, weights_solution, 
                    num_exact_solution, num_iterations, times):    
    line =  str(obj_kp.get_n_items() + " ")
    line += str(obj_kp.get_capacity() + " ")
    line += str(obj_kp.get_objective() + " ")
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