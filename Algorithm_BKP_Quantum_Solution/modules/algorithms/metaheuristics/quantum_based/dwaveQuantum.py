# -*- coding: utf-8 -*-
#!/usr/bin/python

from modules.algorithms.metaheuristics.metaheuristic import Metaheuristic

class DwaveQuantum(Metaheuristic):
    """docstring for DwaveQuantum."""
    
    def __init__(self):
        super(DwaveQuantum, self).__init__()

    def execute(self, my_knapsack, my_aleatory):
        self.my_knapsack = my_knapsack
        self.my_aleatory = my_aleatory
        print("dwave quantum")
    
    def __str__(self):
        return "quantum"

    def __cmp__(self, obj_quantum):
        pass
    