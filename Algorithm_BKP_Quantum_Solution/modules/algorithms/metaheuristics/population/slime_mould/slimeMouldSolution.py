from modules.algorithms.solution import Solution
from numpy.random import uniform
from numpy import log10

class SlimeMouldSolution(Solution):
    """docstring for SlimeMouldSolution."""
    
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
        return obj_solution
    
    @classmethod
    def init_solution(cls, solution):
        obj_solution = cls.__new__(cls)        
        obj_solution.my_container = solution.my_container
        obj_solution.position = solution.position.copy()
        obj_solution.fitness = solution.fitness
        obj_solution.weight = solution.weight
        obj_solution.w = solution.w
        return obj_solution

    def random_initialization(self):
        selected = []
        unselected = []
        self.fillPositionAleatory()
        my_weight = self._define_selected_unselected_list(selected, unselected)
        my_weight = self._complete(unselected, my_weight)
        self.evaluate()

    def fillPositionAleatory(self):
        """ Position list is filled to evaluate the solution. """
        self.position = []
        cap = self.my_container.my_knapsack.capacity
        for i in range(0, self.my_container.my_knapsack.n_items):
            rnd = self.my_container.my_aleatory.uniform(0,1)
            if rnd > 0.5:
                self.position.append(1)
            else:
                self.position.append(0)        

    def evaluate(self):
        self.my_container.current_efos += 1 
        self.calculate_weight_solution()
        self.calculate_fitness_solution(self.weight)

    def calculate_fitness_solution(self, weight):
        """penalty function for unfeasible solutions"""
        self.fitness = self.my_container.my_knapsack.evaluate(self.position)
        if weight > self.my_container.my_knapsack.capacity:
            self.fitness = self.fitness * -1
            
    