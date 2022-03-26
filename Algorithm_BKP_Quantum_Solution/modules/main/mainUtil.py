import os
from modules.file.fileWriter import FileWriter
from modules.arguments.arguments_command_line import ArgumentsCommandLine
from modules.generator.datasetGenerator import DatasetGenerator
import modules.util.generalValue as general
from modules.file.fileReader import FileReader

class MainUtil():
    def __init__(self):
        self.obj_fileWriter=FileWriter()
        self.arguments = ArgumentsCommandLine(
            general.DESCRIPTION_TEXT, 
            general.EPILOG_TEXT
        )

    def get_knapsack_list(self, knapsack_files_path):
        knapsack_list = []
        # list the folders contained in the root directory
        for folder_name, dirs, files in os.walk(knapsack_files_path):
            for knapsack_file_name in files:
                #read knapsack file
                full_file_path = folder_name + general.SEPARATOR + knapsack_file_name
                knapsack = self.get_knapsack(
                    full_file_path, 
                    file_name=knapsack_file_name
                )
                if knapsack:
                    knapsack_list.append(knapsack)
                else:
                    print(f"Error: file {full_file_path} can not be read")
        return knapsack_list

    def get_knapsack(self, full_file_path, file_name=None):
        reader_knapsack_file = FileReader(
            full_file_path, 
            short_file_name=file_name
        )
        return reader_knapsack_file.get_knapsack()
         
    def generate_dataset(self, arguments):
        """Generate dataset according to arguments of subcomand generate"""        
        generator = DatasetGenerator(arguments)
        # generating dataset...
        generator.generate()
        print("--------------------------------------------------------------")
        print("------- ::: DATASET GENERATED ::: ----------------------------")
        print("--------------------------------------------------------------")

    def print_list(self, list):
        print("--------------------------------------------------------------")
        print("------- ::: LIST{ length : " +str(len(list))+ " } ::: --------")
        for i in list:
            print(str(i))
        print("------- ::: END LIST ::: -------------------------------------")
        print("--------------------------------------------------------------")