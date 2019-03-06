# -*- coding: utf-8 -*-

'''
Potential adds - modularize to allow differing solution methods. Ex. BFS, DFS.
'''

from Solver import Solver

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
    
solver = Solver(manhattan_distance)
solution = solver.solve()
print('[+] Expanded Paths: {}'.format(solver.expanded_path_count))
print('[+] Number of Moves: {}'.format(len(solution)))
for step in solution:
    print(step)
    