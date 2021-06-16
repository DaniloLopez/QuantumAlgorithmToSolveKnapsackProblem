# -*- coding: utf-8 -*-
#!/usr/bin/python

from modules.knapsack.knapsack import Knapsack
from modules.knapsack.item import Item

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

        if line:
            k.set_solution([int (i) for i in line.split()])
        f.close()
        return k

def read_file_knapsack_generate_pisinger(file_name):
    """function for read content of a file with information of knapsack"""
    print(file_name)
    try:
        f = open(file_name, 'r+')
    except FileNotFoundError:
        print(f"el nombre {file_name} no corresponde a un archivo valido")
    except OSError:
        print(f"No se logro abrir el archivo: {file_name}")
    else:            
        line = f.readline().split()
        kd = Knapsack( int(line[0]) , int(line[1]) )
        
        for i in range( int(kd.get_n_items())):
            item_line = f.readline().split()
            kd.add_item_to_item_list(Item(i, int(item_line[0]),int(item_line[1])))            

        line = f.readline()
        #print(line)
        if(line):
            kd.set_objetive(int(line.split()[0]))
            line = f.readline()
            if line:
                kd.set_solution([int (i) for i in line.split()])
        else:
            objetive, solution = calculateOptimalSolution(kd)
            f.write(str(objetive) + "\n")
            f.write(" ".join(map(str, solution)))
            kd.set_objetive(objetive)
            kd.set_solution([int (i) for i in solution])
        f.close()
        return kd

def calculateOptimalSolution(knapsack):
    result = []
    best_result = []
    print([it.get_weight() for it in knapsack.get_items_list()])

    best_value = 0
    best_weight = 0
    best_value, best_weight = knapsack.calculate_knapsack_value_weight(format_num_binary(format(0, "b"), knapsack.get_n_items()))
    print("aqui")
    for i in range(1, pow(2, knapsack.get_n_items())):
        bin = format(i, "b")
        temp_solution = format_num_binary(bin, knapsack.get_n_items())
        v, w = knapsack.calculate_knapsack_value_weight(temp_solution)        
        print()
        print(temp_solution)
        print(" value: " + str(v) + "   wei: " + str(w))
        if(w <= knapsack.get_capacity() and v >= best_value):
            best_value,best_weight=v,w
            best_result = temp_solution
    return best_value, best_result

def format_num_binary(num, lenght):
    solution = list(num)
    for i in range(len(num), lenght):
        solution.append('0')    
    #print("sol" + str(solution))
    return solution
