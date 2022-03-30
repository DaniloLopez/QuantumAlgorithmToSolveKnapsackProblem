from random import random
import random
import numpy as np
from numpy import math
from modules.algorithms.metaheuristics.evolutionary.grey_wolf_optimizer.greyWolfOptimizerSolution import GreyWolfSolution
from modules.algorithms.metaheuristics.populationMetaheuristic import PopulationMetaheuristic

ELITISM_WOLVES = 3
F0 = 0.02
F1 = 0.03
_e = math.e
THETA_MIN = 0.03141  # 0.01*pi
THETA_MAX = 0.09424  # 0.03*pi
_MU = 0
_SIGMA = 1
K = 10


class GreyWolf(PopulationMetaheuristic):
    """docstring for GreyWolf."""

    def __init__(self, max_efos, pop_size):  # TODO pop_size no puede ser menor a 3
        super(GreyWolf, self).__init__(pop_size, None)
        self.max_efos = max_efos

    def execute(self, the_knapsack, the_aleatory, debug=False):
        # variables
        self.my_knapsack = the_knapsack
        self.my_aleatory = the_aleatory
        self.curve = []
        self.current_efos = 0
        g_best = None   # DF - Best fitness all iterations
        Q = self.generate_population_aleatory()  # 3.3 initialization

        # get best solution - wolves alpha
        g_best = Q[0]
        pos_g_best = 0

        t = 0
        while t < self.max_efos:
            for it in range(self.pop_size):
                # get current best binary individual Xα

                # de igual manera se hacen las 10 iteraciones, no supone una mejora significativa MAX()
                # maxim = max([k.fitness for k in Q]) 
                for i in range(self.pop_size):  # TODO revisar n_item
                    if g_best.fitness < Q[i].fitness:
                        g_best = Q[i]
                        pos_g_best = i

                pos_qr1_qr2_selected = []
                # select position of qr1 and qr2 randomly
                # -1 porque ya que se tiene el alpha
                while len(pos_qr1_qr2_selected) < ELITISM_WOLVES - 1:
                    r = random.randint(0, self.pop_size - 1)
                    if r not in pos_qr1_qr2_selected and r != pos_g_best:  # TODO refactor numpy choice k=n, replace= false
                        pos_qr1_qr2_selected.append(r)

                # Apply mutation on qM(t) by Equations (8) and (11)//Adaptive mutation
                ft = self.__get_differentiation_control_factor(t)
                q_m = self.__apply_adaptive_mutation(
                    Q, pos_g_best, pos_qr1_qr2_selected, ft
                )

                # Obtain qC(t) by crossover by Equations (12) and (13)//Crossover
                q_c = self.__obtain_crossover(Q[it].quantum_theta, q_m)

                # create solution object for evaluate fitness
                q_c_solution = GreyWolfSolution.init_owner(self)
                q_c_solution.quantum_initialization(q_c)

                if q_c_solution.fitness > Q[it].fitness:
                    Q[it] = q_c_solution
                else:
                    Q[it].quantum_theta = (
                        np.array(Q[it].quantum_theta)
                        + self.__update_by_rgwo(Q.copy(), t, it)
                    ).tolist()

            t += 1
        self.my_best_solution = GreyWolfSolution.init_solution(g_best)
        return g_best

    def generate_population_aleatory(self):
        """generate population vector aleatory"""
        list_agent = []
        for i in range(self.pop_size):
            list_agent.append(self.get_instance_solution())
        return list_agent

    def get_instance_solution(self):
        """ generate an instances solution for Slime Mould. """
        s = GreyWolfSolution.init_owner(self)
        s.random_initialization()
        return s

    def __get_differentiation_control_factor(self, t):
        exp = 1 - (
            self.max_efos / (self.max_efos - t)
        )
        w = math.pow(_e, exp)
        r = round(random.uniform(0, 1), 2)
        return F0 + F1 * math.pow(2, w) * r

    def __apply_adaptive_mutation(
        self, list_search_agents, pos_alpha, pos_selected, ft
    ):
        q_o_m = []
        for i in range(len(list_search_agents[pos_alpha].quantum_theta)):
            q_o_m.append((
                np.array(list_search_agents[pos_alpha].quantum_theta[i]) + (
                    ft * (
                        np.array(
                            list_search_agents[pos_selected[0]].quantum_theta[i]
                        )
                        - np.array(
                            list_search_agents[pos_selected[1]].quantum_theta[i]
                        )
                    )
                )
            ).tolist())

        # q_o_m = list_search_agents[pos_alpha].quantum_theta + (
        #     ft * (
        #         list_search_agents[pos_selected[0]].quantum_theta   # TODO validar funcionalidad
        #         - list_search_agents[pos_selected[1]].quantum_theta
        #     )
        # )
        return q_o_m

    def __obtain_crossover(self, q_i, q_m):
        q_c = []
        cr = random.uniform(0, 1)
        rnbr_i = random.randint(0, len(q_i)-1)
        for j in range(len(q_i)):
            q_c.append(
                q_m[j]
                if random.uniform(0, 1) <= cr or rnbr_i == j
                else q_i[j]
            )
        return q_c

    def __update_by_rgwo(self, population, t, it):
        pop = sorted(population, reverse=True)  # data is ordered by fitness
        quantum_theta_crossover = []
        alpha = pop[0]
        beta = pop[1]
        gama = pop[2]
        angle = (
            THETA_MIN 
            + (1 - (t/self.max_efos)) 
            * (THETA_MAX - THETA_MIN)
        )  # equation 22

        for j in range(len(alpha.position)):
            upsilon_alpha = self.__get_upsilon_wolves(alpha, pop[it], t)
            upsilon_beta = self.__get_upsilon_wolves(beta, pop[it], t)
            upsilon_gama = self.__get_upsilon_wolves(gama, pop[it], t)

            delta_theta = angle * (
                upsilon_alpha*(alpha.position[j] - pop[it].position[j])
                + upsilon_beta*(beta.position[j] - pop[it].position[j])
                + upsilon_gama*(gama.position[j] - pop[it].position[j])
            )
            quantum_theta_crossover.append(delta_theta)
        return np.array(quantum_theta_crossover) # TODO vector s con todas las dimensiones

    def __get_upsilon_wolves(self, leader_wolves, actual_wolf, t):
        if actual_wolf.fitness < leader_wolves.fitness:
            return (
                leader_wolves.fitness / actual_wolf.fitness
                if actual_wolf.fitness > 0
                else 0
            )
        else:
            return (
                (np.random.normal(_MU, _SIGMA) * self.max_efos) 
                / (K * (self.max_efos + t))
            )
