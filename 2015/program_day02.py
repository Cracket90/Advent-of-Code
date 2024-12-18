# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 23:55:51 2024

@author: andre
"""

def find_paper(input_file: str) -> int:
    ans = 0
    with open(input_file) as f:
        data = f.read().strip().split('\n')
    dims = [line.split('x') for line in data]
    for dim in dims:
        l, w, h = list(map(int, dim))
        area = 2*l*w + 2*w*h + 2*h*l
        dim.sort(key= int)
        area += int(dim[0]) * int(dim[1])
        ans += area
    return ans

def find_ribbon(input_file: str) -> int:
    ans = 0
    with open(input_file) as f:
        data = f.read().strip().split('\n')
    dims = [line.split('x') for line in data]
    for dim in dims:
        l, w, h = list(map(int, dim))
        volume = l*w*h
        dim.sort(key= int)
        small_perimeter = 2*int(dim[0]) + 2*int(dim[1])
        ans += volume + small_perimeter
    return ans

if __name__ == '__main__':
    print(find_paper('input_day2.txt'))
    print(find_ribbon('input_day2.txt'))
