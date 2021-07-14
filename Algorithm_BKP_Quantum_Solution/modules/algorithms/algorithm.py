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