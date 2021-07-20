#!/usr/bin/env python3
# coding=utf-8

import operator

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

    def quantum_initialization(self):
         pass

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
        my_weight = (
            self._turn_off_random(selected, my_weight) 
            if self.my_container.my_aleatory.random() < 0.2 
            else self._turn_off_density(selected, my_weight)
        )
        my_weight = self._leave_only_valid_unselected_items(my_weight)
        my_weight = self._turn_off_random(selected, my_weight)
        my_weight = self._complete(unselected, my_weight)
        self.evaluate()

    def calculate_weight(self):
        self.weight = 0.0
        for i in range(len(self.position)):
            if(self.position[i] == 1):
                self.weight += self.my_container.my_knapsack.weight(i)
        
    def evaluate(self):
        self.my_container.current_efos += 1 
        self.calculate_weight();
        if self.weight > self.my_container.my_knapsack.capacity :
            self.fitness = 0
        else:
            self.fitness = self.my_container.my_knapsack.evaluate(
                self.position
            )

    def modify(self, value):
        pass

    def _define_selected_unselected_list(self, selected, unselected):
        selected = []
        unselected = []
        my_weight = 0.0
        for i in range(len(self.position)):
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

    def _turn_off_random(self, selected, my_weight):
        pos = self.my_container.my_aleatory.randint(0, len(self.position))
        pos_turn_off = selected[pos]
        del(selected[pos])
        self.position[pos_turn_off] = 0
        my_weight -= self.my_container.my_knapsack.weight(pos_turn_off)
        return my_weight

    def _turn_off_density(self, selected, my_weight):
        if len(selected) == 0:
            return
        by_density = dict()
        for pos_sel in selected:
            den = self.my_container.my_knapsack.density(pos_sel)
            by_density[pos_sel] = den
        by_density = sorted(by_density.items(), key=operator.itemgetter(1))
        restricted_list_size = len(by_density) / 2
        if(restricted_list_size == 0): 
            restricted_list_size = 1
        pos  = self.my_container.my_aleatory.ranint(0, len(restricted_list_size))
        pos_turn_off = by_density.keys()[pos]
        del(selected[pos_turn_off])
        self.position[pos_turn_off] = 0
        my_weight -= self.my_container.my_knapsack.weight(pos_turn_off)
        return my_weight

    #override
    def __str__(self):
        return (f"p: {self.position} f: {self.fitness} w: {self.weight} con: {self.my_container}")
        
    def __cmp__(self, other = None):
        pass