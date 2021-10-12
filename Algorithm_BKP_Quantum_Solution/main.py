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

def main ():
    """ 
    entry point to the program. algorithm in charge of evaluating the 
    proposed algorithms to solve one or more binary knapsack problems
    """
    # variables 
    max_efos = 10000
    list_knapsack = []
    slimeMould = SlimeMould(max_efos)
    slimeMould.setPopSize = 10
    list_metaheuristics = [slimeMould]
    mainUtil = MainUtil()
    # set default path for folder dataset
    folder_dataset = general.FOLDER_DATASET_GENERATED

    # ************************************************************************
    # generate dataset or extract it from files
    # ************************************************************************
    if(mainUtil.arguments.is_generate()):
        # generate dataset 
        dataset_generator = DatasetGenerator(mainUtil.arguments)
        folder_dataset = dataset_generator.generate()
    # get knapsack list from dataset folder name
    list_knapsack = mainUtil.get_knapsack_list(folder_dataset)
    if mainUtil.arguments.debug or True:
        print("--- ::: " +folder_dataset)
        mainUtil.print_list(list_knapsack)
    # ************************************************************************

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
    # ************************************************************************
    print("<> execution finished.")

if __name__ == '__main__':
    main()