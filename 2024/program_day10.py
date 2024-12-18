# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 08:06:09 2024

@author: andre
"""

def trailheads_score(input_file: str) -> int:
    score = 0
    with open(input_file) as f:
        data = f.read().strip().split('\n')
    trail_map = [[int(value) for value in line] for line in data]
    for y, line in enumerate(trail_map):
        for x, height in enumerate(line):
            if height == 0:
                reachable_nines = search_nines(trail_map, y, x)
                score += len(reachable_nines)
    return score

def trailheads_rate(input_file: str) -> int:
    rate = 0
    with open(input_file) as f:
        data = f.read().strip().split('\n')
    trail_map = [[int(value) for value in line] for line in data]
    for y, line in enumerate(trail_map):
        for x, height in enumerate(line):
            if height == 0:
                rate += search_rate(trail_map, y, x)
    return rate

def search_nines(trail_map: list[list[int]], y: int, x: int) -> set[tuple[int,int]]:
    if trail_map[y][x] == 9:
        return {(y, x)}
    dirs = [(0,-1), (1,0), (0,1), (-1,0)]
    h, l = len(trail_map), len(trail_map[0])
    reachable_nines: set[tuple[int,int]] = set()
    for step in dirs:
        dx, dy = step
        next_x = x + dx
        next_y = y + dy
        if (next_y in range(h) and next_x in range(l) and
            trail_map[next_y][next_x] == trail_map[y][x] + 1):
            reachable_nines = reachable_nines | search_nines(trail_map, next_y, next_x)
    return reachable_nines

def search_rate(trail_map: list[list[int]], y: int, x: int) -> int:
    if trail_map[y][x] == 9:
        return 1
    dirs = [(0,-1), (1,0), (0,1), (-1,0)]
    h, l = len(trail_map), len(trail_map[0])
    hiking_trails = 0
    for step in dirs:
        dx, dy = step
        next_x = x + dx
        next_y = y + dy
        if (next_y in range(h) and next_x in range(l) and
            trail_map[next_y][next_x] == trail_map[y][x] + 1):
            hiking_trails += search_rate(trail_map, next_y, next_x)
    return hiking_trails

if __name__ == '__main__':
    print(trailheads_score('input_day10.txt'))
    print(trailheads_rate('input_day10.txt'))