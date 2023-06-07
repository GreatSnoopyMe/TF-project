from collections import deque
from settings import MAX_DEPTH, MAX_WEIGHT
from get_inputs import get_inputs
import logging
from copy import deepcopy

def warm_up(path):
    '''
    This function will prepare steps before starting to search. Steps include:
    reading input
    setting up weighted deque P
    ...
    '''
    Input_dict = get_inputs(path)

    P = {}
    for i in range(MAX_WEIGHT):
        P[i] = deque()

    

    return P, Input_dict

P, Input_dict = warm_up('examples/1.txt')

def empty(sub_deque):
    return True if len(sub_deque) == 0 else False


print(empty(P[1]))
