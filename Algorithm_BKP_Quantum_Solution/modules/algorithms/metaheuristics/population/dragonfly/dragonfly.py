import random
import numpy as np

from modules.algorithms.metaheuristics.populationMetaheuristic import PopulationMetaheuristic
from modules.algorithms.metaheuristics.population.dragonfly.dragonflySolution import DragonflySolution
from modules.algorithms.metaheuristics.population.dragonfly import DIM_DA

class Dragonfly(PopulationMetaheuristic):
    """DragonfLy algorithm

    Args:
        PopulationMetaheuristic (pop_size, z_value): Base metaheuristic class
    """
    def __init__(self, max_efos, pop_size):
        super(Dragonfly, self).__init__(pop_size, None)
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
        source = X[0]
        enemy = X[0]
        t = 1
        while t <= self.max_efos:
            source, enemy = self.__get_source_and_enemy(X, source, enemy)
            if source.fitness == 0:
                print("as")
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
                S=np.zeros(DIM_DA)
                for k in neighbors_x:
                    S = S + (np.array(k.da) - np.array(X[i].da))
                S = -S
                
                # Alignment
                sum_delta = np.zeros(DIM_DA)
                for nig in neighbors_x:
                    sum_delta = sum_delta + nig.step
                A = sum_delta / neighbors_no
                
                # Cohesion
                sum_x = np.zeros(DIM_DA)
                for nig in neighbors_x:
                    sum_x = sum_x + np.sum(nig.da)
                C_temp = sum_x / neighbors_no
                C = C_temp - X[i].da
                
                # Attraction to food
                F = np.array(source.da) - np.array(X[i].da)
                
                # Distraction from enemy
                E = np.array(enemy.da) + np.array(X[i].da)
            
                for j in range(DIM_DA):
                    X[i].step[j] = (s*S[j] + a*A[j] + c*C[j] + f*F[j] + e*E[j]) + w * X[i].step[j]
                    if X[i].step[j] > 1:
                        X[i].step[j] = 1
                    elif X[i].step[j] < -1:
                        X[i].step[j] = -1

                #equation 7
                X[i].da = (
                    np.array(X[i].da) + np.array(X[i].step)
                ).tolist()
                
                #TODO evaluate gx to get binary position vector
                X[i].evaluate()
            if(t == 9999):
                print("a")
            t += 1
        self.my_best_solution = DragonflySolution.init_solution(source)
        return source

   
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
        rate = 0.1-t*((0.1-0)/(self.max_efos/2))
        if rate < 0:
            rate = 0
        
        s = 2 * random.uniform(0,1) * rate # Seperation weight
        a = 2 * random.uniform(0,1) * rate # Alignment weight
        c = 2 * random.uniform(0,1) * rate # Cohesion weight
        f = 2 * random.uniform(0,1) # Food attraction weight
        e = rate # Enemy distraction weight
        
        if t > (3*self.max_efos/4):
            e = 0

        return w, s, a, c, f, e

    def __get_source_and_enemy(self, population, source, enemy):
        # Update the food source and enemy
        for i in range(self.pop_size):
            # get the best fitness
            if population[i].fitness > source.fitness:
                source =  population[i]

            # get the worst fitness
            if population[i].fitness < enemy.fitness:
                enemy = population[i]

        return DragonflySolution.init_solution(source), DragonflySolution.init_solution(enemy)
        