# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 08:57:32 2024

@author: andre
"""

def sum_secret_numbers(input_file: str) -> int:
    with open(input_file) as f:
        init_nums = list(map(int, f.read().strip().split('\n')))
    ans = 0
    n = 2000
    for num in init_nums:
        for _ in range(n):
            mix = num << 6
            num ^= mix
            num %= 16777216
            mix = int(num >> 5)
            num ^= mix
            num %= 16777216
            mix = num << 11
            num ^= mix
            num %= 16777216
        ans += num
    return ans

def most_bananas(input_file: str) -> int:
    with open(input_file) as f:
        init_nums = list(map(int, f.read().strip().split('\n')))
    n = 2000
    mod = 2**24-1
    buyers = []
    for num in init_nums:
        prices = [(num % 10, None)]
        for i in range(1, n+1):
            mix = num << 6
            num ^= mix
            num &= mod
            mix = int(num >> 5)
            num ^= mix
            num &= mod
            mix = num << 11
            num ^= mix
            num &= mod
            digit = num % 10
            prices.append((digit, digit-prices[i-1][0]))    # type: ignore
        buyers.append(prices)
    sequences: dict[tuple,int] = {}
    for prices in buyers:
        seen = set()
        for p1, p2, p3, p4 in zip(prices[1:], prices[2:], prices[3:], prices[4:]):
            if (p1[1], p2[1], p3[1], p4[1]) not in seen:
                seen.add((p1[1], p2[1], p3[1], p4[1]))
                sequences[(p1[1], p2[1], p3[1], p4[1])] = sequences.get((p1[1], p2[1], p3[1], p4[1]), 0) + p4[0]
    return max(sequences.values())

if __name__ == '__main__':
    print(sum_secret_numbers('input_day22.txt'))
    print(most_bananas('input_day22.txt'))