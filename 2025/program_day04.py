# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 12:01:06 2025

@author: andre
"""

def find_rolls1(input_file: str) -> int:
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    accessible_rolls = 0
    paper_roll = '@'
    with open(input_file, encoding= 'utf8') as f:
        grid = f.read().strip().split('\n')
    H = len(grid)
    W = len(grid[0])
    for y in range(H):
        for x in range(W):
            if grid[y][x] == paper_roll:
                close_rolls = 0
                for dy, dx in dirs:
                    if 0 <= y+dy < H and 0 <= x+dx < W:
                        close_rolls += (grid[y+dy][x+dx] == paper_roll)
                if close_rolls < 4:
                    accessible_rolls += 1
    return accessible_rolls

def find_rolls2(input_file: str) -> int:
    with open(input_file, encoding= 'utf8') as f:
        grid = [list(line) for line in f.read().splitlines()]
    H = len(grid)
    W = len(grid[0])
    total = 0
    while True:
        removed_rolls = remove_rolls(grid, H, W)
        # print(grid)
        if removed_rolls == 0:
            break
        total += removed_rolls
    return total

def remove_rolls(grid: list[list[str]], height: int, width: int) -> int:
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    accessible_rolls: list[tuple[int, int]] = []
    paper_roll = '@'
    removed = 'x'
    for y in range(height):
        for x in range(width):
            if grid[y][x] == paper_roll:
                close_rolls = 0
                for dy, dx in dirs:
                    if 0 <= y+dy < height and 0 <= x+dx < width:
                        close_rolls += (grid[y+dy][x+dx] == paper_roll)
                if close_rolls < 4:
                    accessible_rolls.append((y, x))
    for y, x in accessible_rolls:
        grid[y][x] = removed
    return len(accessible_rolls)

def find_rolls2_faster(input_file: str) -> int:
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    paper_roll = '@'
    with open(input_file, encoding= 'utf8') as f:
        grid = [list(line) for line in f.read().splitlines()]
    H = len(grid)
    W = len(grid[0])
    rolls: dict[tuple[int,int],int] = {}
    accessible_rolls: list[tuple[int,int]] = []
    for y in range(H):
        for x in range(W):
            if grid[y][x] == paper_roll:
                close_rolls = 0
                for dy, dx in dirs:
                    if 0 <= y+dy < H and 0 <= x+dx < W:
                        close_rolls += (grid[y+dy][x+dx] == paper_roll)
                if close_rolls < 4:
                    accessible_rolls.append((y, x))
                rolls[(y, x)] = close_rolls
    starting_rolls = len(rolls)
    while accessible_rolls:
        removed = accessible_rolls.pop()
        rolls.pop(removed)
        y, x = removed
        for dy, dx in dirs:
            ny, nx = y+dy, x+dx
            if (ny, nx) in rolls:
                rolls[(ny, nx)] -= 1
                if rolls[(ny, nx)] == 3:
                    accessible_rolls.append((ny, nx))
    return starting_rolls - len(rolls)

# def find_rolls2_faster(input_file: str) -> int:
#     dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
#     total = 0
#     paper_roll = '@'
#     removed = 'x'
#     with open(input_file, encoding= 'utf8') as f:
#         grid = [list(line) for line in f.read().splitlines()]
#     H = len(grid)
#     W = len(grid[0])
#     while True:
#         changed = False
#         for y in range(H):
#             for x in range(W):
#                 if grid[y][x] == paper_roll:
#                     close_rolls = 0
#                     for dy, dx in dirs:
#                         if 0 <= y+dy < H and 0 <= x+dx < W:
#                             close_rolls += (grid[y+dy][x+dx] == paper_roll)
#                     if close_rolls < 4:
#                         grid[y][x] = removed
#                         total += 1
#                         changed = True
#         if not changed:
#             break
#     return total


if __name__ == '__main__':
    print(find_rolls1('input_day4.txt'))
    print(find_rolls2('input_day4.txt'))
    print(find_rolls2_faster('input_day4.txt'))
