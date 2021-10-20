from modules.algorithms.algorithm import Algorithm

class PopulationMetaheuristic(Algorithm):
    """docstring for Metaheuristic."""

    def __init__(self, pop_size, z_value):
        super(PopulationMetaheuristic, self).__init__()
        self.curve = []
        self.pop_size = pop_size        
        self.lb = [-pop_size]
        self.ub = [pop_size]
        self.z = z_value

    def execute(self, the_knapsack, the_aleatory, debug):
        pass

    def __str__(self) -> str:
        return super().__str__() + ".PopulationMetaheuristic"