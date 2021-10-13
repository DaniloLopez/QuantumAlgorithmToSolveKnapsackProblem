from numpy.lib.function_base import select
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

    #override
    def random_initialization(self):      
        self.__fillPositionAleatory()        
        self.evaluate()      

    #override
    def evaluate(self):
        self.my_container.current_efos += 1
        self.calculate_fitness_solution()
        self.__repair_function()
        self.__inprovement_algorithm()

    #override
    def calculate_fitness_solution(self):
        """ penalty function for unfeasible solutions """        
        self.fitness = self.my_container.my_knapsack.evaluate(self.position)
        self.calculate_weight_solution()
        # penalty function
        if self.weight > self.my_container.my_knapsack.capacity:
            self.fitness = self.fitness * -1

    def __fillPositionAleatory(self):
        """ a position list is filled aleatory to evaluate the solution. """
        self.position = []
        for i in range(0, self.my_container.my_knapsack.n_items):
            rnd = self.my_container.my_aleatory.uniform(0,1)
            if rnd > 0.5:
                self.position.append(1)
            else:
                self.position.append(0)  
    
    def __repair_function(self):
        selected = []
        unselected = []
        self._define_selected_unselected_list(selected, unselected)
        while (self.fitness < 0):
            low_pos = self.__get_lowest_density_item_position(selected)
            self.position[selected[low_pos]] = 0            
            unselected.append(selected[low_pos])
            selected.pop(low_pos)            
            self.calculate_fitness_solution()

    def __inprovement_algorithm(self):
        selected = []
        unselected = []
        self._define_selected_unselected_list(selected, unselected)
        while (self.fitness > 0):
            high_pos = self.__get_highest_density_item_position(unselected)
            self.position[unselected[high_pos]] = 1
            self.calculate_fitness_solution()
            if self.fitness > 0:
                selected.append(unselected[high_pos])
                unselected.pop(high_pos)
            else:
                self.position[unselected[high_pos]] = 0
                self.calculate_fitness_solution()
                break
            
    def __get_lowest_density_item_position(self, selected):
        low_pos = 0 
        kp_items = self.my_container.my_knapsack.items
        for i in range (0, len(selected)) :
            if kp_items[selected[low_pos]].density > kp_items[selected[i]].density :
                low_pos = i
        return low_pos
        
    def __get_highest_density_item_position(self, unselected):
        high_pos = 0 
        kp_items = self.my_container.my_knapsack.items
        for i in range (0, len(unselected)) :
            if kp_items[unselected[high_pos]].density < kp_items[unselected[i]].density :
                high_pos = i
        return high_pos