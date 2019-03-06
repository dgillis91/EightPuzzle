# -*- coding: utf-8 -*-

from random import shuffle
from GameState import GameState

class GameStateRandomizer:
    def __init__(self, cost_function):
        self.cost_function = cost_function
        self._generate_solvable_state()
        self._game_state = GameState(self._state, self.cost_function)
        
    @property
    def state(self):
        return self._game_state
    
    def _generate_solvable_state(self):
        self._state = list(range(9))
        shuffle(self._state)
        while not self._is_solvable():
            shuffle(self._state)
    
    def _is_solvable(self):
        def inversion_count(array):
            inv_count = 0
            array_len = len(array)
            for i in range(array_len):
                for j in range(i + 1, array_len):
                    if (array[i] > 0 and array[j] and array[i] > array[j]):
                        inv_count += 1
            return inv_count
        def is_even(number):
            return (number % 2) == 0
        return is_even(inversion_count(self._state))