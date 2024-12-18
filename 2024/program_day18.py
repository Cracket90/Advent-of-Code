# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 08:35:45 2024

@author: andre
"""

def min_steps(input_file: str) -> int:
    bytes_pos = []
    with open(input_file) as f:
        for line in f:
            xstr, ystr = line.strip().split(',')
            bytes_pos.append((int(xstr),int(ystr)))
    h, l = 71, 71
    memory_grid = [['.']*l for _ in range(h)]
    for n in range(1024):
        x, y = bytes_pos[n]
        memory_grid[y][x] = '#'
    xS, yS = 0, 0
    xE, yE = 70, 70
    steps = shortest_paths(xS, yS, xE, yE, memory_grid)
    return steps[(xE,yE)]

def byte_coordinates(input_file: str) -> str:
    bytes_pos = []
    with open(input_file) as f:
        for line in f:
            xstr, ystr = line.strip().split(',')
            bytes_pos.append((int(xstr),int(ystr)))
    h, l = 71, 71
    memory_grid = [['.']*l for _ in range(h)]
    num_bytes = len(bytes_pos)
    for n in range(num_bytes):
        x, y = bytes_pos[n]
        memory_grid[y][x] = '#'
    for m in range(num_bytes-1, 0, -1):
        # print(m)
        x, y = bytes_pos[m]
        memory_grid[y][x] = '.'
        xS, yS = 0, 0
        xE, yE = 70, 70
        steps = shortest_paths(xS, yS, xE, yE, memory_grid)
        if (xE,yE) in steps:
            break
    xB, yB = bytes_pos[m]
    return f'{xB},{yB}'

def shortest_paths(x: int, y: int, xE: int, yE: int,
                   memory_grid: list[list[str]], step: int = 0,
                   steps: dict[tuple,int]|None = None) -> dict[tuple,int]:
    if steps is None:
        steps = {}
    dirs = [(0,-1), (1,0), (0,1), (-1,0)]
    h, l = len(memory_grid), len(memory_grid[0])
    if (xE, yE) in steps and step >= steps[(yE, xE)]:
        return {}
    if (x, y) in steps and step >= steps[(x, y)]:
        return {}
    steps[(x, y)] = step
    if (x, y) == (xE, yE):
        return steps
    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy
        if nx in range(l) and ny in range(h) and memory_grid[ny][nx] != '#':
            shortest_paths(nx, ny, xE, yE, memory_grid, step+1, steps)
    return steps

if __name__ == '__main__':
    print(min_steps('input_day18.txt'))
    print(byte_coordinates('input_day18.txt'))