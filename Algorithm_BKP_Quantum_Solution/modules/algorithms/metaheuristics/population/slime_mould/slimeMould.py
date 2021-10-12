from modules.algorithms.metaheuristics.population.slime_mould.slimeMouldSolution import SlimeMouldSolution
from modules.algorithms.metaheuristics.metaheuristic import Metaheuristic

from numpy.random import uniform, choice
from numpy import abs, zeros, log10, where, arctanh, tanh, ones, clip

class SlimeMould(Metaheuristic):
    """docstring for SlimeMould."""
    
    _EPSILON = 10E-10

    def __init__(self, max_efos):
        super(SlimeMould, self).__init__()
        self.max_efos = max_efos        
        self.popsize = 0
        self.lb = None
        self.ub = None
        self.z = 0.3
        self.setPopSize()
        
    def setPopSize(self, popsize=5):
        self.popsize = popsize
        self.lb = -1 * ones(self.popsize)
        self.ub = 1 * ones(self.popsize)

    def execute(self, the_knapsack, the_aleatory, debug):
        # variables
        self.my_knapsack = the_knapsack
        self.my_aleatory = the_aleatory        
        self.curve = []
        self.current_efos = 0

        g_best = None   # DF - Best fitness all iterations        
        listSearchAgent = self.__generate_population_aleatory()
        
        # returns descending order list according to best fitness
        listSearchAgent, g_best = self.__get_sorted_list_and_global_best_solution(listSearchAgent, isReverse=True)
        t = 0
        while t < self.max_efos:
            # plus epsilon to avoid denominator zero
            s = listSearchAgent[0].fitness - listSearchAgent[-1].fitness + self._EPSILON              
            self.calculate_w(listSearchAgent, s)

            # The value of vb oscillates randomly between [−a, a] and gradually approaches zero as the iterations increase
            a = arctanh(-((self.current_efos + 1) / self.max_efos) + 1)  # Eq.(2.4)

            #The value of vc oscillates between [− 1,1] and tends to zero eventually           
            b = 1 - (t + 1) / self.max_efos
                       
            # Update the Position of search agents
            for i in range(0, self.pop_size):
                pos_new = None
                if uniform() < self.z:  # Eq.(2.7)
                    pos_new = uniform(0,1) * (self.lb - self.ub) + self.lb
                else:
                    p = tanh(abs(listSearchAgent[i].fitness - g_best.fitness))  # Eq.(2.2)                                    
                    vb = uniform(-a, a)
                    # two positions randomly selected from population, apply for the whole problem size instead of 1 variable
                    id_a, id_b = choice(list(set(range(0, self.pop_size)) - {i}), 2, replace=False)

                    # Eq. 12
                    #xb(t) + vb * (w *xa(t)-xb(t))    
                    pos_1 = g_best.position + vb * ([ag.w for ag in listSearchAgent] * listSearchAgent[id_a].position - listSearchAgent[id_b].position)                    
                    #uniform(0,1) X gausian(x(t))
                    pos_2 = uniform(0,1) * self.__gausian(listSearchAgent[i].position)
                    pos_new = where(uniform(0, 1) < p, pos_1, pos_2)

                # Check bound and re-calculate fitness after each individual move
                pos_new = self.__amend_position(pos_new)

                listSearchAgent[i].position = pos_new
                # plus epsilon to avoid denominator zero
                s = listSearchAgent[0].fitness - listSearchAgent[-1].fitness + self._EPSILON
                self.calculate_w(listSearchAgent, s)
            listSearchAgent, g_best = self.__get_sorted_list_and_global_best_solution(listSearchAgent, isReverse=True)
            t += 1

    def __generate_population_aleatory(self):
        listAgent = []
        for i in range (self.popsize):
            listAgent.append(self.__get_instance_solution())
        return listAgent

    def __get_instance_solution(self):
        s = SlimeMouldSolution.init_owner(self)
        s.random_initialization()
        return s

    def __get_sorted_list_and_global_best_solution(self, population=None, isReverse=False):
        """ Sort population and return the sorted population and the best position """
        sorted_pop = sorted(population, key=lambda ks: ks.fitness, reverse=isReverse)
        copy = SlimeMouldSolution.init_solution(sorted_pop[0])
        return sorted_pop, copy
        #return sorted_pop, deepcopy(sorted_pop[0])

    def __amend_position(self, position=None):
        return clip(position, self.lb, self.ub)

    def calculate_w(self, listSearchAgent, s):
        # calculate weight. EQ 6
        for i in range (self.popsize):
            if i <= int(self.popsize / 2):
                listSearchAgent[i].w = 1 + uniform(0, 1) * log10((listSearchAgent[0].fitness - listSearchAgent[i].fitness) / s + 1)
            else:   
                listSearchAgent[i].w = 1 - uniform(0, 1) * log10((listSearchAgent[0].fitness - listSearchAgent[i].fitness) / s + 1)

    def __validate_feasible_solutions(self):
        pass

    def __gausian(self):
        pass
       
    def __str__(self) -> str:
        return super().__str__() + ".Slime_Mould_Algorithm"
