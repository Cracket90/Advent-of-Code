# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 08:28:50 2024

@author: andre
"""

def find_stones_x25(input_file: str) -> int:
    with open(input_file) as f:
        stones = list(map(int, f.read().strip().split()))
    blinks = 25
    for i in range(blinks):
        changed_stones = []
        for stone in stones:
            if stone == 0:
                changed_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                string = str(stone)
                n = len(string) // 2
                left_stone, right_stone = int(string[:n]), int(string[n:])
                changed_stones.extend([left_stone, right_stone])
            else:
                changed_stones.append(stone*2024)
        # del stones
        stones = changed_stones
        # print(i, len(stones))
    return len(stones)

def find_stones_x75(input_file: str) -> int:
    ans = 0
    with open(input_file) as f:
        stones = list(map(int, f.read().strip().split()))
    blinks = 75
    for stone in stones:
        ans += blink(stone, blinks)
    return ans

def blink(stone: int, blinks: int, cache: dict[tuple[int,int],int] = {}) -> int:
    if blinks == 0:
        return 1
    if (stone, blinks) in cache.keys():
        return cache[(stone, blinks)]
    elif stone == 0:
        ans = blink(1, blinks-1)
    elif len(str(stone)) % 2 == 0:
        string = str(stone)
        n = len(string) // 2
        left_stone, right_stone = int(string[:n]), int(string[n:])
        res_left = blink(left_stone, blinks-1)
        res_right = blink(right_stone, blinks-1)
        ans = res_left + res_right
    else:
        ans = blink(stone*2024, blinks-1)
    cache[(stone, blinks)] = ans
    # cache.clear()
    return ans

if __name__ == '__main__':
    print(find_stones_x25('input_day11.txt'))
    print(find_stones_x75('input_day11.txt'))