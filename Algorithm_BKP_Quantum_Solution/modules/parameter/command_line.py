#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from modules.parameter.arguments import Arguments
import argparse
import modules.util.generalValue as general

class CommandLineArguments(Arguments):
    """docstring for CommandLineArguments."""

    def __init__(self, description="", epilog=""):
        super(CommandLineArguments, self).__init__()
        self.description = description
        self.epilog = epilog
        #parser
        self.parser = argparse.ArgumentParser(
            prog=general.PROGRAM_NAME,
            description=self.description,
            epilog=self.epilog
        )
        #group for option File and Folder. Mutually exclusive in Parser
        self.group_file_folder =  self.parser.add_mutually_exclusive_group()
        self._init_parser_arguments()        
        #submenu generate
        self.parser_generate = None
        self._init_parser_generate()
        self._set_subcomands()
        #init variables
        self.args = self.parser.parse_args()
        self._init_variables()

    #override abstract methods
    def is_generate(self):
        return self.args.generate

    def get_arguments(self):
        return self.args
    
    #private methods
    def _init_parser_arguments(self):
        self.parser.add_argument(
            general.ARG_I,
            general.ARG_ITERATION,
            default=general.NUM_ITERATIONS_STATIC,
            type=int,
            help=general.ARGH_ITERATION
        )
        self.parser.add_argument(
            general.ARG_DB,
            general.ARG_DEBUG,            
            action="store_true",
            help=general.ARGH_DEBUG
        )
        self.group_file_folder.add_argument(
            general.ARG_FL,
            general.ARG_FILE,
            default=None,
            help=general.ARGH_FILE
        )
        self.group_file_folder.add_argument(
            general.ARG_FD,
            general.ARG_FOLDER,
            default=None,
            help=general.ARGH_FOLDER
        )        

    def _init_parser_generate(self):
        self.parser_generate = argparse.ArgumentParser(add_help=False)
        self.parser_generate.add_argument(
            general.ARG_T,
            general.ARG_TYPE,
            nargs='+',
            type=int,
            required=True,
            help=general.ARGH_TYPE
        )
        self.parser_generate.add_argument(
            general.ARG_D,
            general.ARG_DIFFICULT,
            nargs='+',
            type=int,
            required=True,
            help=general.ARGH_DIFFICULT
        )
        self.parser_generate.add_argument(
            general.ARG_N,
            general.ARG_NITEMS,
            nargs='+',
            type=int,
            required=True,
            help=general.ARGH_NITEMS
        )
        self.parser_generate.add_argument(
            general.ARG_R,
            general.ARG_RANGE,
            nargs='+',
            type=int,
            required=True,
            help=general.ARGH_RANGE
        )

    def _set_subcomands(self):
        subparser_generate = self.parser.add_subparsers(            
            title=general.SUBCOMANDS,
            dest=general.CMD_GENERATE
        )
        self.command_generate = subparser_generate.add_parser(
            general.CMD_GENERATE,
            help=general.CMDH_GENERATE,
            parents=[self.parser_generate]
        )

    def _init_variables(self):
        self.iterations = self.args.iterations
        self.file = self.args.file
        self.folder = self.args.folder        
        if(self.args.generate):
           self.type = self.args.type
           self.difficult = self.args.difficult
           self.nitems = self.args.nitems
           self.range = self.args.range
        self.debug = self.args.debug
        print(self.args)

    def __str__(self):
        return f"i: {self.iterations} type:{self.type} difficult:{self.difficult} n items:{self.nitems} range:{self.range} fl:{self.file} fd:{self.folder}"
