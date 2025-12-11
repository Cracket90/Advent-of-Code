# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 12:13:30 2025

@author: andre
"""

def find_largest_area1(input_file: str) -> int:
    with open(input_file, encoding= 'utf8') as f:
        tiles = f.read().splitlines()
    red_tiles = [tuple(map(int, tile.split(','))) for tile in tiles]
    max_area = 0
    for i, first_corner in enumerate(red_tiles):
        xC1, yC1 = first_corner
        for j, second_corner in enumerate(red_tiles):
            if j > i:
                xC2, yC2 = second_corner
                width = abs(xC2 - xC1) + 1
                height = abs(yC2 - yC1) + 1
                area = width * height
                max_area = max(area, max_area)
    return max_area

def find_largest_area2(input_file: str) -> int:
    with open(input_file, encoding= 'utf8') as f:
        tiles = f.read().splitlines()
    red_tiles = [tuple(map(int, tile.split(','))) for tile in tiles]
    n = len(red_tiles)
    segments = []  # perimeter
    for k in range(n):
        x1, y1 = red_tiles[k]
        x2, y2 = red_tiles[(k+1) % n]
        if x1 == x2:
            segments.append((x1, min(y1, y2), x2, max(y1, y2), 'V'))
        elif y1 == y2:
            segments.append((min(x1, x2), y1, max(x1, x2), y2, 'H'))
    max_area = 0
    for i, first_corner in enumerate(red_tiles):
        xC1, yC1 = first_corner
        for j, second_corner in enumerate(red_tiles):
            if j > i:
                xC2, yC2 = second_corner
                area = (abs(yC2 - yC1) + 1) * (abs(xC2 - xC1) + 1)
                if area <= max_area:
                    continue
                xR_min, xR_max = min(xC1, xC2), max(xC1, xC2)
                yR_min, yR_max = min(yC1, yC2), max(yC1, yC2)
                intersects = False
                for xS1, yS1, xS2, yS2, orientation in segments:
                    if orientation == 'V':
                        if xR_min < xS1 < xR_max:
                            overlap_min = max(yS1, yR_min+1)
                            overlap_max = min(yS2, yR_max-1)
                            if overlap_min <= overlap_max:
                                intersects = True
                                break
                    elif orientation == 'H':
                        if yR_min < yS1 < yR_max:
                            overlap_min = max(xS1, xR_min+1)
                            overlap_max = min(xS2, xR_max-1)
                            if overlap_min <= overlap_max:
                                intersects = True
                                break
                if not intersects:
                    max_area = area
    return max_area

# from matplotlib import path
# from matplotlib import pyplot as plt

# def find_largest_area2(input_file: str) -> int:
#     with open(input_file, encoding= 'utf8') as f:
#         tiles = f.read().splitlines()
#     red_tiles = [tuple(map(int, tile.split(','))) for tile in tiles]
#     polygon = path.Path(red_tiles)
#     x = [p[0] for p in red_tiles]
#     y = [p[1] for p in red_tiles]
#     x.append(x[0])
#     y.append(y[0])
#     plt.figure(figsize=(8, 6))
#     plt.plot(x, y, linestyle='-', color='b', label='Perimetro')
#     plt.fill(x, y, alpha=0.2, color='blue')
#     plt.grid(True)
#     plt.title("Visualizzazione Poligono")
#     plt.xlabel("Coordinate X")
#     plt.ylabel("Coordinate Y")
#     plt.legend()
#     plt.axis('equal')
#     plt.show()
#     max_area = 0
#     for i, first_corner in enumerate(red_tiles):
#         xC1, yC1 = first_corner
#         for j, second_corner in enumerate(red_tiles):
#             if j > i:
#                 xC2, yC2 = second_corner
#                 area = (abs(yC2 - yC1) + 1) * (abs(xC2 - xC1) + 1)
#                 if area <= max_area:
#                     continue
#                 xR_min, xR_max = min(xC1, xC2), max(xC1, xC2)
#                 yR_min, yR_max = min(yC1, yC2), max(yC1, yC2)
#                 is_inside = True
#                 for x in range(xR_min, xR_max+1):
#                     for y in range(yR_min, yR_max+1):
#                         if not polygon.contains_point((x, y), radius=0.001):
#                             is_inside = False
#                             break
#                     if not is_inside:
#                         break
#                 if is_inside:
#                     max_area = area
#     return max_area


if __name__ == '__main__':
    print(find_largest_area1('input_day9.txt'))
    print(find_largest_area2('input_day9.txt'))
