# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:11:20 2024

@author: andre
"""

def find_ordered_updates(input_file: str) -> int:
    result = 0
    rules = []
    updates = []
    with open(input_file) as f:
        for line in f:
            if '|' in line:
                rules.append(tuple(int(el) for el in line.split('|')))
            elif ',' in line:
                updates.append(list(int(el) for el in line.split(',')))
    for update in updates:
        if all(control_rule(update, rule) for rule in rules):
            length = len(update)
            middle_page = length//2
            result += update[middle_page]
    return result

def find_disordered_updates(input_file: str) -> int:
    result = 0
    rules = []
    updates = []
    with open(input_file) as f:
        for line in f:
            if '|' in line:
                rules.append(tuple(int(el) for el in line.split('|')))
            elif ',' in line:
                updates.append(list(int(el) for el in line.split(',')))
    for update in updates:
        if not all(control_rule(update, rule) for rule in rules):
            update = ordering(update,rules)
            length = len(update)
            middle_page = length//2
            result += update[middle_page]
    return result

def control_rule(update: list[int], rule: tuple[int,...]) -> bool:
    first = rule[0]
    second = rule[1]
    if first in update and second in update:
        return update.index(first) < update.index(second)
    else: return True

def ordering(update: list[int], rules: list[tuple[int,...]]) -> list[int]:
    ordered_update = update
    for rule in rules:
        if control_rule(ordered_update, rule) == False:
            first_index = ordered_update.index(rule[0])
            second_index = ordered_update.index(rule[1])
            ordered_update[first_index], ordered_update[second_index] = ordered_update[second_index], ordered_update[first_index]
    if all(control_rule(update, rule) for rule in rules): return ordered_update
    else: return ordering(ordered_update, rules)

if __name__ == '__main__':
    print(find_ordered_updates('input_day5.txt'))
    print(find_disordered_updates('input_day5.txt'))