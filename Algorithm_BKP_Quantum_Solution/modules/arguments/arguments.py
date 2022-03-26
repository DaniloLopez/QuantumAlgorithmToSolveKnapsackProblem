from abc import ABC, abstractmethod

class Arguments(ABC):
    """docstring for Arguments."""

    def __init__(self):
        super(Arguments, self).__init__()
        self.iterations = None
        self.type = None
        self.difficult = None
        self.nitems = None
        self.range = None
        self.file = None
        self.folder = None
        self.debug = None
    
    @abstractmethod
    def is_generate(self):
        pass

    @abstractmethod
    def is_debug_enable(self):
        pass

    @abstractmethod
    def get_arguments(self):
        pass

    @abstractmethod
    def get_iterations(self):
        pass

    @abstractmethod
    def get_file_name(self):
        pass

    @abstractmethod
    def get_folder_name(self):
        pass