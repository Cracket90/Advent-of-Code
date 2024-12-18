# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 08:18:35 2024

@author: andre
"""

def fence_price(input_file: str) -> int:
    price = 0
    regions = {}
    seen: set[tuple[int,int]] = set()
    with open(input_file) as f:
        garden = f.read().strip().split('\n')
    h, l = len(garden), len(garden[0])
    for y in range(h):
        for x in range(l):
            if (y, x) not in seen:
                plant = garden[y][x]
                region = find_region(plant, y, x, garden, seen)
                regions[(y, x)] = region
    for area, perimeter in regions.values():
        price += area*perimeter
    # print(regions)
    return price

def fence_sides_price(input_file: str) -> int:
    price = 0
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    regions = {}
    seen: set[tuple[int,int]] = set()
    with open(input_file) as f:
        garden = f.read().strip().split('\n')
    h, l = len(garden), len(garden[0])
    for y in range(h):
        for x in range(l):
            if (y, x) not in seen:
                plant = garden[y][x]
                area = find_region_area(plant, y, x, garden)
                seen = seen.union(area)
                perimeter = set()
                for pos in area:
                    y_pos, x_pos = pos
                    for direction in dirs:
                        dx, dy = direction
                        near_y, near_x = y_pos + dy, x_pos + dx
                        if (near_y, near_x) not in area:
                            perimeter.add((pos, direction))
                regions[(y, x)] = (area, perimeter)
    for area, perimeter in regions.values():
        sides = set()
        for pos, direction in perimeter:
            y, x = pos
            if not any(((y+dy, x+dx), direction) in perimeter for dx, dy in [(1, 0), (0, 1)]):
                sides.add((pos, direction))
        price += len(area)*len(sides)
    # print(regions)
    return price

def find_region(plant: str, y: int, x: int, garden: list[str], seen: set[tuple[int,int]]) -> tuple[int,int]:
    h, l = len(garden), len(garden[0])
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    if y not in range(h) or x not in range(l) or garden[y][x] != plant:
        return (0, 1)
    if (y, x) in seen:
        return (0, 0)
    seen.add((y, x))
    area = 1
    perimeter = 0
    for dx, dy in dirs:
        near_y, near_x = y + dy, x + dx
        near_area, near_perimeter = find_region(plant, near_y, near_x, garden, seen)
        area += near_area
        perimeter += near_perimeter
    return (area, perimeter)

def find_region_area(plant: str, y: int, x: int, garden: list[str],
                      area: set[tuple[int,int]] | None = None) -> set[tuple[int,int]]:
    h, l = len(garden), len(garden[0])
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    if area is None:
        area = set()
    if y not in range(h) or x not in range(l) or garden[y][x] != plant or (y, x) in area:
        return   # type: ignore
    area.add((y, x))
    for dx, dy in dirs:
        near_y, near_x = y + dy, x + dx
        find_region_area(plant, near_y, near_x, garden, area)
    return area

if __name__ == '__main__':
    print(fence_price('input_day12.txt'))
    print(fence_sides_price('input_day12.txt'))