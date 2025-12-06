# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 11:38:48 2025

@author: andre
"""

import math

def find_grand_total1(input_file: str) -> int:
    with open(input_file, encoding= 'utf8') as f:
        lines = f.readlines()
    problems = []
    for i in range(len(lines)-1):
        problems.append(list(map(int, lines[i].split())))
    operators = lines[-1].split()
    total = 0
    for i, operands in enumerate(zip(*problems)):
        match operators[i]:
            case '+':
                total += sum(operands)
            case '*':
                total += math.prod(operands)
    return total

def find_grand_total2(input_file: str) -> int:
    with open(input_file, encoding= 'utf8') as f:
        lines = f.readlines()
    H = len(lines)-1
    W = len(lines[0])
    problems = []
    operands = []
    for i in range(W):
        digits = []
        for j in range(H):
            digits.append(lines[j][i])
        value = ''.join(digits).strip()
        if value:
            operands.append(int(value))
        else:
            problems.append(operands)
            operands = []
    operators = lines[-1].split()
    total = 0
    for i, operands in enumerate(problems):
        match operators[i]:
            case '+':
                total += sum(operands)
            case '*':
                total += math.prod(operands)
    return total


if __name__ == '__main__':
    print(find_grand_total1('input_day6.txt'))
    print(find_grand_total2('input_day6.txt'))
