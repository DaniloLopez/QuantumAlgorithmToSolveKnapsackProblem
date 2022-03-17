# -*- coding: utf-8 -*-
#!/usr/bin/python

class Item:
    def __init__(self, p, v, w):
        self.position = p
        self.value = v
        self.weight = w
        self.density = self.value / self.weight

    @classmethod
    def init_item(cls, item):
        return cls(item.position,item.value,item.weight)

    def __str__(self):
        return 'P: {}  V:{}  W:{}  D:{}'.format(
            self.position, self.value, self.weight, self.density
        )

    def __cmp__(self):
        pass