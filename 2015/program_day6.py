# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 22:43:03 2024

@author: andre
"""

import re

def find_lights_on(input_file: str) -> int:
    with open(input_file) as f:
        instructions = f.read().strip().splitlines()
    h = l = 1000
    grid = [[0]*l for _ in range(h)]
    for instruction in instructions:
        regex = r'\d+'
        nums = re.findall(regex, instruction)
        x1, y1, x2, y2 = map(int, nums)
        if 'turn on' in instruction:
            for y in range(y1, y2+1):
                for x in range(x1, x2+1):
                    grid[y][x] = 1
        elif 'turn off' in instruction:
            for y in range(y1, y2+1):
                for x in range(x1, x2+1):
                    grid[y][x] = 0
        elif 'toggle' in instruction:
            for y in range(y1, y2+1):
                for x in range(x1, x2+1):
                    grid[y][x] = (grid[y][x]+1) % 2
    # with open('grid_day6.txt', 'w') as f:
    #     print('\n'.join(''.join(map(str, line)) for line in grid), file= f)
    ans = 0
    for y in range(h):
        for x in range(l):
            ans += grid[y][x]
    return ans

def find_brightness(input_file: str) -> int:
    with open(input_file) as f:
        instructions = f.read().strip().splitlines()
    h = l = 1000
    grid = [[0]*l for _ in range(h)]
    for instruction in instructions:
        regex = r'\d+'
        nums = re.findall(regex, instruction)
        x1, y1, x2, y2 = map(int, nums)
        if 'turn on' in instruction:
            for y in range(y1, y2+1):
                for x in range(x1, x2+1):
                    grid[y][x] += 1
        elif 'turn off' in instruction:
            for y in range(y1, y2+1):
                for x in range(x1, x2+1):
                    if grid[y][x] > 0:
                        grid[y][x] -= 1
        elif 'toggle' in instruction:
            for y in range(y1, y2+1):
                for x in range(x1, x2+1):
                    grid[y][x] += 2
    ans = 0
    for y in range(h):
        for x in range(l):
            ans += grid[y][x]
    return ans


if __name__ == '__main__':
    print(find_lights_on('input_day6.txt'))
    print(find_brightness('input_day6.txt'))