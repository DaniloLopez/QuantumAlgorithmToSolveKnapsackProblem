# -*- coding: utf-8 -*-
#!/usr/bin/env python3

#necessary packages
from modules.util.generalValue import SEPARATOR
import random
import numpy as np
import sys
import modules.util.util as util
import modules.util.generalValue as general
from modules.file.fileReader import FileReader
from time import time
from os import listdir, path
from modules.parameter.command_line import CommandLineArguments
from os import listdir
from modules.file.fileWriter import FileWriter
from modules.generator.datasetGenerator import DatasetGenerator

ROOT_DIR = path.dirname(path.abspath(__file__)) 

# listar las carpetas contenidas en el directorio raiz
list_folder_dataset_generated = listdir(general.FOLDER_DATASET_GENERATED)

param = CommandLineArguments(general.DESCRIPTION_TEXT, general.EPILOG_TEXT)
print(param)

obj_fileWriter=FileWriter()

def get_list_knapsack():
    knapsack_list = []
    for folder_name in list_folder_dataset_generated:
        root = general.FOLDER_DATASET_GENERATED + folder_name
        for file in util.get_list_files_folder( root ):
            #read knapsack file
            full_file_name = root + SEPARATOR + file
            file_reader = FileReader(full_file_name, file)
            knapsack = file_reader.get_knapsack()
            if knapsack is not None:
                knapsack_list.append(knapsack)
    return knapsack_list

def init_result_file():
    obj_fileWriter.open(util.get_result_file_name())
    obj_fileWriter.write(util.get_line_header(param.iterations))
    obj_fileWriter.new_line()

def run_metaheuristics(knapsack_list, metaheuristic_list, debug=False, deep_debug=False):
    try:        
        init_result_file()
        if debug:                
            print("Algorithm: ")            
        for my_metaheuristic in metaheuristic_list:
            if debug:           
                print("-------------------+----------------------------------")     
                print(my_metaheuristic)
            for knapsack in knapsack_list:
                if debug:
                    print("\n\t" + str(knapsack))
                list_fitness = []
                list_efos = []
                list_times = []
                times_found_ideal = 0
                for it in range(param.args.iterations):
                    random.seed(it)
                    start_time= time() #initial time                        
                    #invocation execute metaheuristic
                    my_metaheuristic.execute(knapsack, random, deep_debug)
                    elapsed_time = time() - start_time #final time
                    list_fitness.append (
                        my_metaheuristic.my_best_solution.fitness
                    )
                    list_efos.append(my_metaheuristic.current_efos)
                    list_times.append(elapsed_time)
                    substraction = (
                        my_metaheuristic.my_best_solution.fitness - 
                        knapsack.objective
                    )
                    if substraction < 1e-10 : 
                        times_found_ideal += 1                    
                
                line_result = (
                    util.get_line_result_format (
                        knapsack, [5], [5], times_found_ideal, 
                        param.args.iterations, list_times
                    )
                )
                
                obj_fileWriter.write_line(line_result)
    except OSError as err:
        print("OS error: {0}".format(err))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    finally:
        print("Execution finished.")
        obj_fileWriter.close()

def generate_dataset():
    """Generate dataset according to arguments of subcomnad generate"""
    generator = DatasetGenerator(param.args)
    print("> generating dataset...")
    generator.generate()
    print("> dataset generated.")    

def print_list_knapsack(list_knapsack):
    print("------------------------------------------------------\nknapsacks:")
    for i in list_knapsack:
        print(str(i))
    print("------------------------------------------------------")

def main ():
    list_knapsack = []
    print("running...")
    if param.is_generate(): #validate option generate
        generate_dataset()
    list_knapsack = get_list_knapsack() #extract dataset from files
    print("\n> run algorithms... ")
    run_metaheuristics(
        list_knapsack,
        general.LIST_METAHEURISTICS,
        debug=param.debug,
        deep_debug=param.debug
    )

if __name__ == '__main__':
    main()