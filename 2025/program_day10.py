# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 11:57:21 2025

@author: andre
"""

import numpy as np
from collections import deque
from scipy.optimize import milp, Bounds, LinearConstraint  # type: ignore

def find_fewest_presses1(input_file: str) -> int:
    with open(input_file, encoding= 'utf8') as f:
        manual = f.read().splitlines()
    table = str.maketrans('.#', '01', '[]')
    presses = 0
    for machine in manual:
        light_diagram, *button_schematics = machine.split()[:-1]
        goal = int(light_diagram.translate(table), 2)
        bits = len(light_diagram.strip('[]'))
        buttons = []
        for scheme in button_schematics:
            button = ['0'] * bits
            for index in map(int, scheme.strip('()').split(',')):
                button[index] = '1'
            buttons.append(int(''.join(button), 2))
        presses += min_presses1(goal, buttons)  # type: ignore
    return presses

def min_presses1(goal: int, buttons: list[int], seen: set[int] | None = None) -> int | None:
    if seen is None:
        seen = set()
    initial_state = 0
    buttons_pressed = 0
    states: deque[tuple[int,int]] = deque()
    states.append((initial_state, buttons_pressed))
    while states:
        state, presses = states.popleft()
        if state not in seen:
            seen.add(state)
            presses += 1
            for button in buttons:
                new_state = state ^ button
                if new_state == goal:
                    return presses
                states.append((new_state, presses))
    return None

def find_fewest_presses2(input_file: str) -> int:
    with open(input_file, encoding= 'utf8') as f:
        manual = f.read().splitlines()
    presses = 0
    for machine in manual:
        *button_schematics, joltage_levels = machine.split()[1:]
        goal = tuple(int(counter) for counter in joltage_levels.strip('{}').split(','))
        counters = len(goal)
        buttons = []
        for scheme in button_schematics:
            button = [0] * counters
            for index in map(int, scheme.strip('()').split(',')):
                button[index] = 1
            buttons.append(button)
        presses += min_presses2(goal, buttons)  # type: ignore
    return presses

def min_presses2(goal: tuple[int,...], buttons: list[list[int]]) -> int | None:
    target = np.array(goal)
    A = np.array(buttons).T
    num_vars = len(buttons)
    c = np.ones(num_vars)
    integrality = np.ones(num_vars)
    bounds = Bounds(lb=0, ub=np.inf)
    constraints = LinearConstraint(A, lb=target, ub=target)
    res = milp(c=c, integrality=integrality, bounds=bounds, constraints=constraints)
    if res.success:
        solution = np.round(res.x)
        if np.allclose(A @ solution, target):
            return int(np.sum(solution))
    return None

# def min_presses2(goal: tuple[int,...], buttons: list[list[int]],
#                  seen: set[tuple[int,...]] | None = None) -> int | None:
#     if seen is None:
#         seen = set()
#     initial_state = (0,) * len(goal)
#     buttons_pressed = 0
#     states: deque[tuple[tuple[int,...],int]] = deque()
#     states.append((initial_state, buttons_pressed))
#     while states:
#         state, presses = states.popleft()
#         if state not in seen:
#             seen.add(state)
#             presses += 1
#             for button in buttons:
#                 new_state = tuple(s + b for s, b in zip(state, button))
#                 if new_state == goal:
#                     return presses
#                 if all(s <= g for s, g in zip(new_state, goal)):
#                     states.append((new_state, presses))
#     return None


if __name__ == '__main__':
    print(find_fewest_presses1('input_day10.txt'))
    print(find_fewest_presses2('input_day10.txt'))
