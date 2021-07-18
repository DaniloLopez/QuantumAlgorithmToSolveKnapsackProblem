# -*- coding=utf-8 -*-

#from modules.algorithms.metaheuristics.quantum_based.ibmQuantum import IbmQuantum
#from modules.algorithms.metaheuristics.simple_state.hillClimbing import HillClimbing
from modules.util.util import get_separator, get_project_root

FILES = "files"
DIR_FILES = str(get_project_root()) + get_separator() + FILES + get_separator()

#DESCRIPTION
DESCRIPTION_TEXT = "This program execute and analize a set of data with "\
    "information about a knapsack every file; the information of a file is "\
    "read and with an algorithm that emaule the functionality of a quantum "\
    "computer."
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
SUBCOMANDS = "subcomands"
CMD_GENERATE = "generate"
CMDH_GENERATE = "generate dataset "

ARG_I = "-i"
ARG_ITERATION = "--iterations"
ARGH_ITERATION = "Number of iterations to run each file with a knapsack"

ARG_T = "-t"
ARG_TYPE = "--type"
ARGH_TYPE = "Indicate type of correlation between items."

ARG_D = "-d"
ARG_DIFFICULT = "--difficult"
ARGH_DIFFICULT = "Indicate difficult of generated dataset (1=Easy, 2=Medium, "\
    "3=Hard, 0=All options)."

ARG_N = "-n"
ARG_NITEMS = "--nitems"
ARGH_NITEMS = "Indicate quantity o items stored in knapsack"

ARG_R = "-r"
ARG_RANGE = "--range"
ARGH_RANGE = "Indicate range of creation for dataset."

ARG_G = "-g"
ARG_GENERATE = "--generate"
ARGH_GENERATE = "To generate dataset according to input parameters.\nT=Type "\
    + ARGH_TYPE + "\nD=Difficult " + ARGH_DIFFICULT + "\nN=N_Items "\
    + ARGH_NITEMS + "\nR=Range " + ARGH_RANGE

ARG_FL = "-fl"
ARG_FILE = "--file"
ARGH_FILE="Indicate file with content of a knapsack to make evaluation.\n"\
    "Default root folder where the dataset is stored is "\
    "[rootProject/files/folder] or provide the full address"

ARG_FD = "-fd"
ARG_FOLDER = "--folder"
ARGH_FOLDER = "Indicate folder with knapsack files to make evaluation."\
    "Default root folder is [rootProject/files/folder] or provide the "\
    "full address "