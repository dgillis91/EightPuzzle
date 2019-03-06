# -*- coding: utf-8 -*-

'''
Potential adds - modularize to allow differing solution methods. Ex. BFS, DFS.
'''

from Solver import Solver

class SolutionSummary:
    def __init__(self, sample_count, cost_functions):
        self._sample_count = sample_count
        self._cost_functions = cost_functions
        self._data = {}
        self._prep_data()

    @property
    def data(self):
        return self._data
        
    def _prep_data(self):
        for cost_function in self._cost_functions:
            self._data[cost_function.__name__] = []
    
    def generate_data(self):
        for cost_function in self._cost_functions:
            for sample in range(self._sample_count):
                solver = Solver(cost_function)
                solution = solver.solve()
                self._data[cost_function.__name__].append((len(solution), 
                          solver.expanded_path_count))

def manhattan_distance(state):
    total = 0
    for i in range(len(state)):
        total += abs(state[i] - i)
    return total

def hamming_distance(state):
    total = 0
    for i in range(len(state)):
        total += (1 if state[i] != i else 0)
    return total

summary = SolutionSummary(40, [manhattan_distance, hamming_distance])
summary.generate_data()
header = '(path_length, expanded_paths)'
for func, data in summary.data.items():
    print('[+] {}'.format(func))
    print('\t[+] {}'.format(header))
    data.sort()
    for data_record in data:
        print('\t[+] {}'.format(data_record))