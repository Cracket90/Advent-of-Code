# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 10:43:23 2025

@author: andre
"""

def find_suitable_regions(input_file: str) -> int:
    with open(input_file, encoding= 'utf8') as f:
        *presents, regions = f.read().split('\n\n')
    shapes = [present.count('#') for present in presents]
    suitable_regions = 0
    for region in regions.splitlines():
        size, shapes_list = region.split(':')
        width, length = map(int, size.split('x'))
        quantities = [int(quantity) for quantity in shapes_list.split()]
        if sum(s * q for s, q in zip(shapes, quantities)) <= width * length:
            suitable_regions += 1
    return suitable_regions


if __name__ == '__main__':
    print(find_suitable_regions('input_day12.txt'))
    print('Merry Christmas and Happy New Year!')
