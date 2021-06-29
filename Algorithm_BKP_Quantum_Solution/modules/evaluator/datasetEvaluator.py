# -*- coding: utf-8 -*-
#!/usr/bin/python

from qiskit.aqua.input import EnergyInput
from qiskit.aqua.algorithms import ExactEigensolver
import modules.quantum.quantum as quantum

from time import time
from datetime import datetime

from modules.file.fileWriter import FileWriter
import modules.util.generalValue as general
import modules.util.util as util

class DatasetEvaluator():

    def __init__(self):
        self.obj_fileWriter  = FileWriter()

    def evaluate(self, num_iterations):
        try:
            print("Running evaluation...")
            self.obj_fileWriter.open(util.get_result_file_name())
            self.obj_fileWriter.write(util.get_line_header(num_iterations))
            self.obj_fileWriter.new_line()

            for folder_name in general.list_folder_dataset_generated:
                list_files = util.get_list_files_folder(general.FOLDER_DATASET_GENERATED + folder_name)
                for file in list_files:            
                    profits_solution = []
                    weigths_solution = []
                    times = []
                    name_file = general.FOLDER_DATASET_GENERATED + folder_name + "/" + file
                    print(name_file)
                    num_exact_solution = 0        
                    time_sum = 0

                    obj_kp = self.fileReader.read_file_knapsack(name_file) 
                    print(obj_kp)
                    result_solution = None
                    print(num_iterations)
                    for it in range(num_iterations):  
                        #get isntances of Pauli operator for ExactEigensolver      
                        qubitOp, offset = quantum.get_knapsack_qubitops(obj_kp.get_profits(), obj_kp.get_weigths(), 
                                                                        obj_kp.get_capacity(), general.M )
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
                        
                        #si solucion tiene un valor mayor o igual que el profit 
                        num_exact_solution += 1 if obj_kp.is_equal_solution(result_solution.tolist()) else 0                     
                    
                    va , wa =  obj_kp.calculate_knapsack_value_weight(result_solution)
                    print(result_solution , end="")
                    print(f" profit: {va}  weight: {wa}\n")

                    line_result = util.get_line_result_format(obj_kp, profits_solution, weigths_solution, num_exact_solution, num_iterations, times)        
                    self.obj_fileWriter.write(line_result)
                    self.obj_fileWriter.new_line()
        except OSError:
            print("execution error")
        finally:
            print("execution finished")
            self.obj_fileWriter.close()
