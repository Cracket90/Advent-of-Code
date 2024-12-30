# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 19:24:43 2024

@author: andre
"""

from hashlib import md5

def lowest_num5(input_file: str) -> int:
    with open(input_file) as f:
        key = f.read().strip()
    num = 0
    while True:
        num += 1
        text = key + str(num)
        res = md5(text.encode('utf-8')).hexdigest()
        if res[:5] == '00000':
            break
    return num

def lowest_num6(input_file: str) -> int:
    with open(input_file) as f:
        key = f.read().strip()
    num = 0
    while True:
        num += 1
        text = key + str(num)
        res = md5(text.encode('utf-8')).hexdigest()
        if res[:6] == '000000':
            break
    return num

if __name__ == '__main__':
    print(lowest_num5('input_day4.txt'))
    print(lowest_num6('input_day4.txt'))
