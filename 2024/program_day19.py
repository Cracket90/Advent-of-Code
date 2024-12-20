# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 17:14:01 2024

@author: andre
"""

# import re

# def find_possible_designs(input_file: str) -> int:
#     ans = 0
#     with open(input_file) as f:
#         data1, data2 = f.read().strip().split('\n\n')
#     patterns = data1.split(', ')
#     designs = data2.split('\n')
#     regex = "^(" + "|".join(patterns) + ")+$"
#     for design in designs:
#         if re.search(regex, design):
#             ans += 1
#     return ans

def find_possible_designs(input_file: str) -> int:
    ans = 0
    with open(input_file) as f:
        data1, data2 = f.read().strip().split('\n\n')
    patterns = data1.split(', ')
    designs = data2.split('\n')
    for design in designs:
        if is_possible(design, patterns):
            ans += 1
    return ans

def find_ways(input_file: str) -> int:
    ans = 0
    with open(input_file) as f:
        data1, data2 = f.read().strip().split('\n\n')
    patterns = data1.split(', ')
    designs = data2.split('\n')
    cache: dict[str,int] = {}
    for design in designs:
        ans += num_possible(design, patterns, cache)
    return ans

def is_possible(design: str, patterns: list[str]) -> bool:
    if not design:
        return True
    possible = False
    for pattern in patterns:
        if design.startswith(pattern):
            possible = is_possible(design[len(pattern):], patterns)
            if possible:
                break
    return possible

def num_possible(design: str, patterns: list[str], cache: dict[str,int]) -> int:
    if not design:
        return 1
    if design in cache:
        return cache[design]
    ans = 0
    for pattern in patterns:
        if design.startswith(pattern):
            ans += num_possible(design[len(pattern):], patterns, cache)
    cache[design] = ans
    return ans

if __name__ == '__main__':
    print(find_possible_designs('input_day19.txt'))
    print(find_ways('input_day19.txt'))