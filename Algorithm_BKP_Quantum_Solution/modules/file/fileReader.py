# -*- coding: utf-8 -*-
#!/usr/bin/python

from modules.knapsack.knapsack import Knapsack
from modules.knapsack.item import Item
<<<<<<< HEAD

def read_file_knapsack(file_name):
    """read content of a file with information of knapsack and items fn"""
    f = open_file(file_name, 'r+')
    k = read_initial_values_knapsack(f)
    line = f.readline()
    if(line):
        read_objetive_solution(k, line, f)
    else:
        set_objetive_solution(k, f)
    f.close()
    return k
=======
 
def read_file_knapsack(name):
    """function for read content of a file with information of knapsack and items fn"""
    try:
        f = open(name, 'r')
    except FileNotFoundError:
        print(f"el nombre {name} no corresponde a un archivo valido")
    except OSError:
        print(f"No se logro abrir el archivo: {name}")
    else:            
        line = f.readline().split()        
        k = Knapsack( int(line[0]) , int(line[1]) )
        
        for i in range( k.get_n_items() ):
            item_line = f.readline().split()
            k.add_item_to_item_list(Item(i, int(item_line[0]),int(item_line[1])))
        
        line = f.readline()
        if(line):
            k.set_objetive(int(line))        
        line = f.readline()
>>>>>>> menu

def open_file(file_name, mode):
    """open file with name file_name"""
    try:
        return open(file_name, mode)
    except FileNotFoundError:
        print(f"File: {file_name} does not exist.")
    except OSError:
        print(f"Can not open file: {file_name}, OS error.")

def read_initial_values_knapsack(file):
    """read knapsack initial values and items"""
    line = file.readline().split()        
    k = Knapsack( int(line[0]) , int(line[1]) )        
    for i in range( k.get_n_items() ):
        item_line = file.readline().split()
        k.add_item_to_item_list(Item(i, int(item_line[0]),int(item_line[1])))
    return k

def read_objetive_solution(k, line, f):
    """read objetive and solution of a knapsack"""
    k.set_objetive(int(line))
    line = f.readline()
    if line:
        k.set_solution([int (i) for i in line.split()])
    else:
        print(f"Dataset imcomplete or corrupt. file: {file_name}")

def set_objetive_solution(kd, f):
    """generate objetive and solution for set to knapsack"""
    objetive, solution = calculateOptimalSolution(kd)
    f.write(str(objetive) + "\n")
    f.write(" ".join(map(str, solution)))
    kd.set_objetive(objetive)
    kd.set_solution([int (i) for i in solution])
    
def calculateOptimalSolution(knapsack):
<<<<<<< HEAD
    """generate optimal solution to knasack"""
    best_result = []
    print([it.get_weight() for it in knapsack.get_items_list()])
    best_value, best_weight = knapsack.calculate_knapsack_value_weight(right_justify_word(format(0, "b"), "0", knapsack.get_n_items()))
    for i in range(1, pow(2, knapsack.get_n_items())):
        bin = format(i, "b")
        temp_solution = right_justify_word(bin, "0", knapsack.get_n_items())
        v, w = knapsack.calculate_knapsack_value_weight(temp_solution)
        #print("sol: " + str(temp_solution) + "  value: " + str(v) + "   wei: " + str(w))
=======
    best_result = []
    print([it.get_weight() for it in knapsack.get_items_list()])

    best_value, best_weight = knapsack.calculate_knapsack_value_weight(format_num_binary(format(0, "b"), knapsack.get_n_items()))    
    
    for i in range(1, pow(2, knapsack.get_n_items())):
        bin = format(i, "b")
        temp_solution = format_binary_number(bin, "0", knapsack.get_n_items())
        v, w = knapsack.calculate_knapsack_value_weight(temp_solution)
        print("sol: " + str(bin) + "  value: " + str(v) + "   wei: " + str(w))
>>>>>>> menu
        if(w <= knapsack.get_capacity() and v >= best_value):
            best_value,best_weight=v, w
            best_result = temp_solution
    return best_value, best_result

<<<<<<< HEAD
def right_justify_word(text, char, lenght):
    """complete text value align right with a character"""
    return list(str(text).rjust(lenght, char)[:lenght])
=======
def format_binary_number(num, char, lenght):
    """complete value """
    return list(str(num).rjust(lenght, char)[:lenght])
>>>>>>> menu
