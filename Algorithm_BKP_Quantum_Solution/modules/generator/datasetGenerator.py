#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from numpy.core.fromnumeric import argmax
import modules.util.util as util
import modules.util.generalValue as general
from modules.generator.generator import Generator

class DatasetGenerator(Generator):
    """docstring for DatasetGenerator."""
    def __init__(self, arguments):
        super(DatasetGenerator, self).__init__(arguments)
    
    def generate(self):
        self.validate_arguments()
        return general.FOLDER_DATASET_GENERATED   

    def validate_arguments(self):
        self._validate_duplicate_arguments()
        self._validate_range_arguments()
        
    def _validate_duplicate_arguments(self):
        if(len(set(self.args.type)) != len(self.args.type)):
            raise Exception(
                general.ERR_DUPLICATED_ARGUMENT + " Review flag -t/--type"
            )
        if(len(set(self.args.difficult)) != len(self.args.difficult)):
            raise Exception(
                general.ERR_DUPLICATED_ARGUMENT + " Review flag -d/--difficult"
            )
        if(len(set(self.args.nitems)) != len(self.args.nitems)):
            raise Exception(
                general.ERR_DUPLICATED_ARGUMENT + " Review flag -n/--nitem"
            )
        if(len(set(self.args.range)) != len(self.args.range)):
            raise Exception(
                general.ERR_DUPLICATED_ARGUMENT + " Review flag -r/--range"
            )

    def _validate_range_arguments(self):
        self._validate_option_valid(self.args.type, 1, 4, 4)
        self._validate_option_valid(self.args.difficult, 1, 3, 3)
        self._validate_range_valid(self.args.nitems, 1,general.MAX_N_ITEMS)
        self._validate_range_valid(self.args.range, 1, general.MAX_RANGE)

    def _validate_option_valid(self, list, min_value, max_value, max_parameters):
        if(len(list) > max_parameters):
            raise Exception("parametro invalido, maximum: " + str(max_parameters) + " arguments")
        else:
            self._validate_min_max(list, min_value, max_value)

    def _validate_range_valid(self, list_eval, min_value, max_value):
        self._validate_min_max(list_eval, min_value, max_value)
        if(len(list_eval) == 2):
            list_eval = list(range(min(list_eval), max(list_eval)+1))
            
    def _validate_min_max(self, list_eval, min_value, max_value):
        if(min(list_eval) < min_value or max(list_eval) > max_value):
            raise Exception("parametro invalido, verifique el rango. valid: "  + str(min_value) + " - " + str(max_value))

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
            raise Exception(
                "<>Bad arguments for parameter (-d/-D).\t)" +
                "err: Repeated values in parameters"
            )

    def generate_by_difficult(self):
        """generate dataset low difficult"""
        self._generate(general.EASY)
        self._generate(general.MEDIUM)
        self._generate(general.HARD)
    
    def _generate(self, difficult):
        for type in self.args.type :
                for nitems in range(self.args.nitems[0], self.args.nitems[1]+1):
                    for range in range(self.args.range[0], self.args.range[1]):
                        file_name = util.build_commnad_line_text_generate (
                            type, difficult, nitems, range, 3
                        )
                        os.system(difficult + " " + file_name)
                        