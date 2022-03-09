from random import random
import numpy as np

from modules.algorithms.metaheuristics.populationMetaheuristic import PopulationMetaheuristic
from modules.algorithms.metaheuristics.population.dragonfly.dragonflySolution import DragonflySolution

class Dragonfly(PopulationMetaheuristic):
    """DragonfLy algorithm

    Args:
        PopulationMetaheuristic (pop_size, z_value): Base metaheuristic class
    """
    def __init__(self, arg):
        super(Dragonfly, self).__init__()
        self.arg = arg

    def __init__(self, max_efos, pop_size, z_value):
        super(Dragonfly, self).__init__(pop_size, z_value)
        self.max_efos = max_efos

    def execute(self, the_knapsack, the_aleatory, debug=False):
        # variables
        self.my_knapsack = the_knapsack
        self.my_aleatory = the_aleatory
        self.curve = []
        self.current_efos = 0

        source = None # Best fitness all iterations
        enemy = None # Worst fitness all iterations

        # initialize dragonfly population and step vector
        # Calculate the objective values of all dragonflies
        X = self.__initialize_dragonflies_population()
        t = 0
        while t < self.max_efos:
            source, enemy = self.__get_source_and_enemy(X)
            w, s, a, c, f, e = self.__calculate_constants(t)
            
            # get neighbors for actual iteration 
            for i in range(self.pop_size):
                neighbors_x = []
                # Find the neighboring solutions 
                # (all the dragonflies are assumed as a group in binary search spaces)
                for j in range(self.pop_size):
                    if (i != j): # not compare itself                 
                        neighbors_x.append(DragonflySolution.init_solution(X[j]))
                neighbors_no = len(neighbors_x)
                
                # Seperation 
                S=np.zeros(self.my_knapsack.n_items)
                for k in neighbors_x:
                    S = S + (np.array(k.position) - np.array(X[i].position))
                S = -S
                
                # Alignment
                sum_delta = np.zeros(self.my_knapsack.n_items)
                for a in neighbors_x:
                    sum_delta = sum_delta + a.step
                A = (np.sum(sum_delta))/neighbors_no
                
                # Cohesion
                sum_x = np.zeros(neighbors_no)
                for a in neighbors_x:
                    sum_x = sum_x + a.position
                C_temp = (np.sum(sum_x))/neighbors_no
                C = C_temp - X[i].position
                
                # Attraction to food
                F = np.array(source.position) - np.array(X[i].position)
                
                # Distraction from enemy
                E = np.array(enemy.position) - np.array(X[i].position)
            
                X[i].step = (s*S + a*A + c*C + f*F + e*E) + w*X[i].step
                X[i].position = (
                    np.array(X[i].position) + np.array(X[i].step)
                ).tolist()
                X[i].evaluate()

   
    def __initialize_dragonflies_population(self):
        population = []
        for i in range(self.pop_size):
            population.append(self.__get_instance_solution())
        return population

    def __get_instance_solution(self):
        """ generate an instances solution for Slime Mould. """
        s = DragonflySolution.init_owner(self)
        s.random_initialization()
        return s
        
    def __calculate_constants(self, t):
        # Update w, s, a, c, f, and e
        w = 0.9-t*((0.9-0.4)/self.max_efos)
        my_c = 0.1-t*((0.1-0)/(self.max_efos/2))
        if my_c < 0:
            my_c = 0
        
        s = 2 * random.uniform(0,1) * my_c # Seperation weight
        a = 2 * random.uniform(0,1) * my_c # Alignment weight
        c = 2 * random.uniform(0,1) * my_c # Cohesion weight
        f = 2 * random.uniform(0,1) # Food attraction weight
        e = my_c # Enemy distraction weight
        
        if t > (3*self.max_efos/4):
            e = 0

    def __get_source_and_enemy(self, population):
        # Update the food source and enemy
        source = None
        enemy = None
        for i in range(self.pop_size):
            # get the best fitness
            if source and population[i].fitness > source.fitness:
                source = population[i]
            else:
                source = population[i]
            # get the worst fitness
            if enemy and population[i].fitness < enemy.fitness:
                enemy = population[i]
            else:
                enemy = population[i]
        return source, enemy
        