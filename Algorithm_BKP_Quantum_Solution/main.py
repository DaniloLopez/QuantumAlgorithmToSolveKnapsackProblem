# -*- coding: utf-8 -*-
#!/usr/bin/env python3

#necessary packages
import random
import numpy as np
import modules.util.util as util
import modules.util.generalValue as general
from modules.file.fileReader import FileReader
from time import time
from os import listdir, path
from modules.parameter.command_line import CommandLineParameter
from os import scandir, getcwd, listdir
from modules.file.fileWriter import FileWriter
from modules.generator.datasetGenerator import DatasetGenerator

# Manage list directory
ROOT_DIR = path.dirname(path.abspath(__file__)) 

# listar las carpetas contenidas en el directorio raiz
list_folder_dataset_generated = listdir(general.FOLDER_DATASET_GENERATED)

# instance to manage program parameters
param = CommandLineParameter(general.DESCRIPTION_TEXT, general.EPILOG_TEXT)
print(param)


obj_fileWriter=FileWriter()

#instance to manage dataset generator program
generator = DatasetGenerator(1000)

def get_knapsack_list():
    knapsack_list = []
    for folder_name in list_folder_dataset_generated:
        root = general.FOLDER_DATASET_GENERATED + folder_name
        for file in util.get_list_files_folder( root ):
            #read knapsack file
            file_name = root + util.get_separator() + file
            file_reader = FileReader(file_name)
            knapsack = file_reader.get_knapsack()
            if knapsack is not None:
                knapsack_list.append(knapsack)
    return knapsack_list

def init_result_file():
    obj_fileWriter.open(util.get_result_file_name())
    obj_fileWriter.write(util.get_line_header(param.iterations))
    obj_fileWriter.new_line()

def run_metaheuristics(knapsack_list):
    try:        
        init_result_file()
        for my_metaheuristic in general.METAHEURISTIC_LIST:
            for knapsack in knapsack_list:
                times = []
                list_fitness = []
                list_efos = []
                list_times = []
                times_found_ideal = 0
                
                for it in range(num_iterations):
                    start_time= time() #initial time                        
                    #invocation execute metaheuristic
                    my_metaheuristic.execute(knapsack, random.seed(it)) 
                    elapsed_time = time() - start_time #final time
                    list_fitness.append (
                        my_metaheuristic.my_best_solution.objetive
                    )
                    list_efos.append(my_metaheuristic.current_efos)
                    list_times.append(elapsed_time - start_time)
                    resto = (
                        my_metaheuristic.my_best_solution.objetive - 
                        knapsack.objetive
                    )
                    if (resto < 1e-10 ): 
                        times_found_ideal += 1                    
                line_result = util.get_line_result_format (
                    knapsack, [5], [5], times_found_ideal, 
                    num_iterations, times
                )
                obj_fileWriter.write_line(line_result)
    except OSError:
        print("Execution error")
    finally:
        print("Execution finished")
        obj_fileWriter.close()


def main ():
    knapsack_list = []
    print("running...")
    #generate dataset acording to arguments of subcomnad generate
    if param.is_generate():
        print("generating dataset...")
        #generator.generarDataset(param.args)
        print("dataset generated.")
    
    print("\nrun algorithm")
    knapsack_list = get_knapsack_list() #knapsack list
    #run_metaheuristics(knapsack_list)
    for i in knapsack_list:
        print(i)

if __name__ == '__main__':
    main()