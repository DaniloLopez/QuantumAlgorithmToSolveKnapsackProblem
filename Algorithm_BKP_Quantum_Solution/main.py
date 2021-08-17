# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from os import path
from modules.util.mainUtil import MainUtil
import modules.util.generalValue as general
from modules.generator.datasetGenerator import DatasetGenerator
from modules.algorithms.metaheuristics.simple_state.hillClimbing import HillClimbing
from modules.algorithms.metaheuristics.quantum_based.ibmQuantum import IbmQuantum

#root path of the project
ROOT_DIR = path.dirname(path.abspath(__file__))

def main ():
    print("<> running...")
    mu = MainUtil()
    max_efos = 10000
    list_knapsack = []
    list_metaheuristics = [HillClimbing(max_efos), IbmQuantum(max_efos)]
    
    #extract dataset from files
    folder_dataset = general.FOLDER_DATASET_GENERATED
    if(mu.arguments.is_generate()):
         dataset_generator = DatasetGenerator(mu.arguments)    
         folder_dataset = dataset_generator.generate()
    list_knapsack = mu.get_knapsack_list(folder_dataset)
    print(folder_dataset)
    mu.print_list_knapsack(list_knapsack)

    mu.init_result_file()
    print("<><> run algorithms...")
    mu.run_metaheuristics(
        list_knapsack,
        list_metaheuristics,
        debug = mu.arguments.is_debug_enable(),
        deep_debug = mu.arguments.is_debug_enable()
    )
    print("<> execution finished.")

if __name__ == '__main__':
    main()

