# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 11:48:58 2025

@author: andre
"""

# import re
# from math import floor, log10

def find_invalid_IDs1(input_file: str) -> int:
    somma = 0
    with open(input_file, encoding= 'utf8') as f:
        intervalli = f.read().strip().split(',')
    for intervallo in intervalli:
        start, end = [int(valore) for valore in intervallo.split('-')]
        invalid_IDs = [valore for valore in range(start, end+1) if is_twice(valore)]
        somma += sum(invalid_IDs)
    return somma

def is_twice(valore: int) -> bool:
    # floor(log10(valore)+1) % 2 == 0
    valore_str = str(valore)
    len_valore = len(valore_str)
    return len_valore % 2 == 0 and valore_str[:len_valore//2] == valore_str[len_valore//2:]

def find_invalid_IDs2(input_file: str) -> int:
    somma = 0
    with open(input_file, encoding= 'utf8') as f:
        intervalli = f.read().strip().split(',')
    for intervallo in intervalli:
        start, end = [int(valore) for valore in intervallo.split('-')]
        invalid_IDs = [valore for valore in range(start, end+1) if is_repeated(valore)]
        somma += sum(invalid_IDs)
    return somma

def is_repeated(valore: int) -> bool:
    valore_str = str(valore)
    len_valore = len(valore_str)
    for len_pattern in range(len_valore//2, 0, -1):
        if len_valore % len_pattern == 0:
            pattern = valore_str[:len_pattern]
            ripetizioni = len_valore // len_pattern
            if pattern * ripetizioni == valore_str:
                return True
    return False

# def is_repeated(valore: int) -> bool:
#     valore_str = str(valore)
#     if valore_str in (valore_str*2)[1:-1]:
#         return True
#     return False

# def is_repeated(valore: int) -> bool:
#     valore_str = str(valore)
#     if re.match(r'^(.+)\1+$', valore_str):
#         return True
#     return False

# def is_repeated(valore: int) -> bool:
#     valore_str = str(valore)
#     len_valore = len(valore_str)
#     for len_pattern in range(len_valore//2, 0, -1):
#         if len_valore % len_pattern == 0:
#             pattern = valore_str[:len_pattern]
#             for index in range(len_pattern, len_valore, len_pattern):
#                 window = valore_str[index: index+len_pattern]
#                 if window != pattern:
#                     break
#             else:
#                 return True
#     return False


if __name__ == '__main__':
    print(find_invalid_IDs1('input_day2.txt'))
    print(find_invalid_IDs2('input_day2.txt'))
