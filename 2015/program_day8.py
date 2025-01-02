# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 17:22:36 2024

@author: andre
"""

def find_diff(input_file: str) -> int:
    with open(input_file) as f:
        data = f.read().strip().splitlines()
    code_chars = 0
    string_chars = 0
    for line in data:
        l = len(line)
        code_chars += l
        i = 1
        while i < l-1:
            string_chars += 1
            if line[i] == "\\":
                if line[i+1] in ["\\", "\""]:
                    i += 1
                elif line[i+1] == "x":
                    i += 3
            i += 1
    return code_chars - string_chars

def find_new_diff(input_file: str) -> int:
    with open(input_file) as f:
        data = f.read().strip().splitlines()
    code_chars = 0
    string_chars = 0
    for line in data:
        l = len(line)
        string_chars += l
        code_chars += l + 2 + line.count("\\") + line.count("\"")
        # code_chars += 2
        # i = 0
        # while i < l:
        #     code_chars += 1
        #     if line[i] in ["\\", "\""]:
        #         code_chars += 1
        #     i += 1
    return code_chars - string_chars

if __name__ == '__main__':
    print(find_diff('input_day8.txt'))
    print(find_new_diff('input_day8.txt'))