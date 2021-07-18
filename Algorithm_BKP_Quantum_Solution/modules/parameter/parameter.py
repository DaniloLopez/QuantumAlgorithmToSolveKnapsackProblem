# -*- coding: utf-8 -*-

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
    def abstract(self):
        pass