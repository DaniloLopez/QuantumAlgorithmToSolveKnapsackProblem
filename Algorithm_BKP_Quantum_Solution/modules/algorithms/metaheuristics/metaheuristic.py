from abc import abstractmethod
from modules.algorithms.algorithm import Algorithm

class Metaheuristic(Algorithm):
    """docstring for Metaheuristic."""

    def __init__(self):
        super(Metaheuristic, self).__init__()
        self.curve = []

    @abstractmethod
    def execute(self, the_knapsack, the_aleatory, debug=False):
        pass

    def __str__(self) -> str:
        return super().__str__() + ".Metaheuristic"