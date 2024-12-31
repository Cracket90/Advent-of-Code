# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 00:18:14 2024

@author: andre
"""

def signal_A_wire(input_file: str) -> int:
    with open(input_file) as f:
        instructions = f.read().strip().splitlines()
    wires: dict[str|None,int] = {None: 0}
    operations = []
    for instruction in instructions:
        operation_data, res = instruction.split(' -> ')
        l = len(operation_data.split())
        if l == 1:
            operations.append((operation_data, None, 'ASSIGN', res))
        elif l == 2:
            op, in1 = operation_data.split()
            operations.append((in1, None, 'NOT', res))
        else:
            in1, op, in2 = operation_data.split()
            operations.append((in1, in2, op, res))   # type: ignore
    while operations:
        operation = operations.pop(0)
        in1, in2, op, res = operation   # type: ignore
        if ((in1 in wires or in1.isdecimal())
            and (in2 in wires or in2.isdecimal())):
                input1 = wires[in1] if in1 in wires else int(in1)
                input2 = wires[in2] if in2 in wires else int(in2)
                wires[res] = do_operation(input1, input2, op)
        else:
            operations.append(operation)
    return wires['a']

def new_signal_A_wire(input_file: str) -> int:
    with open(input_file) as f:
        instructions = f.read().strip().splitlines()
    wires: dict[str|None,int] = {None: 0}
    operations = []
    for instruction in instructions:
        operation_data, res = instruction.split(' -> ')
        l = len(operation_data.split())
        if l == 1:
            operations.append((operation_data, None, 'ASSIGN', res))
        elif l == 2:
            op, in1 = operation_data.split()
            operations.append((in1, None, 'NOT', res))
        else:
            in1, op, in2 = operation_data.split()
            operations.append((in1, in2, op, res))   # type: ignore
    new_operations = operations.copy()
    while operations:
        operation = operations.pop(0)
        in1, in2, op, res = operation   # type: ignore
        if ((in1 in wires or in1.isdecimal())
            and (in2 in wires or in2.isdecimal())):
                input1 = wires[in1] if in1 in wires else int(in1)
                input2 = wires[in2] if in2 in wires else int(in2)
                wires[res] = do_operation(input1, input2, op)
        else:
            operations.append(operation)
    value = wires['a']
    wires.clear()
    wires = {None: 0, 'b': value}
    while new_operations:
        operation = new_operations.pop(0)
        in1, in2, op, res = operation   # type: ignore
        if (res not in wires and (in1 in wires or in1.isdecimal())
            and (in2 in wires or in2.isdecimal())):
                input1 = wires[in1] if in1 in wires else int(in1)
                input2 = wires[in2] if in2 in wires else int(in2)
                wires[res] = do_operation(input1, input2, op)
        elif res in wires:
            continue
        else:
            new_operations.append(operation)
    return wires['a']

def do_operation(in1: int, in2: int, op: str) -> int:
    mod = 2**16
    match op:
        case 'ASSIGN':
            res = in1
        case 'NOT':
            res = (~in1) % mod
        case 'AND':
            res = in1 & in2
        case 'OR':
            res = in1 | in2
        case 'LSHIFT':
            res = in1 << in2
        case 'RSHIFT':
            res = in1 >> in2
    return res

if __name__ == '__main__':
    print(signal_A_wire('input_day7.txt'))
    print(new_signal_A_wire('input_day7.txt'))
