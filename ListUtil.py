# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 08:49:43 2019

@author: dgill
"""

def swap(index_one, index_two, lst):
    temp = lst[index_one]
    lst[index_one] = lst[index_two]
    lst[index_two] = temp

def copy_and_swap(index_one, index_two, lst):
    new_list = [x for x in lst]
    swap(index_one, index_two, new_list)
    return new_list