# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from os import path
from modules.util.mainUtil import MainUtil
import modules.util.generalValue as general
from modules.generator.datasetGenerator import DatasetGenerator
from modules.algorithms.metaheuristics.simple_state.hillClimbing import HillClimbing
from modules.algorithms.metaheuristics.quantum.ibmQuantum import IbmQuantum
from modules.algorithms.metaheuristics.population.slime_mould.slimeMould import SlimeMould

# ****************************************************************************
# get root path of the project
# ****************************************************************************
ROOT_DIR = path.dirname(path.abspath(__file__))
ZERO_DOT_THREE = 0.3
POP_SIZE = 10
MAX_EFOS = 10000

def main ():
    """ 
    entry point to the program. algorithm in charge of evaluating the 
    proposed algorithms to solve one or more binary knapsack problems
    """
    # variables     
    list_knapsack = []
    
    list_metaheuristics = [
        SlimeMould(MAX_EFOS, POP_SIZE, ZERO_DOT_THREE), 
        #IbmQuantum(MAX_EFOS), 
        HillClimbing(MAX_EFOS)
    ]
    
    main_util = MainUtil()
    # set default path for folder dataset
    folder_dataset = general.FOLDER_DATASET_GENERATED

    # ************************************************************************
    # generate dataset or extract it from files
    # ************************************************************************
    if main_util.arguments.is_generate():
        # generate dataset 
        dataset_generator = DatasetGenerator(main_util.arguments)
        folder_dataset = dataset_generator.generate()
    # get knapsack list from dataset folder name
    list_knapsack = main_util.get_knapsack_list(folder_dataset)
    if main_util.arguments.debug:
        print("--- ::: " +folder_dataset)
        main_util.print_list(list_knapsack)
    # ************************************************************************

    # ************************************************************************
    # run metaheuristic list for every knapsack in knapsack problem list
    # ************************************************************************
    main_util.init_result_file()
    print("<-><-> run algorithms...")    
    main_util.run_metaheuristics(
        list_knapsack,  
        list_metaheuristics,
        debug = main_util.arguments.is_debug_enable(),
        deep_debug = main_util.arguments.is_debug_enable()
    )
    # ************************************************************************
    print("<> execution finished.")

if __name__ == '__main__':
    main()