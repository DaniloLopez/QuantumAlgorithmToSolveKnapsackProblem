#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import os
from pathlib import Path

#PROJECT VARIABLES
FILES = "files"
PROJECT_ROOT = Path(__file__).parent.parent.parent
SEPARATOR = os.path.sep
LINE_SEPARATOR = os.linesep
DIR_FILES = str(PROJECT_ROOT) + SEPARATOR + FILES + SEPARATOR

#DESCRIPTION MENU HELP
DESCRIPTION_TEXT = "This program execute and analyze a set of data with "\
    "information about a knapsack every file; the information of a file is "\
    "read and with an algorithm that emulate the functionality of a quantum "\
    "computer."
EPILOG_TEXT="Author: Danilo López - dlopezs@unicauca.edu.co"

#GLOBAL VARIABLES
DATASET_FN = "dataset_fn"
GENERATED_DATASET = "generated_dataset"
NUM_ITERATIONS_STATIC = 20
FOLDER_DATASET_FN = DIR_FILES + DATASET_FN + SEPARATOR
FOLDER_DATASET_GENERATED = DIR_FILES + GENERATED_DATASET + SEPARATOR

ERR_DUPLICATED_ARGUMENT = "Duplicated parameter arguments are not allowed."

#GLOBAL GENERAL VARIABLES 
EASY = "easy"
MEDIUM = "medium"
HARD = "hard"
ZERO_CHAR = "0"
CHAR_R_PLUS = "r+"
ZERO_DOT_TWO = 0.2
PROGRAM_NAME = "main"

#VARIABLES FOR PARAMETERS MENU
SUBCOMANDS = "subcomands"
CMD_GENERATE = "generate"
CMDH_GENERATE = "generate dataset."

ARG_I = "-i"
ARG_ITERATION = "--iterations"
ARGH_ITERATION = "Number of iterations to run each file with a knapsack."

ARG_T = "-t"
ARG_TYPE = "--type"
ARGH_TYPE = "Indicate type of correlation between items."

ARG_D = "-d"
ARG_DIFFICULT = "--difficult"
ARGH_DIFFICULT = "Indicate difficult of generated dataset (1=Easy, 2=Medium, "\
    "3=Hard, 0=All options)."

ARG_N = "-n"
ARG_NITEMS = "--nitems"
ARGH_NITEMS = "Indicate quantity o items stored in knapsack."

ARG_R = "-r"
ARG_RANGE = "--range"
ARGH_RANGE = "Indicate range of creation for dataset."

ARG_G = "-g"
ARG_GENERATE = "--generate"
ARGH_GENERATE = "To generate dataset according to input parameters.\nT=Type "\
    + ARGH_TYPE + "\nD=Difficult " + ARGH_DIFFICULT + "\nN=N_Items "\
    + ARGH_NITEMS + "\nR=Range " + ARGH_RANGE + "."

ARG_FL = "-fl"
ARG_FILE = "--file"
ARGH_FILE="Indicate file with content of a knapsack to make evaluation.\n"\
    "Default root folder where the dataset is stored is "\
    "[rootProject/files/folder] or provide the full address."

ARG_FD = "-fd"
ARG_FOLDER = "--folder"
ARGH_FOLDER = "Indicate folder with knapsack files to make evaluation."\
    "Default root folder is [rootProject/files/folder] or provide the "\
    "full address."

ARG_DB = "-d"
ARG_DEBUG = "--debug"
ARGH_DEBUG = "If this flag is sent, debug mode will be enabled."