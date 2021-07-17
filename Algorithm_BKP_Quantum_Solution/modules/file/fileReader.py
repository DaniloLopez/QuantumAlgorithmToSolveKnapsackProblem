# -*- coding: utf-8 -*-

import copy
from modules.knapsack.knapsack import Knapsack
from modules.knapsack.item import Item

class FileReader():
    """docstring for FileReader."""
    def __init__(self, file_name, mode="r+"):
        super(FileReader, self).__init__()
        self.file_name = file_name
        self.mode = mode
        self.kanapsack = None
        self.file = None
        self._read_knapsack_file()
        
    def get_knapsack(self):
        return copy.deepcopy(self.kanapsack)

    def _read_knapsack_file(self):
        """read content of a file with information of knapsack and items fn"""
        self._open_file(self.file_name, self.mode)
        if self.file:
            self._read_initial_values_knapsack()
            line = self.file.readline()
            if line:
                self._read_objetive_solution(line)
            else:
                self._set_objetive_solution()
            self.file.close()

    def _open_file(self):
        """open file with name file_name"""
        try:
            self.file = open(self.file_name, self.mode)
        except FileNotFoundError:
            print(f"File: {self.file_name} does not exist.")
        except OSError:
            print(f"Can not open file: {self.file_name}, OS error.")

    def _read_initial_values_knapsack(self):
        """read knapsack initial values and items"""
        line = self.file.readline().split()
        self.knapsack = Knapsack(int(line[0]) , int(line[1]))
        for i in range( self.knapsack.n_items ):
            item_line = self.file.readline().split()
            self.knapsack.add_item_to_item_list(
                Item(i, int(item_line[0]),int(item_line[1]))
            )

    def _read_objetive_solution(self, line):
        """read objetive and solution of a knapsack"""
        print(self.file.name)
        self.knapsack.objetive = int(line)
        line = self.file.readline()
        if line:
            self._knapsack.solution = [int (i) for i in line.split()]
        else:
            print(f"Dataset imcomplete or corrupt. file: {self.file.name}")

    def _set_objetive_solution(self):
        """generate objetive and solution for set to knapsack"""
        objetive, solution = self._calculate_optimal_solution()
        self.file.write(str(objetive) + "\n")
        self.file.write(" ".join(map(str, solution)))
        self.knapsack.set_objetive(objetive)
        self.knapsack.set_solution([int (i) for i in solution])

    def _calculate_optimal_solution(self):
        """generate optimal solution to knapsack with brute force"""
        best_result = []
        print([it.weight for it in self.knapsack.items])
        #initialize variables to zero sending zero_list 
        best_value,best_weight = self.knapsack.calculate_knapsack_value_weight(
            self._complete_text_right(
                format(0, "b"), "0", self.knapsack.get_n_items()
            )
        )
        for i in range(1, pow(2, self.knapsack.get_n_items())):
            bin = format(i, "b")
            temp_solution = self._complete_text_right(
                bin, "0", self.knapsack.get_n_items()
            )
            v, w = self.knapsack.calculate_knapsack_value_weight(temp_solution)
            if(w <= self.knapsack.get_capacity() and v >= best_value):
                best_value,best_weight=v, w
                best_result = temp_solution
        return best_value, best_result

    def _complete_text_right(self, text, char, lenght):
        """complete @text on the right according to @char @lenght"""
        return list(str(text).rjust(lenght, char)[:lenght])
