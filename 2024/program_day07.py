# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 09:53:33 2024

@author: andre
"""

def find_calibration(input_file: str) -> int:
    total = 0
    test_values = []
    with open(input_file) as f:
        data = f.read().strip().split('\n')
    for line in data:
        value, operands = line.split(':')
        test_values.append([int(value), list(map(int, operands.split()))[::-1]])
    for test in test_values:
        value, operands = test    # type: ignore
        calibrations = do_calculations(operands)    # type: ignore
        if value in calibrations:
            total += value    # type: ignore
    return total

def find_calibration_concat(input_file: str) -> int:
    total = 0
    test_values = []
    with open(input_file) as f:
        data = f.read().strip().split('\n')
    for line in data:
        value, operands = line.split(':')
        test_values.append([int(value), list(map(int, operands.split()))[::-1]])
    for test in test_values:
        value, operands = test    # type: ignore
        calibrations = do_calculations_concat(operands)    # type: ignore
        if value in calibrations:
            total += value    # type: ignore
    return total

def do_calculations(operands: list[int]) -> list[int]:
    if len(operands) == 1:
        return operands
    results = []
    for calculation in do_calculations(operands[1:]):
        summ = operands[0] + calculation
        prod = operands[0] * calculation
        results.append(summ)
        results.append(prod)
    return results

def do_calculations_concat(operands: list[int]) -> list[int]:
    if len(operands) == 1:
        return operands
    results = []
    for calculation in do_calculations_concat(operands[1:]):
        summ = operands[0] + calculation
        prod = operands[0] * calculation
        concat = int(str(calculation) + str(operands[0]))
        results.append(summ)
        results.append(prod)
        results.append(concat)
    return results

if __name__ == '__main__':
    print(find_calibration('input_day7.txt'))
    print(find_calibration_concat('input_day7.txt'))
