#  usr/bin/env
# -*- coding: utf-8 -*-

from modules.util.util import get_separator
import os
from modules.util.util import build_commnad_line_generate
import modules.util.generalValue as general

class DatasetGenerator():

    def __init__(self, args):
        self.args = args
        self.validate_arguments()

    def validate_arguments(self):
        self._validate_duplicate_arguments_type()
        self._validate_type()

    def generate(self):
        self.generate_type()

    def _validate_duplicate_arguments_type(self):
        if(len(set(self.args.type)) != len(self.args.type)):
            raise Exception(general.ERR_DUPLICATED_ARGUMENT + " Review flag -t/--type")
        if(len(set(self.args.difficult)) != len(self.args.difficult)):
            raise Exception(general.ERR_DUPLICATED_ARGUMENT + " Review flag -d/--difficult")
        if(len(set(self.args.nitems)) != len(self.args.nitems)):
            raise Exception(general.ERR_DUPLICATED_ARGUMENT + " Review flag -n/--nitem")
        if(len(set(self.args.range)) != len(self.args.range)):
            raise Exception(general.ERR_DUPLICATED_ARGUMENT + " Review flag -r/--range")

    def _generate_type(self):
        if sum(self.args.type) <= 10 and len(self.args) < 4 :
            if self.args.type.__contains__(1) :
                self.generate_uncorrelated()
            if self.args.type.__contains__(2) :
                self.generate_weakly_correlation()
            if self.args.type.__contains__(3) :
                self.generate_strongly_correlation()
            if self.args.type.__contains__(4) :
                self.generate_subset_sum()
        else:
            raise Exception("Bad arguments for parameter -t/-T ")

    def generate_difficult(self):
        """generate dataset low difficult"""
        self.generate(general.EASY)
        self.generate(general.MEDIUM)
        self._generate(general.HARD)
    
    def _generate(self, difficult):
        for type in self.args.type :
            for nitems in range(self.args.nitems[0], self.args.nitems[1]+1):
                for range in range(self.args.range[0], self.args.range[1]):
                    file_name = build_commnad_line_generate(type, difficult, nitems, range, 3)
                    os.system(difficult + " " + file_name)