from abc import ABC, abstractmethod

class Algorithm(ABC):
    """docstring for Algorithm."""

    def __init__(self):
        self.max_efos = 0
        self.current_efos = 0
        self.my_best_solution = None
        self.my_knapsack = None
        self.my_aleatory = None
        self.population = []

    @abstractmethod
    def execute(self, the_knapsack, the_aleatory, debug=False):
        pass

    def __str__(self) -> str:
        return "Algorithm"