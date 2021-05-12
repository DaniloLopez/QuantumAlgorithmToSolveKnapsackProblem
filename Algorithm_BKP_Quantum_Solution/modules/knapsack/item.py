# -*- coding: utf-8 -*-
#!/usr/bin/python

class Item:
    def __init__(self, p, v, w):
        self.position = p
        self.value = v
        self.weight = w
        self.density = self.value / self.weight

    @classmethod
    def setOrigin(cls):
        self.position = cls.position
        self.value = cls.value
        self.weight = cls.weight
        self.density = self.value / self.weight

    # getters
    def get_value(self):
        return self.value;

    def get_weight(self):
        return self.weight

    def get_position(self):
        return self.position

    def get_density(self):
        return self.density

    def __str__(self):
        return 'P: {}  V:{}  W:{}  D:{}'.format(self.position, self.value, self.weight, self.density)