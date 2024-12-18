# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 17:32:09 2024

@author: andre
"""

def find_floor(input_file: str) -> int:
    with open(input_file) as f:
        data = f.read().strip()
    return data.count('(')-data.count(')')

def find_basement(input_file: str) -> int:
    floor = 0
    up = '('
    down = ')'
    with open(input_file) as f:
        data = f.read().strip()
    for index, char in enumerate(data):
        if char is up: floor += 1
        elif char is down: floor -= 1
        if floor == -1: break
    return index+1

if __name__ == '__main__':
    print(find_floor('input_day1.txt'))
    print(find_basement('input_day1.txt'))
