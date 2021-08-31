from modules.algorithms.solution import Solution

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
        
        return obj_solution

    @classmethod
    def init_solution(cls, solution):
        obj_solution = cls.__new__(cls)        
        obj_solution.position = solution.position.copy()
        obj_solution.fitness = solution.fitness
        obj_solution.weight = solution.weight
        obj_solution.my_container = solution.my_container
        return obj_solution

    def random_initialization(self):
        selected = []
        unselected = []
        my_weight = self._define_selected_unselected_list(selected, unselected)
        my_weight = self._complete(unselected, my_weight)
        self.evaluate()