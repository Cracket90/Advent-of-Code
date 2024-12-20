# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:54:29 2024

@author: andre
"""

import re

def do_multiplication(input_file: str) -> int:
    result = 0
    regex = r'mul\([0-9]?[0-9]?[0-9],[0-9]?[0-9]?[0-9]\)'
    with open(input_file) as f:
        data = f.read()
    matches = re.findall(regex,data)
    for el in matches:
        values = el[4:-1].split(',')
        result += int(values[0]) * int(values[1])
    return result

def do_better_multiplication(input_file: str) -> int:
    result = 0
    regex = r'mul\([0-9]?[0-9]?[0-9],[0-9]?[0-9]?[0-9]\)'
    with open(input_file) as f:
        data = f.read()
    do_data = data.split("do()")
    for el in do_data:
        dont_data = el.split("don't()")
        matches = re.findall(regex,dont_data[0])
        for el in matches:
            values = el[4:-1].split(',')
            result += int(values[0]) * int(values[1])
    return result

if __name__ == '__main__':
    print(do_multiplication('input_day3.txt'))
    print(do_better_multiplication('input_day3.txt'))