# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 13:45:22 2025

@author: andre
"""

Coordinate = tuple[int,int,int]

def find_three_largest_circuits(input_file: str, connections: int) -> int:
    with open(input_file, encoding= 'utf8') as f:
        boxes = f.read().splitlines()
    positions = set(tuple(map(int, box.split(','))) for box in boxes)
    distances = find_distances(positions)  # type: ignore
    ordered_pairs = sorted(distances.keys(), key= lambda x: distances[x])
    connections_graph = {box: set() for box in positions}  # type: ignore
    for pair in ordered_pairs[:connections]:
        p1, p2 = pair
        connections_graph[p1] |= {p2}
        connections_graph[p2] |= {p1}
    circuits = find_len_circuits(connections_graph)  # type: ignore
    circuits.sort(reverse= True)
    return circuits[0] * circuits[1] * circuits[2]

def find_distances(positions: set[Coordinate],
                   seen: set[Coordinate] | None = None) -> dict[tuple[Coordinate,Coordinate],int]:
    if seen is None:
        seen = set()
    distances = {}
    for p1 in positions:
        seen.add(p1)
        for p2 in positions - seen:
            distances[(p1, p2)] = squared_euclidean_distance(p1, p2)
    return distances

def squared_euclidean_distance(first_point: Coordinate, second_point: Coordinate) -> int:
    x1, y1, z1 = first_point
    x2, y2, z2 = second_point
    return (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2

def find_len_circuits(graph: dict[Coordinate,set[Coordinate]],
                      seen: set[Coordinate] | None = None) -> list[int]:
    if seen is None:
        seen = set()
    circuits = []
    for box in graph:
        if box not in seen:
            seen.add(box)
            len_circuit = 1
            circuit_boxes = graph[box].copy()
            while circuit_boxes:
                next_box = circuit_boxes.pop()
                if next_box not in seen:
                    seen.add(next_box)
                    len_circuit += 1
                    circuit_boxes |= graph[next_box]
            circuits.append(len_circuit)
    return circuits

def find_last_two_boxes(input_file: str) -> int | None:
    with open(input_file, encoding= 'utf8') as f:
        boxes = f.read().splitlines()
    number_of_boxes = len(boxes)
    positions = set(tuple(map(int, box.split(','))) for box in boxes)
    distances = find_distances(positions)  # type: ignore
    ordered_pairs = sorted(distances.keys(), key= lambda x: distances[x])
    connections_graph = {box: set() for box in positions}  # type: ignore
    connections = 0
    for pair in ordered_pairs:
        p1, p2 = pair
        if not are_connected(p1, p2, connections_graph):  # type: ignore
            connections_graph[p1] |= {p2}
            connections_graph[p2] |= {p1}
            connections += 1
            if connections == number_of_boxes-1:
                return p1[0] * p2[0]
    return None

def are_connected(first_point: Coordinate, second_point: Coordinate,
                  graph: dict[Coordinate,set[Coordinate]],
                  seen: set[Coordinate] | None = None) -> bool:
    if seen is None:
        seen = set()
    seen.add(first_point)
    next_points = graph[first_point].copy()
    while next_points:
        next_point = next_points.pop()
        if next_point == second_point:
            return True
        if next_point not in seen:
            seen.add(next_point)
            next_points |= graph[next_point]
    return False


if __name__ == '__main__':
    print(find_three_largest_circuits('input_day8.txt', 1000))
    print(find_last_two_boxes('input_day8.txt'))
