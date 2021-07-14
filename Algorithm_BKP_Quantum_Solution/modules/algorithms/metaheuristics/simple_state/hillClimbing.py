# -*- coding: utf-8 -*-
#!/usr/bin/python

from Algorithm_BKP_Quantum_Solution.modules.algorithms.solution import Solution
from Algorithm_BKP_Quantum_Solution.modules.algorithms.metaheuristics.metaheuristic import Metaheuristic

class HillClimbing(Metaheuristic):
    """docstring for HillClimbing."""
    
    def __init__(self, max_efos):
        super(HillClimbing, self).__init__()
        self.max_efos = max_efos
        
    def execute(self, the_knapsack, the_aleatory):
        self.my_knapsack = the_knapsack
        self.my_aleatory = the_aleatory
        self.current_efos = 0
        self.curve = []

        #Hill Climbing
        s = Solution.init_owner(self)
        

        print("Hola hill climbing")

    def __str__(self):
        return "Hill Climbing"

    def __cmp__(self, obj_hill_climbing):
        pass

"""
    def __str__(self) -> str:
        return super().__str__()
   """