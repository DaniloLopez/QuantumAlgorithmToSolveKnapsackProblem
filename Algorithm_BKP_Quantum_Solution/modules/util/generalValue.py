from modules.algorithms.metaheuristics.quantum_based.ibmQuantum import IbmQuantum
from modules.algorithms.metaheuristics.simple_state.hillClimbing import HillClimbing
from modules.util.util import get_separator, get_project_root


DIR_FILES = str(get_project_root()) + get_separator() + "files" + get_separator()

#DESCRIPTION
DESCRIPTION_TEXT = "This program execute and analize a set of data with information about a knapsack every file; the information of a file is read and with an algorithm that emaule the functionality of a quantum computer."
EPILOG_TEXT="Author: Danilo López - dlopezs@unicauca.edu.co"

#GLOBAL VARIABLES
NUM_ITERATIONS_STATIC = 20
MH_LIST = [HillClimbing(20), IbmQuantum(20)]

FOLDER_DATASET_FN = DIR_FILES + "dataset_fn" + get_separator()
FOLDER_DATASET_GENERATED = DIR_FILES + "generated_dataset" + get_separator()

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