# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:05:27 2024

@author: andre
"""

def find_xmas(input_file: str) -> int:
    words = []
    with open(input_file) as f:
        data = f.read().strip().split('\n')
    height = len(data)
    length = len(data[0])
    for i in range(height):
        for j in range(length):
            if data[i][j] == 'X' or data[i][j] == 'S':
                if j <= length-4: words.append(data[i][j:j+4])
                if i <= height-4: words.append(data[i][j]+data[i+1][j]+data[i+2][j]+data[i+3][j])
                if i <= height-4 and j <= length-4:
                    words.append(data[i][j]+data[i+1][j+1]+data[i+2][j+2]+data[i+3][j+3])
                if i >= 3 and j <= length-4:
                    words.append(data[i][j]+data[i-1][j+1]+data[i-2][j+2]+data[i-3][j+3])
    result = words.count('XMAS') + words.count('SAMX')
    return result

def find_new_xmas(input_file: str) -> int:
    result = 0
    words = ['MAS', 'SAM']
    with open(input_file) as f:
        data = f.read().strip().split('\n')
    height = len(data)
    length = len(data[0])
    for i in range(height):
        for j in range(length):
            if data[i][j] == 'A' and 1 <= j <= length-2 and 1 <= i <= height-2:
                first_X = data[i-1][j-1]+data[i][j]+data[i+1][j+1]
                second_X = data[i+1][j-1]+data[i][j]+data[i-1][j+1]
                if first_X in words and second_X in words:
                    result += 1
    return result

if __name__ == '__main__':
    print(find_xmas('input_day4.txt'))
    print(find_new_xmas('input_day4.txt'))