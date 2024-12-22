# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 13:13:24 2024

@author: andre
"""

def find_cheats(input_file: str) -> int:
    with open(input_file) as f:
        race_map = f.read().strip().split('\n')
    h, l = len(race_map), len(race_map[0])
    dirs = [(0,-1), (1,0), (0,1), (-1,0)]
    for y in range(h):
        for x in range(l):
            if race_map[y][x] == 'S':
                yS, xS = y, x
            elif race_map[y][x] == 'E':
                yE, xE = y, x
    single_path = {}
    single_path[(yS,xS)] = 0
    y, x = yS, xS
    picosec = 0
    while (y,x) != (yE,xE):
        for dx, dy in dirs:
            yn, xn = y+dy, x+dx
            if race_map[yn][xn] in '.E' and (yn,xn) not in single_path:
                picosec += 1
                single_path[(yn,xn)] = picosec
                y, x = yn, xn
                break
    ans = 0
    dist = 2
    for y, x in single_path:
        for dx, dy in dirs:
            yn, xn = y+dy, x+dx
            if race_map[yn][xn] == '#' and (yn+dy,xn+dx) in single_path:
                save = single_path[(yn+dy,xn+dx)] - single_path[(y,x)] - dist
                if save >= 100:
                    ans += 1
    return ans

def find_updated_cheats(input_file: str) -> int:
    with open(input_file) as f:
        race_map = f.read().strip().split('\n')
    h, l = len(race_map), len(race_map[0])
    dirs = [(0,-1), (1,0), (0,1), (-1,0)]
    for y in range(h):
        for x in range(l):
            if race_map[y][x] == 'S':
                yS, xS = y, x
            elif race_map[y][x] == 'E':
                yE, xE = y, x
    single_path = {}
    single_path[(yS,xS)] = 0
    y, x = yS, xS
    picosec = 0
    while (y,x) != (yE,xE):
        for dx, dy in dirs:
            yn, xn = y+dy, x+dx
            if race_map[yn][xn] in '.E' and (yn,xn) not in single_path:
                picosec += 1
                single_path[(yn,xn)] = picosec
                y, x = yn, xn
                break
    ans = 0
    for y, x in single_path:
        for yn in range(y-20, y+21):
            for xn in range(x-20+abs(yn-y), x+21-abs(yn-y)):
                if (yn,xn) in single_path:
                    dist = abs(y-yn) + abs(x-xn)
                    diff = single_path[(yn,xn)] - single_path[(y,x)]
                    save = diff - dist
                    if save >= 100:
                        ans += 1
    # for y, x in single_path:
    #     for yn, xn in single_path:
    #         dist = abs(y-yn) + abs(x-xn)
    #         diff = single_path[(yn,xn)] - single_path[(y,x)]
    #         if 2 <= dist <= 20 and diff > dist:
    #             save = diff - dist
    #             if save >= 100:
    #                 ans += 1
    return ans

if __name__ == '__main__':
    print(find_cheats('input_day20.txt'))
    print(find_updated_cheats('input_day20.txt'))