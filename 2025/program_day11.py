# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 12:36:17 2025

@author: andre
"""

def find_paths1(input_file: str) -> int:
    with open(input_file, encoding= 'utf8') as f:
        devices_list = f.read().splitlines()
    devices_graph = {}
    for line in devices_list:
        device, outputs = line.strip().split(':')
        devices_graph[device] = outputs.split()
    start = 'you'
    end = 'out'
    return DFS_1(start, end, devices_graph)

def DFS_1(start: str, end: str, graph: dict[str,list[str]],
          cache: dict[str,int] | None = None) -> int:
    if cache is None:
        cache = {}
    if start == end:
        return 1
    if start in cache:
        return cache[start]
    paths = 0
    for output in graph[start]:
        paths += DFS_1(output, end, graph, cache)
    cache[start] = paths
    return paths

def find_paths2(input_file: str) -> int:
    with open(input_file, encoding= 'utf8') as f:
        devices_list = f.read().splitlines()
    devices_graph = {}
    for line in devices_list:
        device, outputs = line.strip().split(':')
        devices_graph[device] = outputs.split()
    start = 'svr'
    end = 'out'
    return DFS_2(start, end, devices_graph)

def DFS_2(start: str, end: str, graph: dict[str,list[str]], DAC: bool = False,
          FFT: bool = False, cache: dict[tuple[str,bool,bool],int] | None = None) -> int:
    if cache is None:
        cache = {}
    if start == end:
        return (DAC and FFT)
    if (start, DAC, FFT) in cache:
        return cache[(start, DAC, FFT)]
    paths = 0
    for output in graph[start]:
        paths += DFS_2(output, end, graph, DAC or (output == 'dac'),
                       FFT or (output == 'fft'), cache)
    cache[(start, DAC, FFT)] = paths
    return paths


if __name__ == '__main__':
    print(find_paths1('input_day11.txt'))
    print(find_paths2('input_day11.txt'))
