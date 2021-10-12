from modules.algorithms.metaheuristics.population.slime_mould.slimeMouldSolution import SlimeMouldSolution
from modules.algorithms.metaheuristics.population_metaheuristic import PopulationMetaheuristic

from numpy.random import uniform, choice
import numpy as np


class SlimeMould(PopulationMetaheuristic):
    """docstring for SlimeMould."""

    _EPSILON = 10E-10
    _U = 1.0
    _O = 0.5

    def __init__(self, max_efos, pop_size, z_value):
        super(SlimeMould, self).__init__(pop_size, z_value)
        self.max_efos = max_efos

    def execute(self, the_knapsack, the_aleatory, debug):
        # variables
        self.my_knapsack = the_knapsack
        self.my_aleatory = the_aleatory
        self.curve = []
        self.current_efos = 0

        g_best = None   # DF - Best fitness all iterations
        listSearchAgent = self.__generate_population_aleatory()

        # returns descending order list according to best fitness
        listSearchAgent, g_best = self.__get_sorted_list_and_global_best_solution(
            listSearchAgent,
            isReverse=True
        )
        t = 0
        while t < self.max_efos:
            # plus epsilon to avoid denominator zero
            s = listSearchAgent[0].fitness - \
                listSearchAgent[-1].fitness + self._EPSILON
            self.calculate_w(listSearchAgent, s)

            # The value of vb oscillates randomly between [−a, a] and gradually
            # approaches zero as the iterations increase
            a = np.arctanh(-((self.current_efos + 1) /
                             self.max_efos) + 1)  # Eq.(2.4)

            # The value of vc oscillates between [− 1,1] and tends to zero eventually
            b = 1 - (t + 1) / self.max_efos

            # Update the Position of search agents
            for i in range(0, self.pop_size):
                pos_new = None
                if uniform() < self.z:  # Eq.(2.7)
                    # rand ⋅ (UB − LB) + LB, rand < z
                    pos_new = uniform(self.lb, self.ub)
                else:
                    # Eq.(2.2)
                    p = np.tanh(
                        abs(listSearchAgent[i].fitness - g_best.fitness))
                    vb = uniform(-a, a, self.pop_size)
                    vc = uniform(-b, b, self.pop_size)
                    for j in range(0, self.pop_size):
                        # two positions randomly selected from population, apply
                        # for the whole problem size instead of 1 variable
                        id_a, id_b = choice(
                            list(set(range(0, self.pop_size)) - {i}), 2, replace=False)

                        # Eq. 12
                        #xb(t) + vb * (w *xa(t)-xb(t))
                        pos_1 = np.array(g_best.position) + np.array(vb) * (listSearchAgent[i].w * np.array(
                            listSearchAgent[id_a].position) - np.array(listSearchAgent[id_b].position))

                        # uniform(0,1) X gausian(x(t))
                        # PENDIENTE REEMPLAZAR POR GAUSSIAN
                        pos_2 = np.array(vc) * np.array(listSearchAgent[i].position)
                        pos_new = np.where(uniform(0, 1) < p, pos_1, pos_2)

                # Check bound and re-calculate fitness after each individual move
                pos_new = self.__amend_position(pos_new)

                listSearchAgent[i].position = pos_new
                # plus epsilon to avoid denominator zero
                s = listSearchAgent[0].fitness - \
                    listSearchAgent[-1].fitness + self._EPSILON
                self.calculate_w(listSearchAgent, s)
            listSearchAgent, g_best = self.__get_sorted_list_and_global_best_solution(
                listSearchAgent, isReverse=True)
            t += 1

    def __generate_population_aleatory(self):
        """generate population vector aleatory"""
        listAgent = []
        for i in range(self.pop_size):
            listAgent.append(self.__get_instance_solution())
        return listAgent

    def __get_instance_solution(self):
        """ generate an instances solution for Slime Mould. """
        s = SlimeMouldSolution.init_owner(self)
        s.random_initialization()
        return s

    def __get_sorted_list_and_global_best_solution(self, population=None, isReverse=False):
        """ sort population and return the sorted population and the best position. """
        sorted_pop = sorted(
            population, key=lambda ks: ks.fitness, reverse=isReverse)
        return sorted_pop, SlimeMouldSolution.init_solution(sorted_pop[0])

    def __amend_position(self, position=None):
        return np.clip(position, self.lb, self.ub)

    def calculate_w(self, listSearchAgent, s):
        # calculate weight. EQ 6
        for i in range(self.pop_size):
            if i <= int(self.pop_size / 2):
                listSearchAgent[i].w = 1 + uniform(0, 1) * np.log10(
                    (listSearchAgent[0].fitness - listSearchAgent[i].fitness) / s + 1)
            else:
                listSearchAgent[i].w = 1 - uniform(0, 1) * np.log10(
                    (listSearchAgent[0].fitness - listSearchAgent[i].fitness) / s + 1)

    def __get_gaussian():
        pass

    def __validate_feasible_solutions(self):
        pass

    def __str__(self) -> str:
        return super().__str__() + ".Slime_Mould_Algorithm"
