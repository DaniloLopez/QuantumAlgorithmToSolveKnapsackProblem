#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import modules.util.util as util
import modules.util.generalValue as general

class DatasetGenerator():

    def __init__(self, args):
        self.args = args            

    def generate(self):
        self.validate_arguments()
        self.generate_type()

    def validate_arguments(self):
        self._validate_duplicate_arguments_type()
        self._validate_type()
        
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
        if sum(self.args.type) <= 10 and len(self.args) <= 4 :
            if 1 in self.args.type :
                self.generate_uncorrelated()
            if 2 in self.args.type :
                self.generate_weakly_correlation()
            if 3 in self.args.type :
                self.generate_strongly_correlation()
            if 4 in self.args.type:
                self.generate_subset_sum()
        else:
            raise Exception("Bad arguments for parameter -t/-T ")
        
    def _generate_difficult(self):
        if sum(self.args.type) <= 6 and len(self.args) <= 4 :
            if 1 in self.args.difficult :
                pass
            if 2 in self.args.difficult :
                pass
            if 3 in self.args.difficult :
                pass
            if 0 in self.args.difficult :
                pass
        else:
            raise Exception("Bad arguments for parameter -d/-D ")

    def generate_difficult(self):
        """generate dataset low difficult"""
        self.generate(general.EASY)
        self.generate(general.MEDIUM)
        self._generate(general.HARD)
    
    def _generate(self, difficult):
        for type in self.args.type :
            for nitems in range(self.args.nitems[0], self.args.nitems[1]+1):
                for range in range(self.args.range[0], self.args.range[1]):
                    file_name = util.build_commnad_line_text_generate(
                        type, 
                        difficult, 
                        nitems, 
                        range, 
                        3
                    )
                    os.system(difficult + " " + file_name)