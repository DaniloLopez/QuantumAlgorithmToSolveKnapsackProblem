# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from os import path
from modules.util.mainUtil import MainUtil
import modules.util.generalValue as general
from modules.generator.datasetGenerator import DatasetGenerator
from modules.algorithms.metaheuristics.simple_state.hillClimbing import HillClimbing
from modules.algorithms.metaheuristics.quantum.ibmQuantum import IbmQuantum

#root path of the project
ROOT_DIR = path.dirname(path.abspath(__file__))

def main ():
    print("<> running...")
    mainUtil = MainUtil()
    max_efos = 10000
    list_knapsack = []
    list_metaheuristics = [HillClimbing(max_efos), IbmQuantum(max_efos)]
    
    # ************************************************************************
    # generate dataset or extract it from files
    # ************************************************************************
    # set default path for generate dataset
    folder_dataset = general.FOLDER_DATASET_GENERATED
    # generate flag is present
    if(mainUtil.arguments.is_generate()):
         dataset_generator = DatasetGenerator(mainUtil.arguments)    
         folder_dataset = dataset_generator.generate()
    # get list of knapsack
    list_knapsack = mainUtil.get_knapsack_list(folder_dataset)
    print(folder_dataset)
    mainUtil.print_list_knapsack(list_knapsack)

    # ************************************************************************
    # run metaheuristic list for every knapsack in knapsack problem list
    # ************************************************************************
    mainUtil.init_result_file()
    print("<><> run algorithms...")
    mainUtil.run_metaheuristics(
        list_knapsack,
        list_metaheuristics,
        debug = mainUtil.arguments.is_debug_enable(),
        deep_debug = mainUtil.arguments.is_debug_enable()
    )
    print("<> execution finished.")

if __name__ == '__main__':
    main()