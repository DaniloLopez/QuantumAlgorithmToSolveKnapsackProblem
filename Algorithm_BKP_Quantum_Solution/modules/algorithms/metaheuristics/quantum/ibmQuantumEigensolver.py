# -*- coding: utf-8 -*-
# !/usr/bin/python

# useful additional packages
import modules.util.util as util

#Qiskit libraries
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit.algorithms import NumPyMinimumEigensolver
from qiskit_optimization.applications import Knapsack

from modules.algorithms.metaheuristics.metaheuristic import Metaheuristic
from modules.algorithms.solution import Solution


class IbmQuantumEigensolver(Metaheuristic):
    """docstring for IbmQuantum."""

    def __init__(self, max_efos):
        super(IbmQuantumEigensolver, self).__init__()
        self._M = 2000000
        self.max_efos = max_efos

    def execute(self, my_knapsack, my_aleatory, debug=False):
        self.my_knapsack = my_knapsack
        self.my_aleatory = my_aleatory
        self.current_efos = 0

        prob = Knapsack(
            values=[it.value for it in self.my_knapsack.items],
            weights=[it.weight for it in self.my_knapsack.items],
            max_weight=self.my_knapsack.capacity
        )

        qp = prob.to_quadratic_program()

        # Numpy Eigensolver
        meo = MinimumEigenOptimizer(min_eigen_solver=NumPyMinimumEigensolver())
        result = meo.solve(qp)
        print("result:\n", result)
        print("\nsolution:\n", prob.interpret(result))

        # init solution object
        self.my_best_solution = Solution.init_owner(self)
        self.my_best_solution.position = result.x.astype(int).tolist()
        self.my_best_solution.evaluate()
        out = "\t\tq_solution: " + str(result) + " weight: " + \
              str(self.my_best_solution.weight) + " fitness: " + \
              str(self.my_best_solution.fitness)
        util.if_print_text(out, debug)


    def __str__(self) -> str:
        return super().__str__() + ".IBM_Quantum_Algorithm_QAOA__Qiskit"


