# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 09:41:20 2025

@author: andre
"""

def find_fresh_ingredients1(input_file: str) -> int:
    fresh_ingredients = 0
    with open(input_file, encoding= 'utf8') as f:
        first_section, second_section = f.read().strip().split('\n\n')
    fresh_ranges = [tuple(int(v) for v in r.split('-'))
                    for r in first_section.splitlines()]
    ingredients = [int(v) for v in second_section.splitlines()]
    for ingredient in ingredients:
        for r in fresh_ranges:
            start, end = r
            if start <= ingredient <= end:
                fresh_ingredients += 1
                break
    return fresh_ingredients

def find_fresh_ingredients2(input_file: str) -> int:
    fresh_ingredients = 0
    with open(input_file, encoding= 'utf8') as f:
        first_section = f.read().strip().split('\n\n')[0]
    fresh_ranges = sorted(tuple(int(v) for v in r.split('-'))
                          for r in first_section.splitlines())
    curr_max = -1
    for start, end in fresh_ranges:
        if start > curr_max:
            fresh_ingredients += (end - start + 1)
            curr_max = end
        elif end > curr_max:
            fresh_ingredients += (end - curr_max)
            curr_max = end
    return fresh_ingredients

if __name__ == '__main__':
    print(find_fresh_ingredients1('input_day5.txt'))
    print(find_fresh_ingredients2('input_day5.txt'))
