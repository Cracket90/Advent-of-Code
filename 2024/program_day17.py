# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 10:18:50 2024

@author: andre
"""

def output_program(input_file: str) -> str:
    with open(input_file) as f:
        data1, data2 = f.read().strip().split('\n\n')
    registers = {}
    for line in data1.split('\n'):
        name, value = line.split(':')
        registers[name[-1]] = int(value)
    program = list(map(int, data2.split(':')[1].split(',')))
    num_instr = len(program)
    output: list[str] = []
    pointer = 0
    while pointer < num_instr:
        # print(pointer, program, registers, ','.join(output), sep='\n')
        opcode = program[pointer]
        operand = program[pointer+1]
        match opcode:
            case 0:
                adv(operand, registers)
            case 1:
                bxl(operand, registers)
            case 2:
                bst(operand, registers)
            case 3:
                pointer = jnz(operand, pointer, registers)
            case 4:
                bxc(registers)
            case 5:
                output.append(out(operand, registers))
            case 6:
                bdv(operand, registers)
            case 7:
                cdv(operand, registers)
        pointer += 2
    return ','.join(output)

# def find_register_A(input_file: str) -> int:
#     with open(input_file) as f:
#         data1, data2 = f.read().strip().split('\n\n')
#     program = list(map(int, data2.split(':')[1].split(',')))
#     output = program[::-1]
#     possible_A_values = ['']
#     for value in output:
#         next_possible_A_values = []
#         for r in possible_A_values:
#             for l in ['000', '001', '010', '011', '100', '101', '110', '111']:
#                 a = int(r+l, 2)
#                 b = a % 8
#                 b = b ^ 1
#                 c = a >> b
#                 b = b ^ 5
#                 b = b ^ c
#                 if b % 8 == value:
#                     next_possible_A_values.append(bin(a)[2:])
#         possible_A_values = next_possible_A_values
#     ans = min(int(value, 2) for value in possible_A_values)
#     return ans

def find_register_A(input_file: str) -> int:
    with open(input_file) as f:
        data1, data2 = f.read().strip().split('\n\n')
    registers_init = {}
    for line in data1.split('\n'):
        name, value_init = line.split(':')
        registers_init[name[-1]] = int(value_init)
    program = list(map(int, data2.split(':')[1].split(',')))
    output = program[::-1]
    possible_A_values = ['']
    for value in output:
        next_possible_A_values = []
        for r in possible_A_values:
            for l in ['000', '001', '010', '011', '100', '101', '110', '111']:
                registers_init['A'] = int(r+l, 2)
                registers = {}
                registers['A'] = registers_init['A']
                registers['B'] = registers_init['B']
                registers['C'] = registers_init['C']
                for pointer in range(0, len(program), 2):
                    opcode = program[pointer]
                    operand = program[pointer+1]
                    match opcode:
                        case 0:
                            adv(operand, registers)
                        case 1:
                            bxl(operand, registers)
                        case 2:
                            bst(operand, registers)
                        case 3:
                            jnz(operand, pointer, registers)
                        case 4:
                            bxc(registers)
                        case 5:
                            res = out(operand, registers)
                            if value == int(res):
                                next_possible_A_values.append(bin(registers_init['A'])[2:])
                        case 6:
                            bdv(operand, registers)
                        case 7:
                            cdv(operand, registers)
        possible_A_values = next_possible_A_values
    ans = min(int(value, 2) for value in possible_A_values)
    return ans

def combo_operands(operand: int, registers: dict[str,int]) -> int:
    match operand:
        case 0 | 1 | 2 | 3:
            combo_operand = operand
        case 4:
            combo_operand = registers['A']    # type: ignore
        case 5:
            combo_operand = registers['B']    # type: ignore
        case 6:
            combo_operand = registers['C']    # type: ignore
        case 7:
            raise('Error: program is not valid')    # type: ignore
    return combo_operand

def adv(operand: int, registers: dict[str,int]) -> None:
    num = registers['A']
    den = 2**(combo_operands(operand, registers))
    res = num // den
    registers['A'] = res
    return

def bxl(operand: int, registers: dict[str,int]) -> None:
    res = registers['B'] ^ operand
    registers['B'] = res
    return

def bst(operand: int, registers: dict[str,int]) -> None:
    res = combo_operands(operand, registers) % 8
    registers['B'] = res
    return

def jnz(operand: int, pointer: int, registers: dict[str,int]) -> int:
    if registers['A']:
        pointer = operand-2
    return pointer

def bxc(registers: dict[str,int]) -> None:
    res = registers['B'] ^ registers['C']
    registers['B'] = res
    return

def out(operand: int, registers: dict[str,int]) -> str:
    value = combo_operands(operand, registers) % 8
    return str(value)

def bdv(operand: int, registers: dict[str,int]) -> None:
    num = registers['A']
    den = 2**(combo_operands(operand, registers))
    res = num // den
    registers['B'] = res
    return

def cdv(operand: int, registers: dict[str,int]) -> None:
    num = registers['A']
    den = 2**(combo_operands(operand, registers))
    res = num // den
    registers['C'] = res
    return

# def find_register_A(input_file: str) -> int:
#     with open(input_file) as f:
#         data1, data2 = f.read().strip().split('\n\n')
#     registers_init = {}
#     for line in data1.split('\n'):
#         name, value = line.split(':')
#         registers_init[name[-1]] = int(value)
#     program = list(map(int, data2.split(':')[1].split(',')))
#     num_instr = len(program)
#     output: list[str] = []
#     registers_init['A'] = 2**(3*(len(program)-1))-1
#     while output != list(map(str, program)):
#         output = []
#         registers_init['A'] += 1
#         registers = {}
#         registers['A'] = registers_init['A']
#         registers['B'] = registers_init['B']
#         registers['C'] = registers_init['C']
#         # print(registers['A'])
#         pointer = 0
#         while pointer < num_instr:
#             opcode = program[pointer]
#             operand = program[pointer+1]
#             match opcode:
#                 case 0:
#                     adv(operand, registers)
#                 case 1:
#                     bxl(operand, registers)
#                 case 2:
#                     bst(operand, registers)
#                 case 3:
#                     pointer = jnz(operand, pointer, registers)
#                 case 4:
#                     bxc(registers)
#                 case 5:
#                     output.append(out(operand, registers))
#                     if output != list(map(str, program[:len(output)])):
#                         break
#                 case 6:
#                     bdv(operand, registers)
#                 case 7:
#                     cdv(operand, registers)
#             pointer += 2
#         # print(registers, ','.join(output), sep='\n')
#     return registers_init['A']

if __name__ == '__main__':
    print(output_program('input_day17.txt'))
    print(find_register_A('input_day17.txt'))