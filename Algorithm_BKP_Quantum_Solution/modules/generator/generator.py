from abc import ABC, abstractmethod

class Generator(ABC):
    """docstring for Generator."""
    def __init__(self, arguments):
        super(Generator, self).__init__()
        self.args = arguments

    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def validate_arguments(self):
        pass
    
        