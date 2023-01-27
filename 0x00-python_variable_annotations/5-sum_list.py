#!/usr/bin/env python3
"""Type-annotated function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Type-annotated function sum_list which takes a list input_list
    of floats as argument and returns their sum as a float."""
    result = 0
    for x in input_list:
        result += x
    else:
        return result
