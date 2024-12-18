# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 07:25:43 2024

@author: andre
"""

import copy

def find_positions(input_file: str) -> int:
    pos = {'^': (0,-1), '>': (1,0), 'v': (0,1), '<': (-1,0)}
    next_pos = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    with open(input_file) as f:
        text = f.read().strip().split('\n')
    data = [list(line) for line in text]
    h, l = len(data), len(data[0])
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char in '^>v<':
                pos_y = y
                pos_x = x
                mod = char
    while True:
        data[pos_y][pos_x] = 'X'
        dx, dy = pos.get(mod)   # type: ignore
        pos_y += dy
        pos_x += dx
        if not (0 <= pos_y < h and 0 <= pos_x < l):
            break
        if data[pos_y][pos_x] == '#':
            mod = next_pos.get(mod)    # type: ignore
            pos_y -= dy
            pos_x -= dx
    # for y, line in enumerate(data):
    #     for x, char in enumerate(line):
    #         print(char, sep='', end='')
    #     print()
    num_X = [line.count('X') for line in data]
    ans = sum(num_X)
    return ans

def find_obstructions(input_file: str) -> int:
    ans = 0
    pos = {'^': (0,-1), '>': (1,0), 'v': (0,1), '<': (-1,0)}
    next_pos = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    with open(input_file) as f:
        text = f.read().strip().split('\n')
    data = [list(line) for line in text]
    h, l = len(data), len(data[0])
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char in '^>v<':
                pos_y_in = y
                pos_x_in = x
                mod_in = char
    first_map = copy.deepcopy(data)
    pos_y = pos_y_in
    pos_x = pos_x_in
    mod = mod_in
    while True:
        first_map[pos_y][pos_x] = 'X'
        dx, dy = pos.get(mod)   # type: ignore
        pos_y += dy
        pos_x += dx
        if not (0 <= pos_y < h and 0 <= pos_x < l):
            break
        if first_map[pos_y][pos_x] == '#':
            mod = next_pos.get(mod)    # type: ignore
            pos_y -= dy
            pos_x -= dx
    # for y, line in enumerate(first_map):
    #     for x, char in enumerate(line):
    #         print(char, sep='', end='')
    #     print()
    positions = []
    for y, line in enumerate(first_map):
        for x, char in enumerate(line):
            if char == 'X':
                positions.append((y, x))
    positions.remove((pos_y_in, pos_x_in))
    # print(positions)
    # print(len(positions))
    maps = []
    for position in positions:
            modified_map = copy.deepcopy(data)
            modified_map[position[0]][position[1]] = '0'
            maps.append(modified_map)
    # for current_map in maps:
    #     for y, line in enumerate(current_map):
    #         for x, char in enumerate(line):
    #             print(char, sep='', end='')
    #         print()
    # num = 0
    for current_map in maps:
        # print('sto controllando numero:', num)
        # print(positions[num])
        pos_y = pos_y_in
        pos_x = pos_x_in
        mod = mod_in
        while True:
            current_map[pos_y][pos_x] = 'X'
            dx, dy = pos.get(mod)   # type: ignore
            pos_y += dy
            pos_x += dx
            if not (0 <= pos_y < h and 0 <= pos_x < l):
                break
            if current_map[pos_y][pos_x] == '#':
                current_map[pos_y][pos_x] = '1'
                mod = next_pos.get(mod)    # type: ignore
                pos_y -= dy
                pos_x -= dx
            elif current_map[pos_y][pos_x] in '01234':
                current_map[pos_y][pos_x] = str(int(current_map[pos_y][pos_x]) + 1)
                mod = next_pos.get(mod)    # type: ignore
                pos_y -= dy
                pos_x -= dx
            elif current_map[pos_y][pos_x] == '5':
                ans += 1
                # print('risposta è:', ans)
                break
        # num += 1
    return ans

if __name__ == '__main__':
    print(find_positions('input_day6.txt'))
    print(find_obstructions('input_day6.txt'))
