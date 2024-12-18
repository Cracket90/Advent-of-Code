# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 08:38:40 2024

@author: andre
"""

def fewest_tokens(input_file: str) -> int:
    ans = 0
    tokA = 3
    tokB = 1
    with open(input_file) as f:
        data = f.read().strip().split('\n\n')
    machines = []
    for el in data:
        machine = {}
        butA, butB, prize = el.split('\n')
        X_A, Y_A = butA.split(':')[1].split(',')
        xA, yA = int(X_A.split('+')[1]), int(Y_A.split('+')[1])
        machine['A'] = (xA, yA)
        X_B, Y_B = butB.split(':')[1].split(',')
        xB, yB = int(X_B.split('+')[1]), int(Y_B.split('+')[1])
        machine['B'] = (xB, yB)
        xA, yA = int(X_A.split('+')[1]), int(Y_A.split('+')[1])
        X_P, Y_P = prize.split(':')[1].split(',')
        xP, yP = int(X_P.split('=')[1]), int(Y_P.split('=')[1])
        machine['prize'] = (xP, yP)
        machines.append(machine)
    for machine in machines:
        xA, yA = machine['A']
        xB, yB = machine['B']
        xP, yP = machine['prize']
        nA = (xB*yP-yB*xP) // (xB*yA-xA*yB)
        rA = (xB*yP-yB*xP) % (xB*yA-xA*yB)
        nB = (xA*yP-yA*xP) // (xA*yB-xB*yA)
        rB = (xA*yP-yA*xP) % (xA*yB-xB*yA)
        if rA == 0 and rB == 0:
            ans += nA*tokA + nB*tokB
    return ans

def fewest_tokens2(input_file: str) -> int:
    ans = 0
    tokA = 3
    tokB = 1
    extra = 10000000000000
    with open(input_file) as f:
        data = f.read().strip().split('\n\n')
    machines = []
    for el in data:
        machine = {}
        butA, butB, prize = el.split('\n')
        X_A, Y_A = butA.split(':')[1].split(',')
        xA, yA = int(X_A.split('+')[1]), int(Y_A.split('+')[1])
        machine['A'] = (xA, yA)
        X_B, Y_B = butB.split(':')[1].split(',')
        xB, yB = int(X_B.split('+')[1]), int(Y_B.split('+')[1])
        machine['B'] = (xB, yB)
        xA, yA = int(X_A.split('+')[1]), int(Y_A.split('+')[1])
        X_P, Y_P = prize.split(':')[1].split(',')
        xP, yP = int(X_P.split('=')[1]) + extra, int(Y_P.split('=')[1]) + extra
        machine['prize'] = (xP, yP)
        machines.append(machine)
    for machine in machines:
        xA, yA = machine['A']
        xB, yB = machine['B']
        xP, yP = machine['prize']
        nA = (xB*yP-yB*xP) // (xB*yA-xA*yB)
        rA = (xB*yP-yB*xP) % (xB*yA-xA*yB)
        nB = (xA*yP-yA*xP) // (xA*yB-xB*yA)
        rB = (xA*yP-yA*xP) % (xA*yB-xB*yA)
        if rA == 0 and rB == 0:
            ans += nA*tokA + nB*tokB
    return ans

if __name__ == '__main__':
    print(fewest_tokens('input_day13.txt'))
    print(fewest_tokens2('input_day13.txt'))