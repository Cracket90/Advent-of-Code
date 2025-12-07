# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 11:31:55 2025

@author: andre
"""

def find_splitting_times(input_file: str) -> int:
    with open(input_file, encoding= 'utf8') as f:
        diagram = f.read().splitlines()
    H = len(diagram)
    W = len(diagram[0])
    y_S, x_S = 0, diagram[0].index('S')
    return splitters_hit(diagram, H, W, y_S, x_S)

def splitters_hit(diagram: list[str], H: int, W: int, y_start: int, x_start: int,
                  seen_spaces: set[tuple[int,int]] | None = None) -> int:
    if seen_spaces is None:
        seen_spaces = set()
    if not (0 <= y_start < H and 0 <= x_start < W) or diagram[y_start][x_start] not in 'S.':
        return 0
    splitter = '^'
    y = y_start
    while y < H and diagram[y][x_start] != splitter and (y, x_start) not in seen_spaces:
        seen_spaces.add((y, x_start))
        y += 1
    if y >= H or (y, x_start) in seen_spaces:
        return 0
    return (1 + splitters_hit(diagram, H, W, y, x_start-1, seen_spaces)
              + splitters_hit(diagram, H, W, y, x_start+1, seen_spaces))

def find_timelines(input_file: str) -> int:
    with open(input_file, encoding= 'utf8') as f:
        diagram = f.read().splitlines()
    H = len(diagram)
    W = len(diagram[0])
    y_S, x_S = 0, diagram[0].index('S')
    return timelines(diagram, H, W, y_S, x_S)

def timelines(diagram: list[str], H: int, W: int, y_start: int, x_start: int,
              cache: dict[tuple[int,int],int] | None = None) -> int:
    if cache is None:
        cache = {}
    if not (0 <= y_start < H and 0 <= x_start < W) or diagram[y_start][x_start] not in 'S.':
        return 0
    splitter = '^'
    y = y_start
    while y < H and diagram[y][x_start] != splitter:
        y += 1
    if y >= H:
        return 1
    if (y, x_start) in cache:
        return cache[(y, x_start)]
    total = 0
    total += timelines(diagram, H, W, y, x_start-1, cache)
    total += timelines(diagram, H, W, y, x_start+1, cache)
    cache[(y, x_start)] = total
    return total


if __name__ == '__main__':
    print(find_splitting_times('input_day7.txt'))
    print(find_timelines('input_day7.txt'))
