# -*- coding: utf-8 -*-
#!/usr/bin/python

#necessary packages 
from qiskit.aqua.input import EnergyInput
from qiskit.aqua.algorithms import ExactEigensolver
from time import time
from datetime import datetime
from os import scandir, getcwd, listdir

import modules.util.util as util
from modules.knapsack.knapsack import Knapsack
from modules.file.fileWriter import FileWriter
import modules.file.fileReader as fileReader
import modules.quantum.quantum as quantum
import numpy as np

obj_fileWriter  = FileWriter()
# obj_fileWriter.open(str(util.get_result_file_name()))
num_iterations = 20

FOLDER_DATASET_FN = "files/dataset_fn/"

FOLDER_DATASET_GENERATED = "files/generated_dataset/"
#FOLDER_DATASET_GENERATED = "files/generated_dataset_complete"

FOLDER_DATASET_GEN_EASY = "easy"
FOLDER_DATASET_GEN_MEDIUM = "medium"
FOLDER_DATASET_GEN_HARD = "hard"

files_fn = ["f3.txt", "f2.txt", "f8.txt", "f6.txt", "f9.txt", "f5.txt",  "f11.txt", "f10.txt", "f4.txt", "f7.txt", "f1.txt"]

def get_list_files_folder(ruta = getcwd()):
    """lista los archivos existentes en una ruta determinada"""
    return [arch.name for arch in scandir(ruta) if arch.is_file()]

# listar las carpetas contenidas en el directorio
list_folder_dataset_generated = listdir(FOLDER_DATASET_GENERATED)

def complete_objetive_and_solution():
    for folder_name in list_folder_dataset_generated:
        list_files = get_list_files_folder(FOLDER_DATASET_GENERATED + folder_name)
        for i in list_files:
            obj_kp = fileReader.read_file_knapsack_generate_pisinger(FOLDER_DATASET_GENERATED + folder_name + "/" + i) 
            #print(obj_kp)

#complete_objetive_and_solution()

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
            num_exact_solution = 0        
            time_sum = 0

            obj_kp = fileReader.read_file_knapsack(name_file)        
            print(obj_kp)
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
                num_exact_solution += 1 if obj_kp.is_equal_solution(result_solution.tolist()) else 0                     
                
            line_result = util.get_line_result_format(obj_kp, profits_solution, weigths_solution, num_exact_solution, num_iterations, times)        
            obj_fileWriter.write(line_result)
            obj_fileWriter.new_line()
except OSError:
    print("execution error")
finally:
    print("execution finished")
    obj_fileWriter.close()

