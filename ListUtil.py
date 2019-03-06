# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 08:49:43 2019

@author: dgill
"""

from copy import deepcopy

def swap(index_one, index_two, lst):
    lst[index_one], lst[index_two] = lst[index_two], lst[index_one]

def copy_and_swap(index_one, index_two, lst):
    new_list = deepcopy(lst)
    swap(index_one, index_two, new_list)
    return new_list