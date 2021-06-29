# -*- coding: utf-8 -*-
#!/usr/bin/python

#necessary packages 
import argparse

class Menu:

    def __init__(self, description="", epilog=""):
        """init program menu"""
        self.description = description
        self.epilog = epilog
        self.parser = argparse.ArgumentParser(description=self.description, epilog=self.epilog)
        self.parser.add_argument("-i", "--iterations", help="Number of iterations to run each file with a knapsack")
        
        self.parser.add_argument("-f", "--function", help="defines functionality to run. (1=generate dataset, 2=evaluate dataset, 3=generate and evaluate dataset)")
        
        self.parser.add_argument("-t", "--type", help="indicate type of correlation between items. value should be an integer number.")
        self.parser.add_argument("-d", "--difficult", help="indicate difficult of generated dataset (1=Easy, 2=Medium, 3=Hard, 0=All options).")
        self.parser.add_argument("-n", "--nitems", help="indicate quantity o fitems stored in knapsack. value should be an integer number.")
        self.parser.add_argument("-r", "--range", help="indicate range to create every file.")
        self.args = self.parser.parse_args()

    def add_parameter_positional(self, short, long, help=""):
        self.parser.add_argument(short, long, help)

    def add_parameter_optional(self, argument, help=""):
        self.parser.add_argument(argument, help)

    def getIterations(self):
        return self.args.iterations if self.args.iterations else None

    def is_generated_data(self):
        return True if int(self.args.function) == 1 else False

    def is_evaluate_data(self):
        return True if int(self.args.function) == 2 else False

    def is_generate_evaluate(self):
        return True if int(self.args.function) == 3 else False
