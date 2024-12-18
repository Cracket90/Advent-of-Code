# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 12:12:48 2024

@author: andre
"""

def find_lowest_score(input_file: str) -> int:
    with open(input_file) as f:
        maze = f.read().strip().split('\n')
    h, l = len(maze), len(maze[0])
    yS, xS, dS = h-2, 1, '>'
    yE, xE = 1, l-2
    paths = find_paths(maze, yS, xS, dS, yE, xE)
    return paths[(yE, xE)]

def find_tiles(input_file: str) -> int:
    with open(input_file) as f:
        maze = f.read().strip().split('\n')
    h, l = len(maze), len(maze[0])
    # maze = [list(line) for line in maze]
    # print('\n'.join(''.join(line) for line in maze)+'\n')
    yS, xS, dS = h-2, 1, '>'
    yE, xE = 1, l-2
    best_paths = find_best_paths(maze, yS, xS, dS, yE, xE)
    tiles = best_paths[min(best_paths.keys())]
    # print(min(best_paths.keys()))
    # for y, x in tiles:
    #     maze[y][x] = 'o'
    # print('\n'.join(''.join(line) for line in maze)+'\n')
    return len(tiles)

def find_paths(maze: list[str], yR: int, xR: int, dR: str, yE: int, xE: int,
               score: int = 0, paths: dict[tuple,int]|None = None) -> dict[tuple,int]:
    if paths is None:
        paths = {}
    if (yE, xE) in paths and score >= paths[(yE, xE)]:
        return {}
    if (yR, xR) in paths and score >= paths[(yR, xR)]:
        return {}
    paths[(yR, xR)] = score
    if (yR, xR) == (yE, xE):
        return paths
    dirs = {'^': (0,-1), '>': (1,0), 'v': (0,1), '<': (-1,0)}
    next_dirs = {'^': '^<>', '>': '>^v', 'v': 'v<>', '<': '<^v'}
    for d in next_dirs[dR]:
        dx, dy = dirs[d]
        x = xR + dx
        y = yR + dy
        if maze[y][x] != '#':
            if d == dR:
                find_paths(maze, y, x, d, yE, xE, score+1, paths)
            else:
                find_paths(maze, y, x, d, yE, xE, score+1001, paths)
    return paths

def find_best_paths(maze: list[str], yR: int, xR: int, dR: str, yE: int, xE: int,
                    score: int = 0, path: set[tuple]|None = None, paths: dict[tuple,int]|None = None,
                    best_paths: dict[int,set]|None = None) -> dict[int,set]:
    if path is None:
        path = set()
    if paths is None:
        paths = {}
    if best_paths is None:
        best_paths = {}
    if (yE, xE) in paths and score > paths[(yE, xE)]:
        return {}
    if (yR, xR) in paths and score > paths[(yR, xR)]+1000:
        return {}
    paths[(yR, xR)] = score
    path.add((yR, xR))
    if (yR, xR) == (yE, xE):
        best_paths[score] = best_paths.get(score, set()) | path
        return best_paths
    dirs = {'^': (0,-1), '>': (1,0), 'v': (0,1), '<': (-1,0)}
    next_dirs = {'^': '^<>', '>': '>^v', 'v': 'v<>', '<': '<^v'}
    for d in next_dirs[dR]:
        dx, dy = dirs[d]
        x = xR + dx
        y = yR + dy
        if maze[y][x] != '#':
            if d == dR:
                find_best_paths(maze, y, x, d, yE, xE, score+1, path.copy(), paths, best_paths)
            else:
                find_best_paths(maze, y, x, d, yE, xE, score+1001, path.copy(), paths, best_paths)
    return best_paths

if __name__ == '__main__':
    print(find_lowest_score('input_day16.txt'))
    print(find_tiles('input_day16.txt'))