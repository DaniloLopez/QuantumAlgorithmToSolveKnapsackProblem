# -*- coding=utf-8 -*-

#from modules.algorithms.metaheuristics.quantum_based.ibmQuantum import IbmQuantum
#from modules.algorithms.metaheuristics.simple_state.hillClimbing import HillClimbing
from modules.util.util import get_separator, get_project_root

DIR_FILES = str(get_project_root()) + get_separator() + "files" + get_separator()

#DESCRIPTION
DESCRIPTION_TEXT = "This program execute and analize a set of data with information about a knapsack every file; the information of a file is read and with an algorithm that emaule the functionality of a quantum computer."
EPILOG_TEXT="Author: Danilo López - dlopezs@unicauca.edu.co"

#GLOBAL VARIABLES
DATASET_FN = "dataset_fn"
GENERATED_DATASET = "generated_dataset_complete"
NUM_ITERATIONS_STATIC = 20
FOLDER_DATASET_FN = DIR_FILES + DATASET_FN + get_separator()
FOLDER_DATASET_GENERATED = DIR_FILES + GENERATED_DATASET + get_separator()
#METAHEURISTIC_LIST = [IbmQuantum(20)]

FOLDER_DATASET_GEN_EASY = "easy"
FOLDER_DATASET_GEN_MEDIUM = "medium"
FOLDER_DATASET_GEN_HARD = "hard"

# Name of algorithms executable
EXEC_EASY_KP_GEN = "easy"
EXEC_MEDIUM_KP_GEN = "medium"
EXEC_HARD_KP_GEN = "hard"

# Folder name of dataset
FOLDER_EASY_INSTANCE = "easy"
FOLDER_MEDIUM_INSTANCE = "medium"
FOLDER_HARD_INSTANCE = "hard"

#GLOBAL GENERAL VARIABLES 
ZERO_CHAR = "0"
PROGRAM_NAME = "main"

#VARIABLES FOR PARAMETERS MENU
ARG_I = "-i"
ARG_ITERATION = "--iterations"
ARGH_ITERATION = "Number of iterations to run each file with a knapsack"

ARG_F = "-f"
ARG_FUNCTION = "--function"
ARGH_FUNCTION = "Defines functionality to run. \n1) Generate dataset "\
    "2) Evaluate dataset, 3) Generate and evaluate dataset)"

ARG_T = "-t"
ARG_TYPE = "--type"
ARGH_TYPE = "Indicate type of correlation between items. value should "\
    "be an integer number."

ARG_D = "-d"
ARG_DIFFICULT = "--difficult"
ARGH_DIFFICULT = "Indicate difficult of generated dataset (1=Easy, 2=Medium, "\
    "3=Hard, 0=All options)."

ARG_N = "-n"
ARG_NITEMS = "--nitems"
ARGH_NITEMS = "Indicate quantity o fitems stored in knapsack. value should "\
    "be an integer number."

ARG_R = "-r"
ARG_RANGE = "--range"
ARGH_RANGE = "Indicate range to create every file."

ARG_FL = "-fl"
ARG_FILE = "--file"
ARGH_FILE="Indicate file with content of a knapsack to make evaluationself."\
    "Folder root fodler default to dataset is [rootProject/files/folder] or "\
    "provide the full address"

ARG_FD = "--fd"
ARG_FOLDER = "--folder"
ARGH_FOLDER = "Indicate folder with knapsack files to make evaluation."\
    "Folder root folder default is [rootProject/files/folder] or provide the "\
    "full address "