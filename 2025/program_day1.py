# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 12:38:02 2025

@author: andre
"""

def find_password1(input_file: str) -> int:
    password = 0
    posizione = 50
    with open(input_file, mode= 'rt', encoding= 'utf-8') as f:
        for rotazione in f:
            direzione = rotazione.strip()[0]
            distanza = int(rotazione.strip()[1:])
            if direzione == 'R':
                posizione += distanza
            elif direzione == 'L':
                posizione -= distanza
            if posizione % 100 == 0:
                password += 1
    return password

def find_password2(input_file: str) -> int:
    password = 0
    posizione = 50
    with open(input_file, mode= 'rt', encoding= 'utf-8') as f:
        for rotazione in f:
            direzione = rotazione.strip()[0]
            distanza = int(rotazione.strip()[1:])
            password += (distanza // 100)
            old_posizione = posizione
            if direzione == 'R':
                posizione = (posizione + distanza) % 100
                if posizione < old_posizione:
                    password += 1
            elif direzione == 'L':
                posizione = (posizione - distanza) % 100
                if old_posizione != 0 and (posizione > old_posizione or posizione == 0):
                    password += 1
    return password

def find_password2x(input_file: str) -> int:
    password = 0
    posizione = 50
    with open(input_file, mode= 'rt', encoding= 'utf-8') as f:
        for rotazione in f:
            direzione = rotazione.strip()[0]
            distanza = int(rotazione.strip()[1:])
            for _ in range(distanza):
                if direzione == 'R':
                    passo = 1
                elif direzione == 'L':
                    passo = -1
                posizione += passo
                if posizione % 100 == 0:
                    password += 1
    return password


if __name__ == '__main__':
    print(find_password1('input_day1.txt'))
    print(find_password2('input_day1.txt'))
    print(find_password2x('input_day1.txt'))
