from modules.algorithms.solution import Solution
from modules.algorithms.metaheuristics.slime_mould.slimeMouldSolution import SlimeMouldSolution
from modules.algorithms.metaheuristics.metaheuristic import Metaheuristic

class SlimeMould(Metaheuristic):
    """docstring for SlimeMould."""
    
    def __init__(self, max_efos):
        super(SlimeMould, self).__init__()        
        self.max_efos = max_efos
    
    def execute(self, the_knapsack, the_aleatory, debug):
        self.my_knapsack = the_knapsack
        self.my_aleatory = the_aleatory
        self.current_efos = 0
        
        listSolution = []        
        s = SlimeMouldSolution.init_owner(self)
        s.random_initialization()


        self.curve.append(s.fitness)
        while self.current_efos < self.max_efos:
            r = Solution.init_solution(s)

    def _getBestFitness(listSolution):
        pass