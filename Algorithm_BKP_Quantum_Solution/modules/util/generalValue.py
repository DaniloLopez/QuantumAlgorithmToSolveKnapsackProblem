from os import path
from modules.util.util import get_separator
import modules.util.util as util

ROOT_DIR = util.get_project_root()

NAME_FILES_FN = ["f3.txt", "f2.txt", "f8.txt", "f6.txt", "f9.txt", "f5.txt",  "f11.txt", "f10.txt", "f4.txt", "f7.txt", "f1.txt"]
DIR_FILES = str(ROOT_DIR) + get_separator() + "files" + get_separator()

DESCRIPTION_TEXT = "This program execute and analize a set of data with information about a knapsack every file; the information of a file is read and with an algorithm that emaule the functionality of a quantum computer."
EPILOG_TEXT="Author: Danilo López - dlopezs@unicauca.edu.co"

NUM_ITERATIONS_STATIC = 20
M = 2000000

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

ZERO_CHAR = "0"
