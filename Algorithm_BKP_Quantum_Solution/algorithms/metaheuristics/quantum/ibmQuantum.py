# -*- coding: utf-8 -*-
#!/usr/bin/python

import modules.quantum.quantum as quantum
from qiskit.aqua.algorithms import ExactEigensolver
from qiskit.aqua.input import EnergyInput

from algorithms.metaheuristics.metaheuristic import Metaheuristic

class IbmQuantum(Metaheuristic):
    """docstring for IbmQuantum."""
    
    def __init__(self, max_efos):
        super(IbmQuantum, self).__init__()
        self.max_efos = max_efos
        
    def execute(self, my_knapsack, my_aleatory):
        #get isntances of Pauli operator for ExactEigensolver      
        qubitOp, offset = quantum.get_knapsack_qubitops(my_knapsack.get_profits(), my_knapsack.get_weigths(), 
                                                        my_knapsack.get_capacity(), M )
        algo_input = EnergyInput(qubitOp)
        ee = ExactEigensolver(qubitOp, k=1) #instance of exactEigensolver        
        result = ee.run() #Run quantum algorithm
        
        most_lightly = result['eigvecs'][0] #format result
        x = quantum.sample_most_likely(most_lightly)
        result_solution = x[:len(my_knapsack.get_profits())]
        v , w =  my_knapsack.calculate_knapsack_value_weight(result_solution)

    def __str__(self):
        return "quantum"

    def __cmp__(self, obj_hill_climbing):
        pass
    
        