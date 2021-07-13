# -*- coding: utf-8 -*-
#!/usr/bin/python

#necessary packages
import numpy as np
import modules.util.util as util
import modules.util.generalValue as general
import modules.file.fileReader as fileReader
from time import time
from os import listdir, path
from modules.menu.menu import Menu
from os import scandir, getcwd, listdir
from modules.file.fileWriter import FileWriter
from modules.generator.datasetGenerator import DatasetGenerator
from modules.evaluator.datasetEvaluator import DatasetEvaluator



# Manage list directory
ROOT_DIR = path.dirname(path.abspath(__file__)) 

# listar las carpetas contenidas en el directorio raiz
list_folder_dataset_generated = listdir(general.FOLDER_DATASET_GENERATED)

# instance to manage program menu
menu = Menu(general.DESCRIPTION_TEXT, general.EPILOG_TEXT)

##num iterations, 20 by default
num_iterations=int(menu.getIterations()) if (
    menu.getIterations() is not None) else general.NUM_ITERATIONS_STATIC
obj_fileWriter=FileWriter()

#instance to manage program generator dataset
generator = DatasetGenerator(1000)
#instance to manage program evaluator dataset
evaluator = DatasetEvaluator()

def get_list_files_folder(ruta = getcwd()):
    """lista los archivos existentes en una ruta determinada"""
    return [arch.name for arch in scandir(ruta) if arch.is_file()]

def complete_objetive_and_solution():
    for folder_name in list_folder_dataset_generated:
        list_files = get_list_files_folder (
            general.FOLDER_DATASET_GENERATED + folder_name
        )
        print(list_files)
        for i in list_files:
            obj_kp = fileReader.read_file_knapsack (
                general.FOLDER_DATASET_GENERATED + 
                folder_name + util.get_separator() + i
            ) 
            print(obj_kp)
"""
if(menu.is_generated_data()):
    #generator.generate()
    print("Successfully generated dataset")

if(menu.is_evaluate_data()):
    #evaluator.evaluate()
    print("Successfully evaluated dataset")
    
if(menu.is_generate_evaluate()):
    #generator.generate()
    #evaluator.evaluate()
    print("Successfully generated and evaluate dataset")
"""



def run_metaheuristic():
    try:
        obj_fileWriter.open(util.get_result_file_name())
        obj_fileWriter.write(util.get_line_header(num_iterations))
        obj_fileWriter.new_line()
        for my_metaheuristic in general.MH_LIST:
            for folder_name in list_folder_dataset_generated:
                list_files = get_list_files_folder (
                    general.FOLDER_DATASET_GENERATED + folder_name
                )
                for file in list_files:
                    times = []
                    name_file = (
                        general.FOLDER_DATASET_GENERATED + folder_name +
                        util.get_separator() + file
                    )
                    obj_kp = fileReader.read_file_knapsack(name_file)                            
                    list_fitness = []
                    list_efos = []
                    list_times = []
                    times_found_ideal = 0
                    for it in range(num_iterations):  
                        start_time= time() #initial time                        
                        #invocation execute metaheuristic
                        my_metaheuristic.execute(obj_kp, np.random.seed(it)) 
                        elapsed_time = time() - start_time #final time
                        list_fitness.append (
                            my_metaheuristic.my_best_solution.fitness
                        )
                        list_efos.append(my_metaheuristic.current_efos)
                        list_times.append(elapsed_time - start_time)
                        times_found_ideal += (
                            1 if (
                                    my_metaheuristic.my_best_solution.fitness - 
                                    obj_kp.objetive
                                ) < 1e-10
                            else 0
                        )
                    line_result = util.get_line_result_format (
                        obj_kp, [5], [5], times_found_ideal, 
                        num_iterations, times
                    )
                    obj_fileWriter.write(line_result)
                    obj_fileWriter.new_line()
    except OSError:
        print("Execution error")
    finally:
        print("Execution finished")
        obj_fileWriter.close()

#program init
print("running...")
#complete_objetive_and_solution()
run_metaheuristic()
