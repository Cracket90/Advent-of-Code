# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:00:09 2024

@author: andre
"""

def find_safe_reports(input_file: str) -> int:
    reports = 0
    max_distance = 3
    with open(input_file) as f:
        data = f.readlines()
    for line in data:
        report = [int(el) for el in line.split()]
        reports += int(control_safe(report, max_distance))
    return reports

def find_safe_reports_dampener(input_file: str) -> int:
    reports = 0
    max_distance = 3
    with open(input_file) as f:
        data = f.readlines()
    for line in data:
        report = [int(el) for el in line.split()]
        if control_safe(report, max_distance) == True: reports += 1
        else: reports += int(control_unsafe(report, max_distance))
    return reports

def control_safe(report: list[int], max_distance: int) -> bool:
    num_el = len(report)
    first_el = report[0]
    last_el = report[-1]
    safe_report = True
    if first_el == last_el: return False
    elif report[0] > report[-1]:
        for i in range(num_el-1):
            distance = report[i]-report[i+1]
            if distance <= 0 or distance > max_distance: return False
    else:
        for i in range(num_el-1):
            distance = report[i+1]-report[i]
            if distance <= 0 or distance > max_distance: return False
    return safe_report

def control_unsafe(report: list[int], max_distance: int) -> bool:
    num_el = len(report)
    unsafe_report = False
    for i in range(num_el):
        new_report = report[:i]+report[i+1:]
        safe_report = control_safe(new_report, max_distance)
        if safe_report: return True
    return unsafe_report

if __name__ == '__main__':
    print(find_safe_reports('input_day2.txt'))
    print(find_safe_reports_dampener('input_day2.txt'))