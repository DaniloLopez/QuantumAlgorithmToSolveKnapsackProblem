# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import sys
import os
from os import path
from modules.main.mainUtil import MainUtil
from modules.main.evaluate import Evaluate
import modules.util.generalValue as general
from modules.generator.datasetGenerator import DatasetGenerator
from modules.algorithms.metaheuristics.simple_state.hillClimbing import HillClimbing
from modules.algorithms.metaheuristics.quantum.ibmQuantumQAOA import IbmQuantumQAOA
from modules.algorithms.metaheuristics.quantum.ibmQuantumEigensolver import IbmQuantumEigensolver
from modules.algorithms.metaheuristics.population.slime_mould.slimeMould import SlimeMould
from modules.algorithms.metaheuristics.evolutionary.grey_wolf_optimizer.greyWolfOptimizer import GreyWolf
from modules.algorithms.metaheuristics.population.dragonfly.dragonfly import Dragonfly

# ****************************************************************************
# get root path of the project
# ****************************************************************************
ROOT_DIR = path.dirname(path.abspath(__file__))
ZERO_DOT_THREE = 0.3
POP_SIZE = 20
MAX_EFOS = 1000

def main ():
    """ 
    entry point to the program. algorithm in charge of evaluating the 
    proposed algorithms to solve one or more binary knapsack problems
    """
    # variables     
    list_knapsack = []
    
    list_metaheuristics = [
        SlimeMould(MAX_EFOS, POP_SIZE, ZERO_DOT_THREE),
        GreyWolf(MAX_EFOS, POP_SIZE),
        Dragonfly(MAX_EFOS, POP_SIZE),
        IbmQuantumEigensolver(MAX_EFOS),
        # IbmQuantumQAOA(MAX_EFOS),
        # HillClimbing(MAX_EFOS)
    ]
    
    main_util = MainUtil()
    # set default path for folder dataset
    folder_dataset = general.FOLDER_DATASET_GENERATED

    # ************************************************************************
    # generate dataset or extract it from files
    # ************************************************************************
    files_folder_default = general.FILES + general.SEPARATOR
    dataset_in_file = bool(main_util.arguments.get_file_name())

    # evaluate if must be generate dataset
    if main_util.arguments.is_generate():
        # generate dataset 
        dataset_generator = DatasetGenerator(main_util.arguments)
        folder_dataset = dataset_generator.generate()
        print(f"Dataset generated in folder:\n{folder_dataset}")
    
    # evaluate if dataset is in a folder
    elif main_util.arguments.get_folder_name():
        folder_name = main_util.arguments.get_folder_name()
        exist_in_default_folder = os.path.isdir(
            files_folder_default + folder_name
        )
        if os.path.isdir(folder_name) or exist_in_default_folder:
            folder_dataset = (
                (general.DIR_FILES + folder_name)
                if exist_in_default_folder 
                else folder_name
            )
            if not next(os.scandir(folder_dataset), None):
                sys.exit("Error: Folder is empty")
        else:
            sys.exit("Error: Folder does not exists")

    # evaluate if problem is in a file
    elif dataset_in_file:
        file_name = main_util.arguments.get_file_name()
        exist_in_default_folder = path.exists( files_folder_default + file_name)
        if path.exists(file_name) or exist_in_default_folder:
            try:
                file_path = (
                    (files_folder_default + file_name)
                    if exist_in_default_folder 
                    else file_name
                )
                file = open(file_path)
                file.close()
                file_name = file_path.split(general.SEPARATOR)
                knapsack_from_file = main_util.get_knapsack(
                    file_path, file_name=file_name[-1]
                )
                if knapsack_from_file:
                    list_knapsack.append(knapsack_from_file)
            except FileNotFoundError:
                sys.exit('Error: Value of the -fl flag argument does not correspond to a valid file')
        else:
            sys.exit("Error: File does not exists")

    # get knapsack list from dataset folder name
    if not list_knapsack:
        list_knapsack = main_util.get_knapsack_list(folder_dataset)
    if main_util.arguments.debug:
        print("--- ::: " +folder_dataset)
        main_util.print_list(list_knapsack)
    # ************************************************************************

    # ************************************************************************
    # run metaheuristic list for every knapsack in knapsack problem list
    # ************************************************************************
    evaluate = Evaluate()
    print("<-><-> run algorithms...")
    evaluate.run_metaheuristics(
        list_knapsack,  
        list_metaheuristics,
        debug = main_util.arguments.is_debug_enable(),
        deep_debug = main_util.arguments.is_debug_enable()
    )
    # ************************************************************************
    print("<> execution finished.")

if __name__ == '__main__':
    main()