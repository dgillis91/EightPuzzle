# -*- coding: utf-8 -*-

from queue import PriorityQueue
from GameStateRandomizer import GameStateRandomizer

class Solver:
    __goal_state = list(range(9))
    
    def __init__(self, cost_function):
        self._initial_state = GameStateRandomizer(cost_function).state
        self._expanded_paths = 0
        
    @property
    def expanded_path_count(self):
        return self._expanded_paths
        
    def solve(self):
        frontier = PriorityQueue()
        frontier.put(self._initial_state)
        visited = set()
        
        while not frontier.empty():
            current_state = frontier.get()
            if self._is_goal_state(current_state):
                path = self._backsub_path(current_state)
                return path
            self._expanded_paths += 1
            for neighbor_state in current_state.possible_states():
                if neighbor_state not in visited:
                    frontier.put(neighbor_state)
            visited.add(current_state)
        return []
    
    def  _backsub_path(self, state):
        path = [state.state]
        new_state = state.parent
        while new_state.parent:
            path.append(new_state.state)
            new_state = new_state.parent
        return list(reversed(path))
    
    def _is_goal_state(self, game_state):
        state = game_state.state
        return state == self.__goal_state