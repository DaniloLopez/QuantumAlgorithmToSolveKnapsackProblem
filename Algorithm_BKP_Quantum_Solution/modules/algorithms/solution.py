#!/usr/bin/env python3
# coding=utf-8

class Solution():
    """docstring for Solution."""

    def __init__(self):
        raise RuntimeError

    @classmethod
    def init_owner(cls, owner):
        obj_solution = cls.__new__(cls)        
        obj_solution.position = []
        obj_solution.fitness = None
        obj_solution.weight = None
        obj_solution.my_container = owner
        return obj_solution

    @classmethod
    def init_solution(cls, solution):
        obj_solution = cls.__new__(cls)        
        obj_solution.position = solution.position.copy()
        obj_solution.fitness = solution.fitness
        obj_solution.weight = solution.weight
        obj_solution.my_container = solution.my_container
        return obj_solution

    def random_initialization(self):
        selected = []
        unselected = []
        my_weight = self._define_selected_unselected_list(selected, unselected)
        self._complete(unselected, my_weight)
        self.evaluate()
    
    def tweak(self):
        selected = []
        unselected = []
        my_weight = self._define_selected_unselected_list(selected, unselected)

    def calculate_weight(self):
        pass
        
    def evaluate(self):
        pass

    def modify(self, value):
        pass

    def _define_selected_unselected_list(self, selected, unselected):
        selected = []
        unselected = []
        my_weight = 0.0
        for i in range(self.position.size()):
            if(self.position[i] == 1):
                selected.append(i)
                my_weight += self.my_container.my_knapsack.weight(i)
            else:
                unselected.append(i)
        return my_weight    

    def _complete(self, unselected, my_weight):
        while True:
            self._leave_only_valid_unselected_items(unselected, my_weight)
            if not unselected:
                my_weight = self._turn_on_random(unselected, my_weight)
            else:
                break

    def _leave_only_valid_unselected_items(self, unselected, my_weight):
        free_space = self.my_container.my_knapsack.capacity - my_weight
        for i in range(len(unselected), 0, -1):
            if self.my_container.my_knapsack.weight(unselected[i])>free_space:
                del unselected[i]
    
    def _turn_on_random(self, unselected, my_weight):
        """Escoger aleatoriamente un elemento de la lista de no seleccionados, 
        eliminarlo y activar el vector posicion[] con el dato escogido 
        convirtiendolo a uno"""
        if not unselected:
            pos = self.my_container.my_aleatory.randint(0, len(unselected))
            pos_turn_on = unselected[pos]
            del unselected[pos_turn_on]
            self.position[pos_turn_on] = 1
            my_weight += self.my_container.my_knapsack.weight(pos_turn_on)
        return my_weight



    #override
    def __str__(self):
        return (f"p: {self.position} f: {self.fitness} w: {self.weight} con: {self.my_container}")
        
    def __cmp__(self, other = None):
        pass