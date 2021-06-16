#  usr/bin/env
# -*- coding: utf-8 -*-

from Algorithm_BKP_Quantum_Solution.modules.util.util import get_separator
import os
from modules.generator.instanceData import InstanceData
from modules.util.util import generateUrlNewDataset
import modules.util.generalValue as general

class DatasetGenerator():

    def __init__(self, ntest, nmax=5, tipemax=2, rmax=4, rmin=1, ninstances=5):
        self.n_max = nmax
        self.type_max = tipemax
        self.range_max = rmax
        self.range_min = rmin
        self.n_test = ntest
        self.n_instances = ninstances

    def generate(self):
        """algoritmo principal encargado de generar los dataset"""
        self.generateDatasetLowDificult()
        #self.generateDatasetMediumDificult()
        #self.generateDatasetMediumDificult()    

    def generateDatasetLowDificult(self):
        """generar dataset con dificultad baja"""
        for i in range(self.range_min, self.range_max):
            self.generarDataset(10, i, general.EXEC_EASY_KP_GEN, general.FOLDER_EASY_INSTANCE)

    def generateDatasetMediumDificult(self):
        """generar dataset con dificultad media"""
        for i in range(self.range_min, self.range_max):
            self.generarDataset(10, i, general.EXEC_MEDIUM_KP_GEN, general.FOLDER_MEDIUM_INSTANCE)

    def generateDatasetMediumDificult(self):
        """se genera dataset con dificultad alta"""
        for i in range(self.range_min, self.range_max):
            self.generarDataset(10, i, general.EXEC_HARD_KP_GEN, general.FOLDER_HARD_INSTANCE)
    
    def generarDataset(self, step_range, type_corr, execute, folder):        
        for n in range(5, self.n_max+1):
            for r in range(self.range_min, self.range_max + 1, step_range):
                kp_data = InstanceData(n, r, type_corr, self.n_instances, self.n_test)                
                name_file_new = generateUrlNewDataset(kp_data, 1, folder)
                print("######" + execute + " " + name_file_new)
                os.system(execute + " " + name_file_new)
                #fileReader.read_file_knapsack_generate_pisinger(name_file_new)