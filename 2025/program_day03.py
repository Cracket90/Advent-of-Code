# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 08:43:02 2025

@author: andre
"""

def find_joltage1(input_file: str) -> int:
    output = 0
    with open(input_file, encoding= 'utf8') as f:
        banks = f.read().strip().split('\n')
    for bank in banks:
        first_battery = '1'
        second_battery = '1'
        index = first_index = 0
        while index < len(bank)-1:
            if bank[index] > first_battery:
                first_battery = bank[index]
                first_index = index
            index += 1
        index = first_index + 1
        while index < len(bank):
            if bank[index] > second_battery:
                second_battery = bank[index]
            index += 1
        output += (int(first_battery)*10 + int(second_battery))
    return output

def find_joltage2(input_file: str, digits: int) -> int:
    output = 0
    with open(input_file, encoding= 'utf8') as f:
        banks = f.read().strip().split('\n')
    for bank in banks:
        output += joltage_bank(bank, digits)
    return output

def joltage_bank(bank: str, digits: int) -> int:

    def joltage_bank_ric(bank: str, digits: int, start: int) -> int:
        if digits < 1:
            return 0
        battery = '1'
        power = 10 ** (digits-1)
        index = battery_index = start
        end = len(bank) - digits
        while index <= end:
            if bank[index] > battery:
                battery = bank[index]
                battery_index = index
            index += 1
        return int(battery)*power + joltage_bank_ric(bank, digits-1, battery_index+1)

    start = 0
    return joltage_bank_ric(bank,digits, start)

def find_joltage2_iter(input_file: str, digits: int) -> int:
    output = 0
    with open(input_file, encoding= 'utf8') as f:
        banks = f.read().strip().split('\n')
    for bank in banks:
        output += joltage_bank_iter(bank, digits)
    return output

def joltage_bank_iter(bank: str, digits: int) -> int:
    joltage = 0
    start = 0
    for i in range(digits-1, -1, -1):
        battery = '1'
        power = 10 ** i
        index = battery_index = start
        end = len(bank) - i - 1
        while index <= end:
            if bank[index] > battery:
                battery = bank[index]
                battery_index = index
            index += 1
        joltage += int(battery)*power
        start = battery_index + 1
    return joltage


if __name__ == '__main__':
    print(find_joltage1('input_day3.txt'))
    print(find_joltage2('input_day3.txt', 12))
    print(find_joltage2_iter('input_day3.txt', 12))
