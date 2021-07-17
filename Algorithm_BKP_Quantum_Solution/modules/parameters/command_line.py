# -*- coding=utf-8 -*-

import argparse
import modules.util.generalValue as general
from parameter import Parameter

class CommandLineParameter(Parameter):
    """docstring for parameters."""

    def __init__(self, description="", epilog=""):
        self.description = description
        self.epilog = epilog
        self.parser = argparse.ArgumentParser(
            prog=general.PROGRAM_NAME,
            description=self.description,
            epilog=self.epilog
        )
        self.init_parser_parameters()
        self.args = self.parser.parse_args()

    def init_parser_parameters(self):
        self._add_parameter_positional(
            general.ARG_I, general.ARG_ITERATION, general.ARG_HELP_ITERATION
        )
        self._add_parameter_positional(
            general.ARG_F, general.ARG_FUNCTION,help= general.ARG_HELP_FUNCTION
        )
        self._add_parameter_positional(
            general.ARG_T, general.ARG_TYPE, help=general.ARGH_TYPE
        )
        self._add_parameter_positional(
            general.ARG_D, general.ARG_DIFFICULT, help=general.ARGH_DIFFICULT
        )
        self._add_parameter_positional(
            general.ARG_N, general.ARG_NITEMS, help=general.ARGH_NITEMS
        )
        self._add_parameter_positional(
            general.ARG_R, general.ARG_RANGE, help=general.ARGH_RANGE
        )
        self._add_parameter_positional(
            general.ARG_FL, general.ARG_FILE, help=general.ARGH_FILE
        )
        self._add_parameter_positional(
            general.ARG_FD, general.ARG_FOLDER, help=general.ARGH_FOLDER
        )

    def _add_parameter_positional(self, short, long, help=""):
        self.parser.add_argument(short, long, help)

    def _add_parameter_optional(self, argument, help=""):
        self.parser.add_argument(argument, help)

    def getIterations(self):
        return self.args.iterations if self.args.iterations else None

    def is_generated_data(self):
        return True if int(self.args.function) == 1 else False

    def is_evaluate_data(self):
        return True if int(self.args.function) == 2 else False

    def is_generate_evaluate(self):
        return True if int(self.args.function) == 3 else False

    def get_parameters_to_generate_dataset(self):
        return self.args.type, self.args.difficult, self.args.nitems, self.range
