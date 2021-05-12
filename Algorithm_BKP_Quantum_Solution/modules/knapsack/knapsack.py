# -*- coding: utf-8 -*-
#!/usr/bin/python
import numpy as np

class Knapsack:
    def __init__(self, n, capacity):
        """ Information about of knapsack """
        self.n_items = n
        self.capacity = capacity        
        self.items = []
        self.objetive = 0
        self.solution = []

    def is_equal_solution(self, list_solution):
        """ compares solution"""
        print(f"quantum solution: {list_solution}")
        if(len(self.solution) != len(list_solution)):             
            return False
        else:             
            for i in range(0,len(self.solution)):
                if(self.solution[i] != list_solution[i]):                    
                    print("en false") 
                    return False
        return True 

    def calculate_knapsack_value_weight(self, solution):
        sum_value = 0
        sum_weight = 0
        for i in range(len(solution)):
            sum_value += int(solution[i]) * self.items[i].get_value()
            sum_weight += int(solution[i]) * self.items[i].get_weight()        
        return sum_value, sum_weight

    #setters
    def set_solution(self, s):
        """ add an item to solution list"""
        self.solution = s

    def add_item_to_item_list(self, item):
        """ """
        self.items.append(item)

    def add_element_to_item_list(self, value, weight):
        self.items.append(new )

    def set_objetive(self, obj):
        """ set objetive value for the solution """
        self.objetive = obj  

    def setCapacity(self, c):
        """set maximum capacity of knapsack"""
        self.capacity = c

    #getters
    def get_n_items(self):
        """get item quantity value"""
        return self.n_items
    
    def get_capacity(self):
        """get maximum knapsack capacity"""
        return self.capacity
    
    def get_objetive(self):
        """get objective value"""        
        return self.objetive
    
    def get_solution(self):
        """"get the given solution list"""
        return self.solution     

    def get_items_list(self):
        """"get items list"""
        return self.items

    def get_profits(self):
        return [p.get_value() for p in self.items]

    def get_weigths(self):
        return [p.get_value() for p in self.items]

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
        str = f"Number of items: {self.n_items}  "
        str += f"Capacity: {self.capacity}  "
        str += f"Objetive {self.objetive}  "
        str += f"Solution {self.solution}  "
        return str