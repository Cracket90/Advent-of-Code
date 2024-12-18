# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 00:29:10 2024

@author: andre
"""

def find_houses(input_file: str) -> int:
    dirs = {'^': (0,-1), 'v': (0,1), '>': (1,0), '<': (-1,0)}
    pos = set()
    pos.add((0,0))
    with open(input_file) as f:
        data = f.read().strip()
    x = y = 0
    for char in data:
        dx, dy = dirs.get(char)    # type: ignore
        x += dx
        y += dy
        pos.add((x, y))
    return len(pos)

def find_robo_houses(input_file: str) -> int:
    dirs = {'^': (0,-1), 'v': (0,1), '>': (1,0), '<': (-1,0)}
    pos = set()
    pos.add((0,0))
    with open(input_file) as f:
        data = f.read().strip()
    xS = yS = xR = yR = 0
    for index, char in enumerate(data):
        dx, dy = dirs.get(char)    # type: ignore
        if index % 2:
            xR += dx
            yR += dy
            pos.add((xR, yR))
        else:
            xS += dx
            yS += dy
            pos.add((xS, yS))
    return len(pos)

if __name__ == '__main__':
    print(find_houses('input_day3.txt'))
    print(find_robo_houses('input_day3.txt'))