# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 01:52:29 2024

@author: andre
"""

def nice_strings(input_file: str) -> int:
    with open(input_file) as f:
        text = f.read().strip().splitlines()
    ans = 0
    vowels = 'aeiou'
    forbidden = ['ab', 'cd', 'pq', 'xy']
    for string in text:
        l = len(string)
        num_vowels = 0
        twice = False
        allowed = True
        for i, char in enumerate(string):
            if i+1 < l:
                if char + string[i+1] in forbidden:
                    allowed = False
                    break
                elif char == string[i+1]:
                    twice = True
            if char in vowels:
                num_vowels += 1
        if allowed and twice and num_vowels >= 3:
            ans += 1
    return ans

def nice_strings2(input_file: str) -> int:
    with open(input_file) as f:
        text = f.read().strip().splitlines()
    ans = 0
    for string in text:
        l = len(string)
        pairs: dict[str,int] = {}
        repeated = False
        for i, char in enumerate(string):
            if i+1 < l:
                if i > 0 and string[i-1] + char == char + string[i+1]:
                    if i > 1 and string[i-2] + string[i-1] == char + string[i+1]:
                        pairs[char + string[i+1]] = pairs.get(char + string[i+1], 0) + 1
                else:
                    pairs[char + string[i+1]] = pairs.get(char + string[i+1], 0) + 1
            if i+2 < l:
                if char == string[i+2]:
                    repeated = True
        if repeated and max(pairs.values()) >= 2:
            ans += 1
    return ans

if __name__ == '__main__':
    print(nice_strings('input_day5.txt'))
    print(nice_strings2('input_day5.txt'))