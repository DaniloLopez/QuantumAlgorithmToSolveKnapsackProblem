from modules.algorithms.solution import Solution
from modules.algorithms.metaheuristics.population.dragonfly import DIM_DA, LB_DA, UB_DA, PI
import math

class DragonflySolution(Solution):
    """docstring for DragonflySolution."""

    def __init__(self):
        raise RuntimeError

    @classmethod
    def init_owner(cls, owner):
        obj_solution = cls.__new__(cls)        
        obj_solution.my_container = owner
        obj_solution.position = [
            0 for k in range(obj_solution.my_container.my_knapsack.n_items)
        ]
        obj_solution.da = [] # a,b,c,d,k vector
        obj_solution.step = None
        obj_solution.fitness = None
        obj_solution.weight = None
        obj_solution.w = None
        return obj_solution
    
    @classmethod
    def init_solution(cls, solution):
        obj_solution = cls.__new__(cls)        
        obj_solution.my_container = solution.my_container
        obj_solution.position = solution.position.copy()
        obj_solution.step = solution.step.copy()
        obj_solution.da = solution.da.copy()
        obj_solution.fitness = solution.fitness
        obj_solution.weight = solution.weight
        obj_solution.w = solution.w
        
        return obj_solution

    #override
    def random_initialization(self):      
        self.position = self.__get_binary_vector_aleatory(
            self.my_container.my_knapsack.n_items, 0, 1, False
        )
        self.step = self.__get_binary_vector_aleatory(DIM_DA, 0, 1, True)
        self.da = self.__get_binary_vector_aleatory(DIM_DA, LB_DA, UB_DA, True)
        self.evaluate()

    #override
    def evaluate(self):
        self.my_container.current_efos += 1
        self.__calculate_position_with_gx()
        self.calculate_fitness_solution()

    #override
    def calculate_fitness_solution(self):
        """ penalty function for unfeasible solutions """
        self.fitness = self.my_container.my_knapsack.evaluate(self.position)
        self.calculate_weight_solution()
        # penalty function: fitness = C - sum(Wi * Xi)
        if self.weight > self.my_container.my_knapsack.capacity:
            self.fitness = self.my_container.my_knapsack.capacity - self.weight

    def __get_binary_vector_aleatory(self, length, min, max, is_continuous):
        """ a position list is filled aleatory to evaluate the solution. """
        vector = []
        for i in range(0, length):
            rnd = self.my_container.my_aleatory.uniform(min,max)
            if is_continuous:
                vector.append(rnd)
            else:
                vector.append(1 if rnd > 0.5 else 0)
        return vector

    def __calculate_position_with_gx(self):
        a = self.da[0]
        b = self.da[1]
        c = self.da[2]
        d = self.da[3]
        k = self.da[4]

        cos_value = None
        sen_value = None
        for x in range(len(self.position)):
            
            try:
                cos_value = 2 * PI * (x-a) * c
                sen_value = 2 * PI * (x-a) * b
                gx = math.sin(sen_value * math.cos(cos_value) + k) + d
                self.position[x] = 1 if gx > 0 else 0
            except Exception as e:
                print(e)
