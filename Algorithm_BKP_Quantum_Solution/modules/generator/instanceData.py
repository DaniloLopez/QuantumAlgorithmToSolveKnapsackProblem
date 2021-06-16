#  usr/bin/env
# -*- coding: utf-8 -*-

class InstanceData():
    def __init__(self, n_items ,range, type_corr, n_instances, n_test):
        self.n_items = n_items
        self.range = range
        self.type_corr = type_corr
        self.n_instances = n_instances
        if n_test is None:
            self.n_test = 1000
        else:
            self.n_test = n_test

