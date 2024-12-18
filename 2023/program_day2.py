# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 18:13:23 2024

@author: andre
"""

def find_possible_games(input_file: str) -> int:
    BAG = {"red": 12, "green": 13, "blue": 14}
    with open(input_file, mode="r", encoding="utf-8") as f:
        DATA = f.readlines()
    sum_IDs = 0
    for line in DATA:
        game = line.rstrip("\n").split(":")
        ID_game = int(game[0].split()[1])
        possible_game = True
        extracted_sets = []
        for random_set in game[1].split(";"):
            extracted_set = {}
            for cubes in random_set.split(","):
                number, colour = cubes.split()
                extracted_set[colour] = int(number)
            extracted_sets.append(extracted_set)
        for extraction in extracted_sets:
            if any(extraction[key] > BAG[key] for key in extraction):
                possible_game = False
                break
        if possible_game:
            sum_IDs += ID_game
    return sum_IDs

def find_power_sets(input_file: str) -> int:
    with open(input_file, mode="r", encoding="utf-8") as f:
        DATA = f.readlines()
    sum_power = 0
    for line in DATA:
        game = line.rstrip("\n").split(":")[1]
        power_game = 1
        minimum_set = {"red": 0, "green": 0, "blue": 0}
        for random_set in game.split(";"):
            for cubes in random_set.split(","):
                number, colour = cubes.split()
                number = int(number)    # type: ignore
                minimum_set[colour] = (
                    number if number > (maximum := minimum_set.get(colour)) else maximum    # type: ignore
                )
        for value in minimum_set.values():
            power_game *= value
        sum_power += power_game
    return sum_power

if __name__ == '__main__':
    print(find_possible_games('input_day2.txt'))
    print(find_power_sets('input_day2.txt'))