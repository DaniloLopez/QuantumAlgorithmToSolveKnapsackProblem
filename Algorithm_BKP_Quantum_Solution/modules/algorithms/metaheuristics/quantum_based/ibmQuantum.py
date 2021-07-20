# -*- coding: utf-8 -*-
#!/usr/bin/python

# useful additional packages 
import numpy as np
import math
from qiskit.quantum_info import Pauli
from qiskit.aqua.operators import WeightedPauliOperator
from qiskit.aqua.algorithms import ExactEigensolver
from qiskit.aqua.input import EnergyInput

from collections import OrderedDict
from modules.algorithms.metaheuristics.metaheuristic import Metaheuristic
from modules.algorithms.solution import Solution

class IbmQuantum(Metaheuristic):
    """docstring for IbmQuantum."""
    
    def __init__(self, max_efos):
        super(IbmQuantum, self).__init__()
        self.max_efos = max_efos
        self._M = 2000000
        
    def execute(self, my_knapsack, my_aleatory, debug=False):
        self.my_knapsack = my_knapsack
        self.my_aleatory = my_aleatory

        #get isntances of Pauli operator for ExactEigensolver      
        qubitOp, offset = self._get_knapsack_qubitops(
            [it.value for it in self.my_knapsack.items], 
            [it.weight for it in self.my_knapsack.items], 
            self.my_knapsack.capacity, 
            self._M 
        )
        EnergyInput(qubitOp)
        ee = ExactEigensolver(qubitOp, k=1) #instance of exactEigensolver        
        result = ee.run() #Run quantum algorithm
        
        most_lightly = result['eigvecs'][0] #format result
        x = self._sample_most_likely(most_lightly)
        #solution
        result_solution = x[:len(my_knapsack.get_profits())]
        self.my_best_solution = Solution.init_owner(self)
        self.my_best_solution.position = result_solution
        self.my_best_solution.evaluate()
        v , w =  my_knapsack.calculate_knapsack_value_weight(result_solution)
        if debug:            
            print(result_solution , end="")
            print(f" profit: {v}  weight: {w}\n")

    def _sample_most_likely(self, state_vector):
        if isinstance(state_vector, dict) or isinstance(state_vector, OrderedDict):
            # get the binary string with the largest count
            binary_string = sorted(state_vector.items(), 
                                    key=lambda kv: kv[1])[-1][0]
            x = np.asarray([int(y) for y in reversed(list(binary_string))])
            return x
        else:
            n = int(np.log2(state_vector.shape[0]))
            k = np.argmax(np.abs(state_vector))
            x = np.zeros(n)
            for i in range(n):
                x[i] = k % 2
                k >>= 1
            return x

    def _get_knapsack_qubitops(self, values, weights, w_max, M):
        ysize = int(math.log(w_max + 1, 2))
        n = len(values)
        num_values = n + ysize;
        pauli_list = []
        shift = 0
        
        #term for sum(x_i*w_i)^2
        for i in range(n):
            for j in range(n):
                coef = -1 * 0.25 * weights[i] * weights[j] * M
                
                xp = np.zeros(num_values, dtype=np.bool)
                zp = np.zeros(num_values, dtype=np.bool)
                zp[j] = not zp[j]
                pauli_list.append([coef, Pauli(zp, xp)])
                shift -= coef
                
                xp = np.zeros(num_values, dtype=np.bool)
                zp = np.zeros(num_values, dtype=np.bool)
                zp[i] = not zp[i]
                pauli_list.append([coef, Pauli(zp, xp)])
                shift -= coef
                
                coef = -1 * coef
                xp = np.zeros(num_values, dtype=np.bool)
                zp = np.zeros(num_values, dtype=np.bool)
                zp[i] = not zp[i]
                zp[j] = not zp[j]
                pauli_list.append([coef, Pauli(zp, xp)])
                shift -= coef
                
        #term for sum(2^j*y_j)^2
        for i in range(ysize):
            for j in range(ysize):
                coef = -1 * 0.25 * (2^i) * (2^j) * M
                
                xp = np.zeros(num_values, dtype=np.bool)
                zp = np.zeros(num_values, dtype=np.bool)
                zp[n+j] = not zp[n+j]
                pauli_list.append([coef, Pauli(zp, xp)])
                shift -= coef
                
                xp = np.zeros(num_values, dtype=np.bool)
                zp = np.zeros(num_values, dtype=np.bool)
                zp[n+i] = not zp[n+i]
                pauli_list.append([coef, Pauli(zp, xp)])
                shift -= coef
                
                coef = -1 * coef
                xp = np.zeros(num_values, dtype=np.bool)
                zp = np.zeros(num_values, dtype=np.bool)
                zp[n+i] = not zp[n+i]
                zp[n+j] = not zp[n+j]
                pauli_list.append([coef, Pauli(zp, xp)])
                shift -= coef
                
        #term for -2*W_max*sum(x_i*w_i)
        for i in range(n):
            xp = np.zeros(num_values, dtype=np.bool)
            zp = np.zeros(num_values, dtype=np.bool)
            zp[i] = not zp[i]
            coef = w_max * weights[i] * M
            pauli_list.append([coef, Pauli(zp, xp)])
            shift -= coef
            
        #term for -2*W_max*sum(2^j*y_j)
        for j in range(ysize):
            xp = np.zeros(num_values, dtype=np.bool)
            zp = np.zeros(num_values, dtype=np.bool)
            zp[n+j] = not zp[n+j]
            coef = w_max * (2^j) * M
            pauli_list.append([coef, Pauli(zp, xp)])
            shift -= coef
        
        #term for -2*sum(2^j*y_j)*sum(x_i*w_i)
        for i in range(n):
            for j in range(ysize):
                coef = -0.5 * weights[i] * (2^j) * M
                
                xp = np.zeros(num_values, dtype=np.bool)
                zp = np.zeros(num_values, dtype=np.bool)
                zp[n+j] = not zp[n+j]
                pauli_list.append([coef, Pauli(zp, xp)])
                shift -= coef
                
                xp = np.zeros(num_values, dtype=np.bool)
                zp = np.zeros(num_values, dtype=np.bool)
                zp[i] = not zp[i]
                pauli_list.append([coef, Pauli(zp, xp)])
                shift -= coef
                
                coef = -1 * coef
                xp = np.zeros(num_values, dtype=np.bool)
                zp = np.zeros(num_values, dtype=np.bool)
                zp[i] = not zp[i]
                zp[n+j] = not zp[n+j]
                pauli_list.append([coef, Pauli(zp, xp)])
                shift -= coef
                
        #term for -sum(x_i*v_i)
        for i in range(n):
            xp = np.zeros(num_values, dtype=np.bool)
            zp = np.zeros(num_values, dtype=np.bool)
            zp[i] = not zp[i]
            pauli_list.append([0.5 * values[i], Pauli(zp, xp)])
            shift -= 0.5 * values[i]
        return WeightedPauliOperator(paulis=pauli_list), shift
    
    def __str__(self):
        return "quantum"

    def __cmp__(self, obj_quantum):
        pass