#!/usr/bin/python3


def best_score(a_dictionary):
    """
    gets the best value from a dictionary (greatest integer)
    """
    high_val = 0
    winner = None
    if type(a_dictionary) is dict:
        for key, value in a_dictionary.items():
            if value > high_val:
                high_val = value
                winner = key
    return winner
