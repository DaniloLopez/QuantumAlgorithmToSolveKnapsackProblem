from typing import Match

from pandas import value_counts
from modules.algorithms.solution import Solution
import random, math

PI = math.pi
PI_DIV_4 = math.pi/4

class GreyWolfSolution(Solution):
    """docstring for GreyWolfOptimizerSolution."""
    def __init__(self):
        raise RuntimeError
    
    @classmethod
    def init_owner(cls, owner):
        obj_solution = cls.__new__(cls)        
        obj_solution.my_container = owner
        obj_solution.position = [
            0 for k in range(obj_solution.my_container.my_knapsack.n_items)
        ]
        obj_solution.fitness = None
        obj_solution.weight = None
        obj_solution.w = None
        obj_solution.quantum_theta = None
        return obj_solution
    
    @classmethod
    def init_solution(cls, solution):
        obj_solution = cls.__new__(cls)        
        obj_solution.my_container = solution.my_container
        obj_solution.position = solution.position.copy()
        obj_solution.fitness = solution.fitness
        obj_solution.weight = solution.weight
        obj_solution.w = solution.w
        obj_solution.quantum_theta = solution.quantum_theta
        return obj_solution

    def __gt__(self, greyWolf):
        return self.fitness > greyWolf.fitness

    #override
    def random_initialization(self):
        values_admitted = [1,3,5,7]
        self.quantum_theta = [
            random.choice(values_admitted)*PI_DIV_4 # (r_ij * PI_DIV_4) - equation 5
            for k in range(self.my_container.my_knapsack.n_items)
        ]
        self.quantum_observation_fitness_evaluation()

    def quantum_initialization(self, quantum):
        self.quantum_theta = quantum
        self.quantum_observation_fitness_evaluation()

    def quantum_observation_fitness_evaluation(self):
        quantum = [list([math.cos(o), math.sin(o)]) for o in self.quantum_theta] #q_i - equation 6
        self.__quantum_observation_reparation(quantum)
        self.evaluate()

    def __quantum_observation_reparation(self, quantum):
        # initialize the bits of individual X to 0
        self.position = [0 for k in range(self.my_container.my_knapsack.n_items)]
        w_total = 0
        i = 0
        m = len(quantum)-1
        while(w_total < self.my_container.my_knapsack.capacity):
            i = random.randint(0, m)
            if self.position[i] == 0: 
                r = random.choice([0,1])
                cos = quantum[i][0] # TODO deberia ser seno ya que es quien representa la probabilidad de seleccionar el item
                if r > math.pow(abs(cos),2): #observation of quantum vector
                    self.position[i] = 1
                    w_total += self.my_container.my_knapsack.items[i].weight
        self.position[i] = 0
        self.weight = w_total - self.my_container.my_knapsack.items[i].weight

    #override
    def evaluate(self):
        self.my_container.current_efos += 1
        self.calculate_fitness_solution()

    #override
    def calculate_fitness_solution(self):
        """ penalty function for unfeasible solutions """        
        self.fitness = self.my_container.my_knapsack.evaluate(self.position)
        self.calculate_weight_solution()
        
