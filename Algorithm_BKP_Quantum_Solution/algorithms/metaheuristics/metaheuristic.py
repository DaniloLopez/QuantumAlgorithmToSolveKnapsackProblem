#!/usr/bin/env python3
# coding=utf-8

from abc import abstractmethod
from algorithms.algorithm import Algorithm

class Metaheuristic(Algorithm):
    """docstring for Metaheuristic."""

    def __init__(self):
        super(Metaheuristic, self).__init__()
        super().set_current_efos(0)
        self.curve = []
    
    @abstractmethod
    def execute(self, the_knapsack, the_aleatory):
        pass

    @property
    def max_efos(self):
        """The max_efos property."""
        return self._max_efos
    
    @max_efos.setter
    def max_efos(self, value):
        self._max_efos = value

    @property
    def current_efos(self):
        """The current_efos property."""
        return self._current_efos

    @current_efos.setter
    def current_efos(self, value):
        self._current_efos = value