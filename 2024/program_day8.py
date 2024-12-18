# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 08:51:13 2024

@author: andre
"""

def find_antinodes(input_file: str) -> int:
    antennae: dict[str,list] = {}
    antinodes = set()
    with open(input_file) as f:
        data = f.read().strip().split('\n')
    h, l = len(data), len(data[0])
    for j, line in enumerate(data):
        for i, char in enumerate(line):
            if char != '.':
                antennae[char] = antennae.get(char, []) + [(j, i)]
    for positions in antennae.values():
        for n, position in enumerate(positions):
            y_ant1, x_ant1 = position
            for other in positions[n+1:]:
                y_ant2, x_ant2 = other
                dy = abs(y_ant1 - y_ant2)
                dx = abs(x_ant1 - x_ant2)
                if y_ant1 < y_ant2:
                    y_nod1 = y_ant1 - dy
                    y_nod2 = y_ant2 + dy
                else:
                    y_nod1 = y_ant1 + dy
                    y_nod2 = y_ant2 - dy
                if x_ant1 < x_ant2:
                    x_nod1 = x_ant1 - dx
                    x_nod2 = x_ant2 + dx
                else:
                    x_nod1 = x_ant1 + dx
                    x_nod2 = x_ant2 - dx
                if y_nod1 in range(h) and x_nod1 in range(l):
                    antinodes.add((y_nod1, x_nod1))
                if y_nod2 in range(h) and x_nod2 in range(l):
                    antinodes.add((y_nod2, x_nod2))
    return len(antinodes)

def find_more_antinodes(input_file: str) -> int:
    antennae: dict[str,list] = {}
    antinodes = set()
    with open(input_file) as f:
        data = f.read().strip().split('\n')
    h, l = len(data), len(data[0])
    for j, line in enumerate(data):
        for i, char in enumerate(line):
            if char != '.':
                antennae[char] = antennae.get(char, []) + [(j, i)]
    for positions in antennae.values():
        for n, position in enumerate(positions):
            for other in positions[n+1:]:
                y_ant1, x_ant1 = position
                y_ant2, x_ant2 = other
                dy = abs(y_ant1 - y_ant2)
                dx = abs(x_ant1 - x_ant2)
                antinodes.add((y_ant1, x_ant1))
                antinodes.add((y_ant2, x_ant2))
                for _ in range(max(h, l)):
                    if y_ant1 < y_ant2:
                        y_nod1 = y_ant1 - dy
                        y_nod2 = y_ant2 + dy
                    else:
                        y_nod1 = y_ant1 + dy
                        y_nod2 = y_ant2 - dy
                    if x_ant1 < x_ant2:
                        x_nod1 = x_ant1 - dx
                        x_nod2 = x_ant2 + dx
                    else:
                        x_nod1 = x_ant1 + dx
                        x_nod2 = x_ant2 - dx
                    if y_nod1 in range(h) and x_nod1 in range(l):
                        antinodes.add((y_nod1, x_nod1))
                    if y_nod2 in range(h) and x_nod2 in range(l):
                        antinodes.add((y_nod2, x_nod2))
                    y_ant1, x_ant1 = y_nod1, x_nod1
                    y_ant2, x_ant2 = y_nod2, x_nod2
    # output = []
    # for j in range(h):
    #     row = []
    #     for i in range(l):
    #         row.append('.')
    #     output.append(row)
    # for position in antinodes:
    #     j, i = position
    #     output[j][i] = '#'
    # output_text = ''
    # for row in output:
    #     output_text += ''.join(row) + '\n'
    # with open('output.txt', 'w') as f:
    #     f.write(output_text)
    return len(antinodes)

if __name__ == '__main__':
    print(find_antinodes('input_day8.txt'))
    print(find_more_antinodes('input_day8.txt'))