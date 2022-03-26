import sys
import os
import math
import numpy as np
import modules.util.generalValue as general

from os import scandir, getcwd
from modules.util.generalValue import SEPARATOR
from datetime import datetime
from modules.util import util

sys.path.append('../')

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


def get_list_files_folder(path=getcwd()):
    """list existing files in a given path"""
    return [arch.name for arch in scandir(path) if arch.is_file()]


def get_line_header(iterations) -> str:
    return f"Number of iterations: {iterations} \n"


def get_attr_value(attr, value, init=False):
    line = "\"" if init else ",    \""
    return line + attr + "\": " + str(value)


def get_line_result_format(knapsack, list_fitness, list_efos, list_times,
                           times_found_ideal, iterations, best_solution):
    avg = sum(list_fitness) / len(list_fitness)
    var = sum((fit-avg)**2 for fit in list_fitness) / len(list_fitness)
    st_dev = math.sqrt(var)

    #line = "best_solution: " + str(best_solution)
    line = "success_rate: " + \
        str(round(((times_found_ideal*100)/iterations), 2)) + "% "
    line += "fitness_average: " + str(round(float(avg), 2)) + "% "
    line += "standar_deviation: " + str(round(st_dev, 2)) +" "
    line += "best_fitness: " + str(max(list_fitness)) +" "
    line += "worst_fitness: " + str(min(list_fitness)) + " "
    line +="average_time: " + str(round((sum(list_times) * 100) / iterations, 2))+ " ###"
    return line


def get_line_result(obj_kp, profits_solution, weights_solution,
                    num_exact_solution, num_iterations, times):
    line = str(obj_kp.n_items + " ")
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


def generate_full_name_file(generator, type, difficult, nitems, range):
    folder_name = f"{general.FOLDER_DATASET_GENERATED}_{util.get_info_time()}{SEPARATOR}{generator}"
    os.makedirs(folder_name, exist_ok=True)
    return (f"{folder_name}{SEPARATOR}t{type}_d{difficult}_n{nitems}_r{range}.dat")


def build_commnad_line_text_generate(
        generate,
        type,
        difficult,
        nitems,
        range,
        instance,
        S=1000):
    """
    type: 1=uncorrelated., 2=weakly corr., 3=strongly corr., 4=subset sum.
    difficult: difficult.
    nitems: number of items.
    range: range of coefficients.
    instance: instance no.
    S: number of tests in series (typically 1000).
    """
    return (str(nitems) + " " + str(range) + " " + str(type) +
            " " + str(instance) + " " + str(S) + " " +
            generate_full_name_file(generate, type, difficult, nitems, range))


def if_print_text(object, condition=True):
    if condition:
        print(object)


def get_info_dataset(knapsack):
    return (
        knapsack.file_name 
        + "  " + str(knapsack.n_items) 
        + "  " + str(knapsack.capacity) 
        + "  " + str(knapsack.objective) 
        + "  [" + str(knapsack.solution)[1:-1]+"]  "
    )

def get_solution_header(metaheuristic_list):
    n = len(metaheuristic_list)
    line = "\t\t\tDATASET\t\t\t ###"
    for i in range(n):
        line += "\tAlgorithm "+ metaheuristic_list[i].__class__.__name__ +"\t###"
    line+="\n file_name|n items|capacity|objective|solution"
    for i in range (n):
        line+="|success Rate|fitness average|standar deviation|best fitness|worst fitness|time average|###"
    return line