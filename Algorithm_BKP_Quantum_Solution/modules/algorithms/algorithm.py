#!/usr/bin/env python3
# coding=utf-8

from abc import ABC, abstractmethod

class Algorithm(ABC):
    """docstring for Algorithm."""

    def __init__(self):
        self.max_efos = None
        self.current_efos = 0
        self.my_best_solution = None
        self.my_knapsack = None
        self.my_aleatory = None

    @abstractmethod
    def execute(self, the_knapsack, the_aleatory):
        pass
"""
    #getters & setters
    def _get_max_efos(self):
        pass

    def _set_max_efos(self, value):
        self.max_efos = value

    def _get_current_efos(self):
        pass

    def _set_current_efos(self, arg):
        pass

    def get_my_best_solution(self):
        return self.my_best_solution

    def set_my_best_solution(self, value):
        self.my_best_solution = value

    def get_my_knapsack(self):
        return self.my_knapsack

    def set_my_knapsack(self, value):
        self.my_knapsack = value

    def _my_aleatory(self):
        return self.my_aleatory
    
    def _my_aleatory(self, value):
        self.my_aleatory = value

        """