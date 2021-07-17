# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class Parameter(ABC):
    """docstring for Option."""

    def __init__(self):
        super(Parameter, self).__init__()
        self.iterations = None
        self.function = None
        self.type = None
        self.difficult = None
        self.nitems = None
        self.range = None
        self.file = None
        self.folder = None
    
    def get_parameters_dataset(self):
        """return parameters to generate dataset"""
        return self.type, self.difficult, self.nitems, self.nitems

    #Abstract methods
    @abstractmethod
    def getIterations(self):
        pass

    @abstractmethod
    def is_generated_data(self):
        pass

    @abstractmethod
    def is_evaluate_data(self):
        pass

    @abstractmethod
    def get_file_knapsack(self):
        pass

    @abstractmethod
    def get_folder_dataset(self):
        pass