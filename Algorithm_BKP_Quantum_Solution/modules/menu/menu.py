# -*- coding: utf-8 -*-
#!/usr/bin/python

#necessary packages 
import argparse

class Menu:

    def __init__(self,description="", epilog=""):
        """program menu"""
        self.description = description
        self.epilog = epilog
        self.parser = argparse.ArgumentParser(description=self.description, epilog=self.epilog)
        print("por aqui pase")
        #list of parameters
        self.args = self.parser.parse_args()
        self.defineDefaultParameters()

    def defineDefaultParameters(self):
        #parameters defined to terminal
        print("por aqui pase")
        self.parser.add_argument("-i", "--iterations", help="Number of iterations to run each file with a knapsack")

    def add_parameter_positional(self, short, long, help=""):
        self.parser.add_argument(short, long, help)

    def add_parameter_optional(self, arg, help=""):
        self.parser.add_argument(arg, help)