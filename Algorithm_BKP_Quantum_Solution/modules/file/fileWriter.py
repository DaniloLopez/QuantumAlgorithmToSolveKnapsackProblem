# -*- coding: utf-8 -*-
#!/usr/bin/python

from modules.util.generalValue import LINE_SEPARATOR

class FileWriter:
    """class """

    def __init__(self):
        """class for write in files"""        
        self.file = ""
    
    def open(self, file_name):        
        """open file"""                
        self.file = open(file_name, 'w')

    def close(self):
        """close file"""
        self.file.close()

    def write(self, line):
        """write line in file"""
        self.file.write(line)

    def write_line(self, line):
        """write line in file ending with new line"""
        self.file.write(line)
        self.new_line()

    def new_line(self):
        """new line"""
        self.file.write(LINE_SEPARATOR)
    
    