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


        pass
    
    def tweak(self):
        pass

    def calculate_weight(self):
        pass
        
    def evaluate(self):
        pass

    def modify(self, value):
        pass

    def 

    #override
    def __str__(self):
        return f"p: {self.position} f: {self.fitness} w: {self.weight} con: {self.my_container}"
        
    def __cmp__(self, other = None):
        pass