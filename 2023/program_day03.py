# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 18:15:31 2024

@author: andre
"""

import re

def find_part_numbers(input_file: str) -> int:
    ans = 0
    with open(input_file, mode="r", encoding="utf-8") as f:
        data = f.read().strip().split('\n')
    for row, line in enumerate(data):
        index = tmp_index = 0
        while True:
            line = line[tmp_index:]
            regex = '[0-9]+'
            matching = re.search(regex, line)
            if matching != None:
                start = matching.start()    # type: ignore
                end = matching.end()    # type: ignore
                if is_part_number(data, row, start+index, end+index):
                    ans += int(matching.group())    # type: ignore
                tmp_index = end
                index += end
            else: break
    return ans

def find_gear_ratios(input_file: str) -> int:
    with open(input_file, mode="r", encoding="utf-8") as f:
        data = f.read().strip().split('\n')
    possible_gears: dict[tuple[int,int],list[int]] = {}
    for row, line in enumerate(data):
        index = tmp_index = 0
        while True:
            line = line[tmp_index:]
            regex = '[0-9]+'
            matching = re.search(regex, line)
            if matching != None:
                start = matching.start()    # type: ignore
                end = matching.end()    # type: ignore
                value = int(matching.group())   # type: ignore
                possible_gears = update_gears(data, row, start+index, end+index, value, possible_gears)
                tmp_index = end
                index += end
            else: break
    gears = {pos: values for pos, values in possible_gears.items() if len(values) == 2}
    # print(gears)
    ans = sum(num1*num2 for num1, num2 in gears.values())
    return ans

def is_part_number(data: list[str], row: int, start: int, end: int) -> bool:
    height, width = len(data), len(data[0])
    first_row = row-1 if row-1 >= 0 else row
    final_row = row+1 if row+1 < height else row
    first_index = start-1 if start-1 >= 0 else start
    final_index = end if end < width else end-1
    for i in range(first_row, final_row+1):
        for j in range(first_index, final_index+1):
            if not data[i][j].isdecimal() and data[i][j] != '.':
                return True
    return False

def update_gears(data: list[str], row: int, start: int, end: int, value: int, possible_gears: dict[tuple[int,int],list[int]]) -> dict[tuple[int,int],list[int]]:
    height, width = len(data), len(data[0])
    first_row = row-1 if row-1 >= 0 else row
    final_row = row+1 if row+1 < height else row
    first_index = start-1 if start-1 >= 0 else start
    final_index = end if end < width else end-1
    for i in range(first_row, final_row+1):
        for j in range(first_index, final_index+1):
            if data[i][j] == '*':
                possible_gears[(i,j)] = possible_gears.get((i,j), []) + [value]
    return possible_gears

if __name__ == '__main__':
    print(find_part_numbers('input_day3.txt'))
    print(find_gear_ratios('input_day3.txt'))
