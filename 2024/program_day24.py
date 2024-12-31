# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 07:14:25 2024

@author: andre
"""

def find_decimal_number(input_file: str) -> int:
    with open(input_file) as f:
        data1, data2 = f.read().strip().split('\n\n')
    wire_values: dict[str,int] = {}
    operations = []
    for line in data1.split('\n'):
        wire, value = line.split(': ')
        wire_values[wire] = int(value)
    for line in data2.split('\n'):
        operation_data, res = line.split('-> ')
        in1, op, in2 = operation_data.split()
        operations.append((in1, in2, op, res))
    while operations:
        operation = operations.pop(0)
        in1, in2, op, res = operation
        if in1 in wire_values and in2 in wire_values:
            wire_values[res] = do_operation(wire_values[in1], wire_values[in2], op)
        else:
            operations.append(operation)
    bits = []
    for wire in sorted((el for el in wire_values if el.startswith('z')), reverse= True):
        bits.append(str(wire_values[wire]))
    return int(''.join(bits), 2)

def find_swapped_wires(input_file: str) -> str:
    with open(input_file) as f:
        data1, data2 = f.read().strip().split('\n\n')
    wire_values: dict[str,int] = {}
    operations = []
    msb = 'z00'
    for line in data1.split('\n'):
        wire, value = line.split(': ')
        wire_values[wire] = int(value)
    for line in data2.split('\n'):
        operation_data, res = line.split('-> ')
        in1, op, in2 = operation_data.split()
        operations.append((in1, in2, op, res))
        if res.startswith('z') and int(res[1:]) > int(msb[1:]):
            msb = res
    to_swap = set()
    for operation in operations:
        in1, in2, op, res = operation
        if res.startswith('z') and res != msb and op != 'XOR':
            to_swap.add(res)
        # if res == 'z00' and 'x00' not in [in1, in2]:
        #     to_swap.add(res)
        # if res == msb and op != 'OR':
        #     to_swap.add(res)
        if op == 'XOR' and in1[0] not in 'xy' and res[0] != 'z':
            to_swap.add(res)
        if op == 'OR':
            for suboperation in operations:
                subin1, subin2, subop, subres = suboperation
                if subres in [in1, in2] and subop != 'AND':
                    to_swap.add(subres)
        if op == 'AND' and 'x00' not in [in1, in2]:
            for suboperation in operations:
                subin1, subin2, subop, subres = suboperation
                if res in [subin1, subin2] and subop != 'OR':
                    to_swap.add(res)
    return ','.join(sorted(to_swap))

def do_operation(in1: int, in2: int, op: str) -> int:
    match op:
        case 'AND':
            res = in1 & in2
        case 'OR':
            res = in1 | in2
        case 'XOR':
            res = in1 ^ in2
    return res

if __name__ == '__main__':
    print(find_decimal_number('input_day24.txt'))
    print(find_swapped_wires('input_day24.txt'))