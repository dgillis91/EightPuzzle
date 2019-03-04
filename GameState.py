# -*- coding: utf-8 -*-

from ListUtil import copy_and_swap

class GameState:
    __blank_flag = 0
    def __init__(self, state, cost_function, moves=0, parent=None):
        self._state = state
        self._moves = moves
        self._parent = parent
        self._blank = self._state.index(self.__blank_flag)
        
        self._cost_function = cost_function
        
        self._cost = self._cost_function(self.state) + self.moves
        
        self._move_dict = {
            'left': self._left,
            'right': self._right,
            'up': self._up,
            'down': self._down
        }
    
    # properties
    @property
    def moves(self):
        return self._moves
    @property
    def state(self):
        return self._state
    @property
    def parent(self):
        return self._parent
    @property
    def cost(self):
        return self._cost
    @property
    def _blank_index(self):
        return self._blank
    
    def possible_states(self):
        blank_index = self._blank_index
        possible_moves = self._possible_moves()
        for possible_move in possible_moves:
            state = copy_and_swap(possible_move, blank_index, self._state)
            yield GameState(state, self._cost_function, self._moves + 1, self)
    
    def _possible_moves(self):
        possible_moves = []
        blank_index = self._blank_index
        for move, function in self._move_dict.items():
            if self._is_valid_move(move, blank_index):
                possible_moves.append(function(blank_index))
        return possible_moves
    
    def _is_valid_move(self, move, index):
        if move == 'up' and index < 3:
            return False
        elif move == 'down' and index >= 6:
            return False
        elif move == 'left' and (index % 3) == 0:
            return False
        elif move == 'right' and ((index + 1) % 3) == 0:
            return False
        else: 
            return True
    
    # move index generators
    def _left(self, index):
        return index - 1
    def _right(self, index):
        return index + 1
    def _up(self, index):
        return index - 3
    def _down(self, index):
        return index + 3
    
    # magic methods
    def __hash__(self):
        return hash(str(self._state))
    def __eq__(self, other):
        return self.__cmp__(other)
    def __cmp__(self, other):
        return self._state == other._state
    def __lt__(self, other):
        return self.cost < other.cost