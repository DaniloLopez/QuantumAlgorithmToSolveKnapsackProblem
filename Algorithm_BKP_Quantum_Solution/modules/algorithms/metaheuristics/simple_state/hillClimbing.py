# -*- coding: utf-8 -*-
#!/usr/bin/python

from modules.algorithms.solution import Solution
from modules.algorithms.metaheuristics.metaheuristic import Metaheuristic
import modules.util.util as util

class HillClimbing(Metaheuristic):
    """docstring for HillClimbing."""
    
    def __init__(self, max_efos):
        super(HillClimbing, self).__init__()
        self.max_efos = max_efos
        
    def execute(self, the_knapsack, the_aleatory, debug=False):
        self.my_knapsack = the_knapsack
        self.my_aleatory = the_aleatory
        self.current_efos = 0
        #Hill Climbing
        s = Solution.init_owner(self)
        s.random_initialization()
        self.curve.append(s.fitness)
        while self.current_efos < self.max_efos and abs(s.fitness - self.my_knapsack.objective) > 1e-10:
            r = Solution.init_solution(s)
            r.tweak()
            if r.fitness > s.fitness:
                s = Solution.init_solution(r)                
                if debug and abs(s.fitness - self.my_knapsack.objective) < 1e-10:
                    print("\t\thc_solution: " + str(s.position) +\
                        "  weight: " + str(s.weight) +  "  fitness: " +\
                        str(s.fitness)
                    )
            self.curve.append(s.fitness)

            if abs(s.fitness - self.my_knapsack.objective) < 1e-10:
                break
        self.my_best_solution = s

    def __str__(self) -> str:
        return super().__str__() + ".Hill_Climbing"
