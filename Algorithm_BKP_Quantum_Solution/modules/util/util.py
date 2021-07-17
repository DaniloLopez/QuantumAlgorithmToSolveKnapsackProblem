# -*- coding=utf-8 -*-

import sys
import os
import numpy as np

sys.path.append('../')
from datetime import datetime
from pathlib import Path

def get_project_root():
    return Path(__file__).parent.parent.parent

def get_path():
    return os.getcwd()

def get_separator():
    return os.path.sep

def get_line_separator():
    return os.linesep

def get_info_time():
    return datetime.now().strftime("%d%m%Y_%H%M%S")

def get_result_file_name():
    return (get_path() + get_separator() + "solutions" + get_separator() + 
            "result_" + get_info_time() + ".txt")    

def fill_spaces(value, tamanio):
    return str(value).ljust(tamanio)[:tamanio]

def get_line_header(iterations):
    line =f"Number of iterations: {iterations} \n"
    line+="n-items | capacity | objetive value | max profit | min profit | "
    line+="average profit | max capacity | min capacity | average capacity | "
    line+="exact solutions | NON exact solutions | success rate | "
    line+="max time   |   min time   |   average time"
    return line

def get_line_result_format(obj_kp, profits_solution, weigths_solution, 
                            num_exact_solution, num_iterations, times):    
    line =  fill_spaces(obj_kp.get_n_items(), 10)
    line += fill_spaces(obj_kp.get_capacity(), 11)
    line += fill_spaces(obj_kp.get_objetive(), 17)
    line += fill_spaces(np.max(profits_solution), 13)
    line += fill_spaces(np.min(profits_solution), 13)
    line += fill_spaces(str(sum(profits_solution)/len(profits_solution)), 15)
    line += fill_spaces(np.max(weigths_solution), 15)
    line += fill_spaces(np.min(weigths_solution), 16)
    line += fill_spaces(sum(weigths_solution) / len(weigths_solution), 19)
    line += fill_spaces(num_exact_solution, 18)
    line += fill_spaces(num_iterations - num_exact_solution, 22)
    line += fill_spaces(str((num_exact_solution*100) / num_iterations)+"%", 17)
    line += fill_spaces("{0:.4f}".format(max(times)), 15)
    line += fill_spaces("{0:.4f}".format(min(times)), 15)
    line += fill_spaces("{0:.4f}".format(sum(times)/len(times)), 14)
    return line
    
def get_line_result(obj_kp, profits_solution, weigths_solution, 
                    num_exact_solution, num_iterations, times):    
    line =  str(obj_kp.get_n_items() + " ")
    line += str(obj_kp.get_capacity() + " ")
    line += str(obj_kp.get_objetive() + " ")
    line += str(np.max(profits_solution) + " ")
    line += str(np.min(profits_solution) + " ")
    line += str(np.max(weigths_solution) + " ")
    line += str(np.min(weigths_solution) + " ")
    line += str(sum(weigths_solution) / len(weigths_solution) + " ")
    line += str(num_exact_solution + " ")
    line += str(num_iterations - num_exact_solution + " ")
    line += str(str((num_exact_solution*100) / num_iterations)+"%" + " ")
    line += str(max(times) + " ")
    line += str(min(times) + " ")
    line += str(sum(times)/len(times) + " ")
    return line

def generateNameFile(id, level, name):
    return (general.FOLDER_GENERATED_DATASET + get_separator() + name + 
            get_separator() + "t" + str(id.type_corr) + "_d" +str(level) + 
            "_n" + str(id.n_items) + "_r" + str(id.range) + ".txt")

def generateUrlNewDataset(id, level, name_folder):
    return (str(id.n_items) + " " + str(id.range) + " " + str(id.type_corr) + 
            " " + str(id.n_instances) + " " + str(id.n_test) + " " + 
            generateNameFile(id, level, name_folder))