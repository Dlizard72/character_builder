from random import randint
from dataclasses import dataclass


@dataclass
class Attributes:
    Str: int
    Int: int
    Wis: int
    Dex: int
    Con: int
    Cha: int


def roll_die() -> list[int]:
    '''
    Rolls a 6 sided die 4 times and sorts
    them from least to greatest
    '''
    return sorted([randint(1, 6) for rolls in range(4)])

def drop_lowest()-> int:
    '''
    sums the highest 3 numbers
    in a list'''
    return(sum(roll_die()[1:])) 

