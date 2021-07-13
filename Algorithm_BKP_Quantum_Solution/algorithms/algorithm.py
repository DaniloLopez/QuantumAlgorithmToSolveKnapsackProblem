#!/usr/bin/env python3
# coding=utf-8

from abc import ABC, abstractmethod, abstractproperty

class Algorithm(ABC):
    """docstring for Algorithm."""

    def __init__(self):
        """init class Algorithm"""

    def my_best_solution(self):
        pass

    def my_best_solution(self, value):
        pass

    def my_knapsack(self):
        pass
    
    def my_knapsack(self, value):
        pass

    def my_aleatory(self):
        pass

    @abstractmethod
    def execute(self, the_knapsack, the_aleatory):
        pass

    #abstract properties
    def get_max_efos(self):
        pass

    def set_max_efos(self, value):
        pass

    max_efos = abstractproperty(get_max_efos, set_max_efos) 

    def get_current_efos(self):
        pass

    def set_current_efos(self, value):
        pass

    current_efos = abstractproperty(get_current_efos, set_current_efos)