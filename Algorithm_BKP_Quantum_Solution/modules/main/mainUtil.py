from os import listdir
from modules.file.fileWriter import FileWriter
from modules.arguments.arguments_command_line import ArgumentsCommandLine
from modules.generator.datasetGenerator import DatasetGenerator
import modules.util.generalValue as general
from modules.util.generalValue import SEPARATOR
import modules.util.util as util
from modules.file.fileReader import FileReader

class MainUtil():
    def __init__(self):
        self.obj_fileWriter=FileWriter()
        self.arguments = ArgumentsCommandLine(
            general.DESCRIPTION_TEXT, 
            general.EPILOG_TEXT
        )
        print(self.arguments)
        pass

    def get_knapsack_list(self, knapsack_files_path):
        knapsack_list = []
        # list the folders contained in the root directory
        list_folder_dataset_generated = listdir(knapsack_files_path)
        for folder_name in list_folder_dataset_generated:
            root_path = knapsack_files_path + folder_name
            for knapsack_file_name in util.get_list_files_folder( root_path ):
                #read knapsack file
                full_file_path = root_path + SEPARATOR + knapsack_file_name
                knapsack = self.get_knapsack(
                    full_file_path, 
                    file_name=knapsack_file_name
                )
                if knapsack:
                    knapsack_list.append(knapsack)
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