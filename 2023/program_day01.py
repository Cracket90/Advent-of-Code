# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 00:16:51 2023

@author: andre
"""

def calibration(data_file:str) -> int:
    with open(data_file) as f:
        data = f.readlines()
    calibration_values = []
    for line in data:
        list_digits = [char for char in line if char.isdigit()]
        calibration_value = int(list_digits[0] + list_digits[-1])
        calibration_values.append(calibration_value)
    return sum(calibration_values)

def calibration2(data_file:str) -> int:
    with open(data_file) as f:
        data = f.readlines()
    calibration_values = []
    for line in data:
        line = line.replace('one','o1e').replace('two','t2o').replace('three','t3e').replace(
            'four','4').replace('five','5e').replace('six','6').replace(
            'seven','7n').replace('eight','e8t').replace('nine','n9e')
        list_digits = [char for char in line if char.isdigit()]
        calibration_value = int(list_digits[0] + list_digits[-1])
        calibration_values.append(calibration_value)
    return sum(calibration_values)

if __name__ == '__main__':
    print(calibration('input_day1.txt'))
    print(calibration2('input_day1.txt'))
