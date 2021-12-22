import operator
import modules.util.generalValue as general


class Solution():
    """docstring for Solution."""

    def __init__(self):
        raise RuntimeError

    @classmethod
    def init_owner(cls, owner):
        obj_solution = cls.__new__(cls)
        obj_solution.my_container = owner
        obj_solution.position = [
            0 for k in range(obj_solution.my_container.my_knapsack.n_items)
        ]
        obj_solution.fitness = None
        obj_solution.weight = None

        return obj_solution

    @classmethod
    def init_solution(cls, solution):
        obj_solution = cls.__new__(cls)
        obj_solution.position = solution.position.copy()
        obj_solution.fitness = solution.fitness
        obj_solution.weight = solution.weight
        obj_solution.my_container = solution.my_container
        return obj_solution

    def random_initialization(self, theRandom=None):
        selected = []
        unselected = []
        my_weight = self._define_selected_unselected_list(selected, unselected)
        my_weight = self.__complete(unselected, my_weight)
        self.evaluate()

    def tweak(self):
        selected = []
        unselected = []
        my_weight = self._define_selected_unselected_list(selected, unselected)
        # operador terciario que se evalua según la probabilidad escogida
        my_weight = (
            self.__turn_off_random(selected, my_weight)
            if self.my_container.my_aleatory.random() < general.ZERO_DOT_TWO
            else self.__turn_off_density(selected, my_weight)
        )
        self.__leave_only_valid_unselected_items(unselected, my_weight)
        my_weight = self.__turn_on_random(unselected, my_weight)
        my_weight = self.__complete(unselected, my_weight)
        self.evaluate()

    def calculate_weight_solution(self):
        self.weight = 0.0
        for i in range(len(self.position)):
            if self.position[i] == 1:
                self.weight += self.my_container.my_knapsack.weight(i)

    def calculate_fitness_solution(self, weight):
        self.fitness = self.my_container.my_knapsack.evaluate(self.position)
        if weight > self.my_container.my_knapsack.capacity:
            self.fitness = 0

    def evaluate(self):
        self.my_container.current_efos += 1
        self.calculate_weight_solution()
        self.calculate_fitness_solution(self.weight)

    def modify(self, value):
        binary = []
        #binary = Convert.ToString(value, 2)
        self.weight = 0
        j = 0
        for i in range(len(binary)):
            self.position[j] = int(binary[i])
            if self.position[j] == 1:
                self.weight += self.my_container.my_knapsack.weight(j)
            j += 1
        self.evaluate()

    def _define_selected_unselected_list(self, selected, unselected):
        selected.clear()
        unselected.clear()
        my_weight = 0.0
        for i in range(len(self.position)):
            if self.position[i] == 1:
                selected.append(i)
                my_weight += self.my_container.my_knapsack.weight(i)
            else:
                unselected.append(i)
        return my_weight

    def __complete(self, unselected, my_weight):
        weight = my_weight
        while True:
            self.__leave_only_valid_unselected_items(unselected, weight)
            if unselected:
                weight = self.__turn_on_random(unselected, weight)
            else:
                break
        return weight

    def __leave_only_valid_unselected_items(self, unselected, my_weight):
        free_space = self.my_container.my_knapsack.capacity - my_weight
        for i in range(len(unselected)-1, -1, -1):
            if self.my_container.my_knapsack.weight(unselected[i]) > free_space:
                unselected.pop(i)

    def __turn_on_random(self, unselected, my_weight):
        """Escoger aleatoriamente un elemento de la lista de no seleccionados, 
        eliminarlo y activar el vector posicion[] con el dato escogido 
        convirtiendolo a uno"""
        if unselected:
            pos = self.my_container.my_aleatory.randint(0, len(unselected)-1)
            pos_turn_on = unselected[pos]
            unselected.pop(pos)  # delete item from unselected list
            self.position[pos_turn_on] = 1
            my_weight += self.my_container.my_knapsack.weight(pos_turn_on)
        return my_weight

    def __turn_off_random(self, selected, my_weight):
        pos = self.my_container.my_aleatory.randint(0, len(selected)-1)
        pos_turn_off = selected[pos]
        selected.pop(pos)
        self.position[pos_turn_off] = 0
        my_weight -= self.my_container.my_knapsack.weight(pos_turn_off)
        return my_weight

    def __turn_off_density(self, selected, my_weight):
        if not selected:
            return
        by_density = dict()
        for pos_sel in selected:
            den = self.my_container.my_knapsack.density(pos_sel)
            by_density[pos_sel] = den
        # here variable density is changed to tuple
        by_density = sorted(by_density.items(), key=operator.itemgetter(1))
        # elitism operation
        restricted_list_size = int(len(by_density) / 2)
        if restricted_list_size == 0:
            restricted_list_size = 1
        pos = self.my_container.my_aleatory.randint(0, restricted_list_size-1)
        pos_turn_off = by_density[pos][0]
        selected.remove(pos_turn_off)
        self.position[pos_turn_off] = 0
        my_weight -= self.my_container.my_knapsack.weight(pos_turn_off)
        return my_weight

    # override
    def __str__(self):
        return " [weight: " + str(self.weight) +\
            ",fitness: " + str(self.fitness) +\
            ",solution_found: " + str(self.position) + "] "
