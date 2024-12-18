# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 09:15:46 2024

@author: andre
"""

def find_safety_factor(input_file: str) -> int:
    sec = 100
    l = 101
    h = 103
    xC = l//2
    yC = h//2
    with open(input_file) as f:
        data = f.read().strip().split('\n')
    robots_final_pos = []
    quadr = [0, 0, 0, 0]
    for line in data:
        p, v = line.split()
        Px, Py = map(int, p.split('=')[1].split(','))
        Vx, Vy = map(int, v.split('=')[1].split(','))
        Px = (Px + sec*Vx) % l
        Py = (Py + sec*Vy) % h
        robots_final_pos.append((Py, Px))
        if Py in range(0, yC) and Px in range(0, xC):
            quadr[0] += 1
        elif Py in range(0, yC) and Px in range(xC+1, l):
            quadr[1] += 1
        elif Py in range(yC+1, h) and Px in range(0, xC):
            quadr[2] += 1
        elif Py in range(yC+1, h) and Px in range(xC+1, l):
            quadr[3] += 1
    # print(robots_final_pos)
    # robots_map = [[0]*l for _ in range(h)]
    # for y, x in robots_final_pos:
    #     robots_map[y][x] += 1
    # print(robots_map)
    safety_factor = quadr[0]*quadr[1]*quadr[2]*quadr[3]
    return safety_factor

# def find_fewest_seconds(input_file: str) -> str:
#     l = 101
#     h = 103
#     max_sec = l*h
#     with open(input_file) as f:
#         data = f.read().strip().split('\n')
#     robots = []
#     for line in data:
#         robot = {}
#         p, v = line.split()
#         Px, Py = map(int, p.split('=')[1].split(','))
#         Vx, Vy = map(int, v.split('=')[1].split(','))
#         robot['p'] = (Py, Px)
#         robot['v'] = (Vy, Vx)
#         robots.append(robot)
#     # print(robots)
#     robots_maps = []
#     for s in range(0, max_sec+1):
#         robots_map = [['.']*l for _ in range(h)]
#         for robot in robots:
#             Py, Px = robot['p']
#             Vy, Vx = robot['v']
#             Px = (Px + s*Vx) % l
#             Py = (Py + s*Vy) % h
#             robots_map[Py][Px] = 'X'
#         robots_map_str = '\n'.join(''.join(line) for line in robots_map)
#         robots_maps.append(f'Second: {s}\nMap:\n{robots_map_str}\n\n')
#     with open('output_day14.txt', 'w') as f:
#         f.writelines(robots_maps)
#     return "The output file 'output_day14.txt' has been written.\nFind the Christmas tree!"

def find_fewest_seconds(input_file: str) -> int:
    l = 101
    h = 103
    with open(input_file) as f:
        data = f.read().strip().split('\n')
    robots = []
    for line in data:
        robot = {}
        p, v = line.split()
        Px, Py = map(int, p.split('=')[1].split(','))
        Vx, Vy = map(int, v.split('=')[1].split(','))
        robot['p'] = (Py, Px)
        robot['v'] = (Vy, Vx)
        robots.append(robot)
    num_robots = len(robots)
    x_variances = []
    y_variances = []
    for s in range(l):
        robots_x = []
        for robot in robots:
            Py, Px = robot['p']
            Vy, Vx = robot['v']
            Px = (Px + s*Vx) % l
            robots_x.append(Px)
        average = sum(robots_x)/num_robots
        variance = (sum(map(lambda x: (x-average)**2, robots_x))/num_robots)**(1/2)
        x_variances.append((s, variance))
    for s in range(h):
        robots_y = []
        for robot in robots:
            Py, Px = robot['p']
            Vy, Vx = robot['v']
            Py = (Py + s*Vy) % h
            robots_y.append(Py)
        average = sum(robots_y)/num_robots
        variance = (sum(map(lambda x: (x-average)**2, robots_y))/num_robots)**(1/2)
        y_variances.append((s, variance))
    bx = min(x_variances, key=lambda x: x[1])[0]
    by = min(y_variances, key=lambda x: x[1])[0]
    k = ((by-bx)*pow(l,-1,h)) % h
    fs = bx + k*l
    # robots_map = [['.']*l for _ in range(h)]
    # for robot in robots:
    #     Py, Px = robot['p']
    #     Vy, Vx = robot['v']
    #     Px = (Px + fs*Vx) % l
    #     Py = (Py + fs*Vy) % h
    #     robots_map[Py][Px] = 'X'
    # print('\n'.join(''.join(line) for line in robots_map))
    return fs

if __name__ == '__main__':
    print(find_safety_factor('input_day14.txt'))
    print(find_fewest_seconds('input_day14.txt'))