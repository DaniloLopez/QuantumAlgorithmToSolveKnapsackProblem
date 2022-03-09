from modules.algorithms.solution import Solution

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
        obj_solution.fitness = solution.fitness
        obj_solution.weight = solution.weight
        obj_solution.w = solution.w
        
        return obj_solution

    #override
    def random_initialization(self):      
        self.position = self.__getBinaryVectorAleatory()
        self.step = self.__getBinaryVectorAleatory()
        self.evaluate()

    #override
    def evaluate(self):
        self.my_container.current_efos += 1
        self.calculate_fitness_solution()

    #override
    def calculate_fitness_solution(self):
        """ penalty function for unfeasible solutions """        
        self.fitness = self.my_container.my_knapsack.evaluate(self.position)
        self.calculate_weight_solution()

    def __getBinaryVectorAleatory(self):
        """ a position list is filled aleatory to evaluate the solution. """
        vector = []
        for i in range(0, self.my_container.my_knapsack.n_items):
            rnd = self.my_container.my_aleatory.uniform(0,1)
            if rnd > 0.5:
                vector.append(1)
            else:
                vector.append(0)
        return vector