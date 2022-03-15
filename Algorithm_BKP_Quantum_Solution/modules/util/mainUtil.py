from os import listdir
from modules.file.fileWriter import FileWriter
from modules.util.arguments.arguments_command_line import ArgumentsCommandLine
from modules.generator.datasetGenerator import DatasetGenerator
import modules.util.generalValue as general
from time import time
import random
from modules.util.generalValue import SEPARATOR
import modules.util.util as util
from modules.file.fileReader import FileReader
import sys

class MainUtil():
    def __init__(self):
        self.obj_fileWriter=FileWriter()
        self.arguments = ArgumentsCommandLine(
            general.DESCRIPTION_TEXT, 
            general.EPILOG_TEXT
        )
        print(self.arguments)
        self.init_result_file()
        pass

    def get_knapsack_list(self, knapsack_files_path):
        knapsack_list = []
        # list the folders contained in the root directory
        list_folder_dataset_generated = listdir(knapsack_files_path)
        for folder_name in list_folder_dataset_generated:
            root_path = knapsack_files_path + folder_name
            for knapsack_file_name in util.get_list_files_folder( root_path ):
                #read knapsack file
                full_file_path = root_path + SEPARATOR + knapsack_file_name
                reader_knapsack_file = FileReader(
                    full_file_path, 
                    knapsack_file_name
                )
                knapsack = reader_knapsack_file.get_knapsack()
                if knapsack is not None:
                    knapsack_list.append(knapsack)
        return knapsack_list

    def init_result_file(self):
        self.obj_fileWriter.open(util.get_result_file_name())
        self.obj_fileWriter.write(
            util.get_line_header(self.arguments.get_iterations())
        )
        self.obj_fileWriter.new_line()

    def run_metaheuristics(
        self, 
        knapsack_list, 
        metaheuristic_list, 
        debug=False, 
        deep_debug=False
    ):
        try:  
            self.obj_fileWriter.write_line(
                util.get_solution_header(metaheuristic_list)
            )
            for knapsack in knapsack_list:
                util.if_print_text("\n\t" + str(knapsack), debug)
                self.obj_fileWriter.write(util.get_info_dataset(knapsack))                
                for my_metaheuristic in metaheuristic_list:
                    list_fitness = []
                    list_efos = []
                    list_times = []
                    times_found_ideal = 0          
                    util.if_print_text(my_metaheuristic, debug)
                    #self.obj_fileWriter.write("*"+ str(my_metaheuristic))
                    for it in range(self.arguments.get_iterations()):
                        random.seed(it)                        
                        start_time= time() # initial time record
                        
                        # invocation execute metaheuristic
                        my_metaheuristic.execute(knapsack, random, deep_debug)
                        
                        elapsed_time = time() - start_time # end time record
                        list_fitness.append (
                            my_metaheuristic.my_best_solution.fitness
                        )
                        list_efos.append(my_metaheuristic.current_efos)
                        list_times.append(elapsed_time)                    
                        substraction = (
                            my_metaheuristic.my_best_solution.fitness
                            - knapsack.objective
                        )
                        if substraction < 1e-10 : 
                            times_found_ideal += 1
                            
                    self.obj_fileWriter.write(
                        util.get_line_result_format (
                            knapsack, 
                            list_fitness, 
                            list_efos, 
                            list_times, 
                            times_found_ideal, 
                            self.arguments.get_iterations(),
                            my_metaheuristic.my_best_solution
                        )
                    )
                    util.if_print_text(
                        "\t" + str(my_metaheuristic.my_best_solution), 
                        debug
                    )
                self.obj_fileWriter.write_line("")
        except OSError as err:
            print("OS error: {0}".format(err))
        except BaseException as e:
            print("Unexpected error: {}".format(e))
            raise
        finally:        
            self.obj_fileWriter.close()

    def generate_dataset(self, arguments):
        """Generate dataset according to arguments of subcomand generate"""        
        generator = DatasetGenerator(arguments)
        # generating dataset...
        generator.generate()
        print("--------------------------------------------------------------")
        print("------- ::: DATASET GENERATED ::: ----------------------------")
        print("--------------------------------------------------------------")

    def print_list(self, list):
        print("--------------------------------------------------------------")
        print("------- ::: LIST{ length : " +str(len(list))+ " } ::: --------")
        for i in list:
            print(str(i))
        print("------- ::: END LIST ::: -------------------------------------")
        print("--------------------------------------------------------------")