#!/usr/bin/env python3
# coding=utf-8

from Algorithm_BKP_Quantum_Solution.modules.algorithms.algorithm import Algorithm

class Metaheuristic(Algorithm):
    """docstring for Metaheuristic."""

    def __init__(self):
        super(Metaheuristic, self).__init__()
        self.curve = []

    def get_curve(self):
        return self.curve

    def set_curve(self, value):
        self.curve = value