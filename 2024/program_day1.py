# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 16:29:39 2024

@author: andre
"""

def find_distance(input_file: str) -> int:
    summ = 0
    with open(input_file) as f:
        data = f.readlines()
    list1 = []
    list2 = []
    for line in data:
        el = line.split()
        list1.append(int(el[0]))
        list2.append(int(el[1]))
    list1.sort()
    list2.sort()
    for el1,el2 in zip(list1,list2):
        difference = abs(el1-el2)
        summ += difference
    return summ

def similarity_score(input_file: str) -> int:
    score = 0
    with open(input_file) as f:
        data = f.readlines()
    list1 = []
    list2 = []
    for line in data:
        el = line.split()
        list1.append(int(el[0]))
        list2.append(int(el[1]))
    for num in list1:
        times = list2.count(num)
        score += num*times
    return score

if __name__ == '__main__':
    print(find_distance('input_day1.txt'))
    print(similarity_score('input_day1.txt'))