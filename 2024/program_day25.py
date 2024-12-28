# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 06:06:47 2024

@author: andre
"""

def lock_key_pairs(input_file: str) -> int:
    with open(input_file) as f:
        schemes = f.read().strip().split('\n\n')
    locks = []
    keys = []
    for scheme_data in schemes:
        scheme = scheme_data.split('\n')
        h, l = len(scheme), len(scheme[0])
        heights = [0]*l
        for y in range(1, h-1):
            for x in range(l):
                if scheme[y][x] == '#':
                    heights[x] += 1
        if all(el == '#' for el in scheme[0]):
            locks.append(heights)
        else:
            keys.append(heights)
    ans = 0
    for lock in locks:
        for key in keys:
            if all(lock[i] + key[i] <= h-2 for i in range(l)):
                ans += 1
    return ans

# def lock_key_pairs(input_file: str) -> int:
#     with open(input_file) as f:
#         data = f.read().strip().split('\n\n')
#     schemes = []
#     for scheme_data in data:
#         scheme = scheme_data.split('\n')
#         schemes.append(scheme)
#     ans = 0
#     h, l = len(schemes[0]), len(schemes[0][0])
#     for scheme1 in schemes:
#         for scheme2 in schemes:
#             if all((scheme1[y][x], scheme2[y][x]) != ('#', '#')
#                    for y in range(h) for x in range(l)):
#                 ans += 1
#     return ans // 2

if __name__ == '__main__':
    print(lock_key_pairs('input_day25.txt'))