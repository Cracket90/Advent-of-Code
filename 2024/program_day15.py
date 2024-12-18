# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 07:42:55 2024

@author: andre
"""

def find_GPS_coordinates(input_file: str) -> int:
    ans = 0
    with open(input_file) as f:
        data1, data2 = f.read().strip().split('\n\n')
    warehouse = [list(line) for line in data1.split('\n')]
    moves = ''.join(data2.split('\n'))
    h, l = len(warehouse), len(warehouse[0])
    distY = 100
    dirs = {'^': (0,-1), '>': (1,0), 'v': (0,1), '<': (-1,0)}
    robot, box, space, wall = '@', 'O', '.', '#'
    for y in range(h):
        for x in range(l):
            if warehouse[y][x] == robot:
                ry, rx = y, x
                break
    for move in moves:
        dx, dy = dirs[move]
        nx, ny = rx+dx, ry+dy
        if warehouse[ny][nx] == space:
            warehouse[ny][nx], warehouse[ry][rx] = warehouse[ry][rx], warehouse[ny][nx]
            rx, ry = nx, ny
        elif warehouse[ny][nx] == box:
            bx, by = nx, ny
            while warehouse[ny][nx] != wall:
                nx, ny = nx+dx, ny+dy
                if warehouse[ny][nx] == space:
                    warehouse[ny][nx], warehouse[by][bx], warehouse[ry][rx] = warehouse[by][bx], warehouse[ry][rx], warehouse[ny][nx]
                    rx, ry = bx, by
                    break
        # print('\n'.join(''.join(line) for line in warehouse)+'\n')
    for y in range(h):
        for x in range(l):
            if warehouse[y][x] == box:
                GPS_coordinate = y*distY + x
                ans += GPS_coordinate
    return ans

def find_GPS_coordinates_X2(input_file: str) -> int:
    ans = 0
    with open(input_file) as f:
        data1, data2 = f.read().strip().split('\n\n')
    warehouse = [list(line) for line in data1.split('\n')]
    moves = ''.join(data2.split('\n'))
    h, l = len(warehouse), len(warehouse[0])
    distY = 100
    dirs = {'^': (0,-1), '>': (1,0), 'v': (0,1), '<': (-1,0)}
    robot, box, space, wall = '@', 'O', '.', '#'
    warehouseX2 = []
    for y in range(h):
        line = []
        for x in range(l):
            if warehouse[y][x] == robot:
                line.extend(['@', '.'])
            elif warehouse[y][x] == box:
                line.extend(['[', ']'])
            elif warehouse[y][x] == space:
                line.extend(['.', '.'])
            elif warehouse[y][x] == wall:
                line.extend(['#', '#'])
        warehouseX2.append(line)
    h2, l2 = h, l*2
    for y in range(h2):
        for x in range(l2):
            if warehouseX2[y][x] == robot:
                ry, rx = y, x
                break
    for move in moves:
        dx, dy = dirs[move]
        nx, ny = rx+dx, ry+dy
        if warehouseX2[ny][nx] == space:
            warehouseX2[ny][nx], warehouseX2[ry][rx] = warehouseX2[ry][rx], warehouseX2[ny][nx]
            rx, ry = nx, ny
        elif warehouseX2[ny][nx] in '[]' and move in '><':
            bx, by = nx, ny
            num_box_aligned = 1
            while warehouseX2[ny][nx] != wall:
                nx, ny = nx+2*dx, ny+2*dy
                if warehouseX2[ny][nx] in '[]':
                    num_box_aligned += 1
                    continue
                elif warehouseX2[ny][nx] == space:
                    for n in range(0, num_box_aligned*2, 2):
                        warehouseX2[by+n*dy][bx+n*dx], warehouseX2[by+(n+1)*dy][bx+(n+1)*dx] = warehouseX2[by+(n+1)*dy][bx+(n+1)*dx], warehouseX2[by+n*dy][bx+n*dx]
                    warehouseX2[ny][nx], warehouseX2[by][bx], warehouseX2[ry][rx] = warehouseX2[by][bx], warehouseX2[ry][rx], warehouseX2[ny][nx]
                    rx, ry = bx, by
                    break
        elif warehouseX2[ny][nx] in '[]' and move in '^v':
            bx, by = nx, ny
            levels = [{(ry, rx)}]
            boxes = set()
            if warehouseX2[ny][nx] == '[':
                boxes.update({(ny,nx), (ny,nx+1)})
            else:
                boxes.update({(ny,nx-1), (ny,nx)})
            levels.append(boxes)
            while wall not in (warehouseX2[y][x] for y, x in boxes):
                next_level = set()
                for ny, nx in boxes:
                    mx, my = nx+dx, ny+dy
                    next_level.add((my,mx))
                    if warehouseX2[my][mx] in '[]' and warehouseX2[my][mx] != warehouseX2[ny][nx]:
                        next_level.update({(my,mx-1), (my,mx+1)})
                levels.append(next_level)
                if all(warehouseX2[y][x] == space for y, x in next_level):
                    to_move = {pos for level in levels for pos in level}
                    for level in levels[::-1]:
                        for y, x in level:
                            if (y-dy,x-dx) in to_move:
                                warehouseX2[y][x] = warehouseX2[y-dy][x-dx]
                            else:
                                warehouseX2[y][x] = space
                    rx, ry = bx, by
                    break
                boxes = {(y,x) for y, x in next_level if warehouseX2[y][x] != space}
        # print('\n'.join(''.join(line) for line in warehouseX2)+'\n')
    for y in range(h2):
        for x in range(l2):
            if warehouseX2[y][x] == '[':
                GPS_coordinate = y*distY + x
                ans += GPS_coordinate
    return ans

if __name__ == '__main__':
    print(find_GPS_coordinates('input_day15.txt'))
    print(find_GPS_coordinates_X2('input_day15.txt'))