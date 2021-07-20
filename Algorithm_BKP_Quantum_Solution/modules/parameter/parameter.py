# -*- coding: utf-8 -*-

from modules.pattern.singleton import singleton
from abc import ABC, abstractmethod

class Parameter(ABC):
    """docstring for Parameter."""

    def __init__(self):
        super(Parameter, self).__init__()
        self.iterations = None
        self.type = None
        self.difficult = None
        self.nitems = None
        self.range = None
        self.file = None
        self.folder = None
    
    @abstractmethod
    def is_generate(self):
        pass

    @abstractmethod
    def get_arguments(self):
        return self.args