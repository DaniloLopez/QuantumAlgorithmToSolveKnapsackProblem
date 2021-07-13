#!/usr/bin/env python3
# coding=utf-8

class Solution():
    """docstring for Solution."""

    position = None
    fitness = None
    weight = None
    my_container = None

    def __init__(self):
        raise RuntimeError

    @classmethod
    def init_owner(cls, the_owner):
        obj_solution = cls.__new__(cls)
        obj_solution.my_container = the_owner
        obj_solution.position = []
        return obj_solution

    @classmethod
    def init_original(cls, original):
        obj_solution = cls.__new__(cls)
        obj_solution.set_my_container = original.get_my_container()
        cls.set_position(original.get_position().copy())
        cls.set_fitness(original.get_fitness())

    def random_initialization(self):
        pass
    
    def tweak(self):
        pass

    def calculate_weight(self):
        pass
        
    def evaluate(self):
        pass

    def modify(self, value):
        pass

    #getters and setters
    def get_position(self):
        return self.position

    def set_position(self, value):
        self.position = value

    def get_fitness(self):
        return self.fitness

    def set_fitness(self, value):
        self.fitness = value

    def get_weight(self):
        return self.weight

    def set_weight(self, value):
        self.weight = value

    def get_my_container(self):
        return self.my_container

    def set_my_container(self, value):
        self.my_container = value

    #override
    def __str__(self):
        pass
        
    def __cmp__(self, other = None):
        pass