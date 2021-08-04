# -*- coding: utf-8 -*-

class Knapsack():
    """docstring for Knapsack."""

    def __init__(self, n, capacity, file_name=None):
        """ Information about of knapsack """
        self.n_items = n
        self.capacity = capacity
        self.items = []
        self.objective = 0
        self.solution = []
        self.quantum_solution = []
        self.file_name = file_name

    def is_equal_solution(self, list_solution):
        """compares solution"""
        if(len(self.solution) != len(list_solution)):             
            return False
        else:             
            for i in range(0,len(self.solution)):
                if(self.solution[i] != list_solution[i]): 
                    return False
        return True 

    def calculate_knapsack_value_weight(self, solution):
        sum_value = 0
        sum_weight = 0
        for i in range(len(solution)):
            sum_value += int(solution[i]) * self.items[i].value
            sum_weight += int(solution[i]) * self.items[i].weight
        return sum_value, sum_weight

    def evaluate(self, dim):
        sum = 0
        for i in range(self.n_items):
            sum += dim[i] * self.items[i].value
        return sum

    def weight(self, index):
        return self.items[index].weight

    def density(self, index):
        return self.items[index].density

    #setters
    def add_item_to_item_list(self, item):
        """ add an item to solution list """
        self.items.append(item)

    def get_profits(self):
        return [p.value for p in self.items]

    def get_weights(self):
        return [p.weight for p in self.items]

    # metodo para comparar objetos
    def __cmp__(self, other):
        if self.n_items == other.n_items:
            return 1 if self.capacity > other.capacity else -1
        elif self.n_items < other.n_items:
            return -1
        else:
            return 1    

    # toString
    def __str__(self):
        """ to_string function to print information from a knapsack instance"""
        line = "{ \"FILE_NAME\": " + str(self.file_name) +\
            ",    \"N_ITEM\": " + str(self.n_items) +\
            ",    \"CAPACITY\": " + str(self.capacity) +\
            ",    \"OBJECTIVE\": " + str(self.objective) +\
            ",    \"SOLUTION\": " + str(self.solution) + " }"
        return line