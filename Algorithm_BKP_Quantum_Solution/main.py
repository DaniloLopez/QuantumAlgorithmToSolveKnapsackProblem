# -*- coding: utf-8 -*-
#!/usr/bin/python

#necessary packages 
from modules.menu.menu import Menu
import modules.util.generalValue as general
from modules.generator.datasetGenerator import DatasetGenerator
from modules.evaluator.datasetEvaluator import DatasetEvaluator
from modules.file.fileWriter import FileWriter
from os import listdir, path

# Manage list directory
ROOT_DIR = path.dirname(path.abspath(__file__))
list_folder_dataset_generated = listdir(ROOT_DIR + general.FOLDER_DATASET_GENERATED)
print(ROOT_DIR)
print(ROOT_DIR + general.FOLDER_DATASET_GENERATED)

menu = Menu(general.DESCRIPTION_TEXT, general.EPILOG_TEXT) # instance to manage program menu
obj_fileWriter  = FileWriter()

num_iterations = int(menu.getIterations()) if (menu.getIterations() is not None) else general.NUM_ITERATIONS_STATIC

#instance to manage program generator dataset
generator = DatasetGenerator(1000)

#instance to manage program evaluator dataset
evaluator = DatasetEvaluator()

print("Running...")

num_iterations = int(menu.getIterations()) if (menu.getIterations() is not None) else general.NUM_ITERATIONS_STATIC
    

if(menu.is_generated_data()):
    generator.generate()
    print("Successfully generated dataset")

if(menu.is_evaluate_data()):
    #evaluator.evaluate()
    print("Successfully evaluated dataset")
    
if(menu.is_generate_evaluate()):
    #generator.generate()
    #evaluator.evaluate()
    print("Successfully generated and evaluate dataset")
