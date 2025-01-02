# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 02:13:06 2025

@author: andre
"""

def find_lengths(input_file: str) -> tuple[int,int]:
    with open(input_file) as f:
        sequence = f.read().strip()
    t1 = 40
    t2 = 50
    l1 = num_digits(sequence, t1)
    l2 = num_digits(sequence, t2)
    return l1, l2

def num_digits(sequence: str, times: int) -> int:
    if not times:
        return len(sequence)
    l = len(sequence)
    new_sequence = []
    i = 0
    while i < l:
        value = sequence[i]
        j = i+1
        while j < l and sequence[j] == value:
            j += 1
        new_sequence.append(str(j-i) + value)
        i += (j-i)
    length = num_digits(''.join(new_sequence), times-1)
    return length

if __name__ == '__main__':
    print(find_lengths('input_day10.txt'))