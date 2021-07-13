# -*- coding: utf-8 -*-
#!/usr/bin/python

from Algorithm_BKP_Quantum_Solution.modules.algorithms.metaheuristics.metaheuristic import Metaheuristic

class HillClimbing(Metaheuristic):
    """docstring for HillClimbing."""
    
    def __init__(self, max_efos):
        super(HillClimbing, self).__init__()
        self.max_efos = max_efos
        
    def execute(self, the_knapsack, the_aleatory):
        print("Hola hill climbing")

    def __str__(self):
        return "Hill Climbing"

    def __cmp__(self, obj_hill_climbing):
        pass

"""
    def __str__(self) -> str:
        return super().__str__()
   """