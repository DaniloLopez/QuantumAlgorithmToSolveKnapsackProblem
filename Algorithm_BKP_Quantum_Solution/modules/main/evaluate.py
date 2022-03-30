from modules.file.fileWriter import FileWriter
from modules.arguments.arguments_command_line import ArgumentsCommandLine
import modules.util.generalValue as general
from time import time
import random
import modules.util.util as util

class Evaluate():
    def __init__(self):
        self.obj_fileWriter=FileWriter()
        self.obj_fileWriter_fitness=FileWriter()
        self.arguments = ArgumentsCommandLine(
            general.DESCRIPTION_TEXT, 
            general.EPILOG_TEXT
        )
        self.init_result_file()
        pass

    def init_result_file(self):
        name = util.get_result_file_name()
        self.obj_fileWriter.open(name)
        self.obj_fileWriter.write(
            util.get_line_header(self.arguments.get_iterations())
        )
        self.obj_fileWriter.new_line()

        self.obj_fileWriter_fitness.open(f"{name.split('.')[0]}_fitness.csv")
        self.obj_fileWriter_fitness.write(
            util.get_line_header(self.arguments.get_iterations())
        )
        self.obj_fileWriter_fitness.new_line()

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
            self.obj_fileWriter_fitness.write_line(
                "FileName,Objective,Slime_mould,Grey_wolf,Dragon_fly,QuantumEigensolver"
            )
            for knapsack in knapsack_list:
                print(knapsack.file_name)
                util.if_print_text("\n\t" + str(knapsack), debug)
                self.obj_fileWriter.write(util.get_info_dataset(knapsack) + " ### ")
                self.obj_fileWriter_fitness.write(f"{knapsack.file_name},{knapsack.objective},")

                for my_metaheuristic in metaheuristic_list:
                    print(my_metaheuristic.__class__.__name__)
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
                            knapsack.objective
                            - my_metaheuristic.my_best_solution.fitness
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
                    self.obj_fileWriter_fitness.write(
                        f"{sum(list_fitness) / len(list_fitness)},"
                    )
                    util.if_print_text(
                        "\t" + str(my_metaheuristic.my_best_solution), 
                        debug
                    )
                self.obj_fileWriter.write_line("")
                self.obj_fileWriter_fitness.write_line("")
        except OSError as err:
            print("OS error: {0}".format(err))
        except BaseException as e:
            print(f"Unexpected error: {e}")
            raise
        finally:        
            self.obj_fileWriter.close()