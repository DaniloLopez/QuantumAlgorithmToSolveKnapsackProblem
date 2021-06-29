# -*- coding: utf-8 -*-
#!/usr/bin/python

#necessary packages 

import argparse

DESCRIPTION_TEXT = "This program execute and analize a set of data with information about a knapsack every file; the information of a file is read and with an algorithm that emaule the functionality of a quantum computer"

parser = argparse.ArgumentParser(description=DESCRIPTION_TEXT)
parser.add_argument("-i", "--iterations", help="Number of iterations to run each file with a knapsack")
args = parser.parse_args()

num_iterations = 0

if args.iterations:
    num_iterations = int(args.iterations)
else:
    num_iterations = 20

#necessary packages 
from qiskit.aqua.input import EnergyInput
from qiskit.aqua.algorithms import ExactEigensolver
from time import time
from datetime import datetime
from os import scandir, getcwd, listdir

import modules.util.util as util
from modules.knapsack.knapsack import Knapsack

from modules.menu.menu import Menu
import modules.util.generalValue as general
from modules.generator.datasetGenerator import DatasetGenerator
from modules.evaluator.datasetEvaluator import DatasetEvaluator



from modules.file.fileWriter import FileWriter
from os import listdir, path

# Manage list directory
ROOT_DIR = path.dirname(path.abspath(__file__))
list_folder_dataset_generated = listdir(ROOT_DIR + general.FOLDER_DATASET_GENERATED)
print(ROOT_DIR)
print(ROOT_DIR + general.FOLDER_DATASET_GENERATED)


files_fn = ["f3.txt", "f2.txt", "f8.txt", "f6.txt", "f9.txt", "f5.txt",  "f11.txt", "f10.txt", "f4.txt", "f7.txt", "f1.txt"]

def get_list_files_folder(ruta = getcwd()):
    """lista los archivos existentes en una ruta determinada"""
    return [arch.name for arch in scandir(ruta) if arch.is_file()]

# listar las carpetas contenidas en el directorio
list_folder_dataset_generated = listdir(FOLDER_DATASET_GENERATED)

def complete_objetive_and_solution():
    for folder_name in list_folder_dataset_generated:
        list_files = get_list_files_folder(FOLDER_DATASET_GENERATED + folder_name)
        print(list_files)
        for i in list_files:
            obj_kp = fileReader.read_file_knapsack(FOLDER_DATASET_GENERATED + folder_name + "/" + i) 
            print(obj_kp)

complete_objetive_and_solution()

menu = Menu(general.DESCRIPTION_TEXT, general.EPILOG_TEXT) # instance to manage program menu
obj_fileWriter  = FileWriter()

num_iterations = int(menu.getIterations()) if (menu.getIterations() is not None) else general.NUM_ITERATIONS_STATIC

run_quantum_algorithm()

#instance to manage program generator dataset
generator = DatasetGenerator(1000)

#instance to manage program evaluator dataset
evaluator = DatasetEvaluator()

if(menu.is_generated_data()):
    generator.generate()
    print("Successfully generated dataset")

if(menu.is_evaluate_data()):
    #evaluator.evaluate()
    print("Successfully evaluated dataset")
    
if(menu.is_generate_evaluate()):
    #generator.generate()
    #evaluator.evaluate()
    print("Successfully generated and evaluate dataset")

def run_quantum_algorithm():
    try:
        print("running...")
        obj_fileWriter.open(util.get_result_file_name())
        obj_fileWriter.write(util.get_line_header(num_iterations))
        obj_fileWriter.new_line()
        for folder_name in list_folder_dataset_generated:
            list_files = get_list_files_folder(FOLDER_DATASET_GENERATED + folder_name)
            for file in list_files:
                M = 2000000
                profits_solution = []
                weigths_solution = []
                times = []
                name_file = FOLDER_DATASET_GENERATED + folder_name + "/" + file
                print(name_file)
                cant_best_solution_found = 0        
                time_sum = 0

                obj_kp = fileReader.read_file_knapsack(name_file)        
                print(obj_kp)
                result_solution = None
                for it in range(num_iterations):  
                    #get isntances of Pauli operator for ExactEigensolver      
                    qubitOp, offset = quantum.get_knapsack_qubitops(obj_kp.get_profits(), obj_kp.get_weigths(), 
                                                                    obj_kp.get_capacity(), M )
                    algo_input = EnergyInput(qubitOp)
                    ee = ExactEigensolver(qubitOp, k=1) #instance of exactEigensolver
                    start_time= time() #initial time
                    result = ee.run() #Run quantum algorithm
                    elapsed_time = time() - start_time #final time
                    time_sum += elapsed_time
                    times.append(elapsed_time)
                    
                    most_lightly = result['eigvecs'][0] #format result
                    x = quantum.sample_most_likely(most_lightly)
                    result_solution = x[:len(obj_kp.get_profits())]

                    v , w =  obj_kp.calculate_knapsack_value_weight(result_solution)
                    profits_solution.append(v)
                    weigths_solution.append(w)
                    
                    cant_best_solution_found += 1 if (v >= obj_kp.objetive and w <= obj_kp.capacity) else 0                     
                
                va , wa =  obj_kp.calculate_knapsack_value_weight(result_solution)
                print(result_solution , end="")
                print(f" profit: {va}  weight: {wa}\n")

                line_result = util.get_line_result_format(obj_kp, profits_solution, weigths_solution, cant_best_solution_found, num_iterations, times)        
                obj_fileWriter.write(line_result)
                obj_fileWriter.new_line()
    except OSError:
        print("Execution error")
    finally:
        print("Execution finished")
        obj_fileWriter.close()