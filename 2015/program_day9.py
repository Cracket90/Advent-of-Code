# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 00:58:21 2025

@author: andre
"""

def shortest_route(input_file: str) -> int:
    with open(input_file) as f:
        data = f.read().strip().splitlines()
    distances: dict[tuple,int] = {}
    locations: set[str] = set()
    for line in data:
        locs, dist = line.split(' = ')
        loc1, loc2 = locs.split(' to ')
        distances[(loc1, loc2)] = int(dist)
        distances[(loc2, loc1)] = int(dist)
        locations.update({loc1, loc2})
    shortest_routes = []
    for location in locations:
        next_locations = locations - {location}
        shortest_routes.append(find_shortest_route(location, next_locations, distances))
    return min(shortest_routes)

def longest_route(input_file: str) -> int:
    with open(input_file) as f:
        data = f.read().strip().splitlines()
    distances: dict[tuple,int] = {}
    locations: set[str] = set()
    for line in data:
        locs, dist = line.split(' = ')
        loc1, loc2 = locs.split(' to ')
        distances[(loc1, loc2)] = int(dist)
        distances[(loc2, loc1)] = int(dist)
        locations.update({loc1, loc2})
    longest_routes = []
    for location in locations:
        next_locations = locations - {location}
        longest_routes.append(find_longest_route(location, next_locations, distances))
    return max(longest_routes)

def find_shortest_route(start: str, locations: set[str], distances: dict[tuple,int]) -> int:
    if not locations:
        return 0
    if len(locations) == 1:
        return distances[(start, *locations)]
    shortest_routes = []
    for location in locations:
        next_locations = locations - {location}
        route = distances[(start, location)] + find_shortest_route(location, next_locations, distances)
        shortest_routes.append(route)
    return min(shortest_routes)

def find_longest_route(start: str, locations: set[str], distances: dict[tuple,int]) -> int:
    if not locations:
        return 0
    if len(locations) == 1:
        return distances[(start, *locations)]
    longest_routes = []
    for location in locations:
        next_locations = locations - {location}
        route = distances[(start, location)] + find_longest_route(location, next_locations, distances)
        longest_routes.append(route)
    return max(longest_routes)

if __name__ == '__main__':
    print(shortest_route('input_day9.txt'))
    print(longest_route('input_day9.txt'))