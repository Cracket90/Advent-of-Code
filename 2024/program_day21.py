# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 08:05:58 2024

@author: andre
"""

def complexities_codes(input_file: str) -> int:
    with open(input_file) as f:
        codes = f.read().strip().split('\n')
    num_keypad = ('789','456','123',' 0A')
    hn, ln = len(num_keypad), len(num_keypad[0])
    num_pos_keypad = {}
    for y in range(hn):
        for x in range(ln):
            num_pos_keypad[num_keypad[y][x]] = (y,x)
    num_paths = {}
    for start in 'A0123456789':
        for end in 'A0123456789':
            num_paths[(start,end)] = find_shortest_paths(start, end, num_keypad, num_pos_keypad)
    dir_keypad = (' ^A','<v>')
    hd, ld = len(dir_keypad), len(dir_keypad[0])
    dir_pos_keypad = {}
    for y in range(hd):
        for x in range(ld):
            dir_pos_keypad[dir_keypad[y][x]] = (y,x)
    dir_paths = {}
    for start in 'A<^>v':
        for end in 'A<^>v':
            dir_paths[(start,end)] = find_shortest_paths(start, end, dir_keypad, dir_pos_keypad)
    ans = 0
    for code in codes:
        first_dir_robot = []
        for seq in find_sequences(code, num_paths):
            first_dir_robot.extend(find_sequences(seq, dir_paths))
        first_dir_robot.sort(key= len)
        second_dir_robot = []
        for seq in filter(lambda x: len(x) == len(first_dir_robot[0]), first_dir_robot):
            second_dir_robot.extend(find_sequences(seq, dir_paths))
        second_dir_robot.sort(key= len)
        length = len(second_dir_robot[0])
        num_part = int(code[:-1])
        ans += length*num_part
    return ans

def complexities_codes_X25(input_file: str) -> int:
    with open(input_file) as f:
        codes = f.read().strip().split('\n')
    num_keypad = ('789','456','123',' 0A')
    hn, ln = len(num_keypad), len(num_keypad[0])
    num_pos_keypad = {}
    for y in range(hn):
        for x in range(ln):
            num_pos_keypad[num_keypad[y][x]] = (y,x)
    num_paths = {}
    for start in 'A0123456789':
        for end in 'A0123456789':
            num_paths[(start,end)] = find_shortest_paths(start, end, num_keypad, num_pos_keypad)
    dir_keypad = (' ^A','<v>')
    hd, ld = len(dir_keypad), len(dir_keypad[0])
    dir_pos_keypad = {}
    for y in range(hd):
        for x in range(ld):
            dir_pos_keypad[dir_keypad[y][x]] = (y,x)
    dir_paths = {}
    for start in 'A<^>v':
        for end in 'A<^>v':
            dir_paths[(start,end)] = find_shortest_paths(start, end, dir_keypad, dir_pos_keypad)
    ans = 0
    num_dir_robots = 25
    for code in codes:
        start = 'A'
        length = 0
        el1 = start
        for el2 in code:
            lengths = []
            for dir_seq in num_paths[(el1,el2)]:
                lengths.append(find_min_cost(start, dir_seq, dir_paths, num_dir_robots))
            length += min(lengths)
            el1 = el2
        num_part = int(code[:-1])
        ans += length*num_part
    return ans

def find_shortest_paths(el1: str, el2: str, keypad: tuple[str,...],
                        pos_keypad: dict[str,tuple], min_dist: int|None = None,
                        path: str = '', paths: list[str]|None = None) -> list[str]:
    if paths is None:
        paths = []
    y1, x1 = pos_keypad[el1]
    y2, x2 = pos_keypad[el2]
    if min_dist is None:
        min_dist = abs(y1-y2) + abs(x1-x2)
    if min_dist == 0:
        if el1 == el2:
            paths.append(path + 'A')
            return paths
        else: return []
    dirs = {(0,-1): '^', (1,0): '>', (0,1): 'v', (-1,0): '<'}
    h, l = len(keypad), len(keypad[0])
    for dx, dy in dirs:
        xn, yn = x1+dx, y1+dy
        if xn in range(l) and yn in range(h) and keypad[yn][xn] != ' ':
            eln = keypad[yn][xn]
            direction = dirs[(dx,dy)]
            find_shortest_paths(eln, el2, keypad, pos_keypad, min_dist-1, path+direction, paths)
    return paths

def find_sequences(code: str, paths: dict[tuple,list[str]]) -> list[str]:
    start = 'A'
    sequences = ['']
    for el in code:
        next_sequences = []
        for seq in sequences:
            for path in paths[(start,el)]:
                next_sequences.append(seq + path)
        sequences = next_sequences
        start = el
    return sequences

def find_min_cost(start: str, dir_seq: str, dir_paths: dict[tuple,list[str]],
                  num_dir_robots: int, cache: dict[tuple,int] = {}) -> int:
    if num_dir_robots == 0:
        return len(dir_seq)
    if (dir_seq, num_dir_robots) in cache:
        return cache[(dir_seq, num_dir_robots)]
    cost = 0
    el1 = start
    for el2 in dir_seq:
        seq_costs = []
        for seq in dir_paths[(el1,el2)]:
            seq_costs.append(find_min_cost(start, seq, dir_paths, num_dir_robots-1, cache))
        cost += min(seq_costs)
        el1 = el2
    cache[(dir_seq, num_dir_robots)] = cost
    return cost

if __name__ == '__main__':
    print(complexities_codes('input_day21.txt'))
    print(complexities_codes_X25('input_day21.txt'))