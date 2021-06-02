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
        self.args = self.parser.parse_args()

    def add_parameter_positional(self, short, long, help=""):
        self.parser.add_argument(short, long, help)

    def add_parameter_optional(self, argument, help=""):
        self.parser.add_argument(argument, help)

    def getIterations(self):
        return self.args.iterations if self.args.iterations else None