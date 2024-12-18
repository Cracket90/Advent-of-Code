# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 08:57:14 2024

@author: andre
"""

def filesystem_checksum(input_file: str) -> int:
    checksum = 0
    with open(input_file) as f:
        data = f.read().strip()
    disk_map: list[int|str] = []
    ID_file = -1
    space = '.'
    for i, value in enumerate(data):
        if i % 2 == 0:
            ID_file += 1
            disk_map.extend([ID_file]*int(value))
        else:
            disk_map.extend([space]*int(value))
    start = 0
    end = len(disk_map)-1
    while start < end:
       if disk_map[start] == space:
           while end > start:
               if disk_map[end] != space:
                   disk_map[start], disk_map[end] = disk_map[end], disk_map[start]
                   end -= 1
                   break
               end -= 1
       start += 1
    for i, num in enumerate(disk_map):
        if num != space:
            checksum += i*num   # type: ignore
    return checksum

# def new_filesystem_checksum(input_file: str) -> int:
#     checksum = 0
#     with open(input_file) as f:
#         data = f.read().strip()
#     disk_map: list[int|str] = []
#     ID_file = -1
#     space = '.'
#     for i, value in enumerate(data):
#         if i % 2 == 0:
#             ID_file += 1
#             disk_map.extend([ID_file]*int(value))
#         else:
#             disk_map.extend([space]*int(value))
#     # print(disk_map)
#     start = 0
#     end = len(disk_map)-1
#     while end > start:
#        if disk_map[end] != space:
#            k = disk_map[end]
#            file_space = 1
#            while disk_map[end-file_space] == k:
#                file_space += 1
#            end -= file_space-1
#            while start < end:
#                if disk_map[start] == space:
#                    free_space = 1
#                    while disk_map[start+free_space] == space:
#                        free_space += 1
#                    diff = free_space - file_space
#                    if diff >= 0:
#                        for n in range(file_space):
#                            disk_map[start+n], disk_map[end+n] = disk_map[end+n], disk_map[start+n]
#                        break
#                    start += free_space-1
#                start += 1
#        end -= 1
#        start = disk_map.index(space)
#        # print(disk_map)
#     for i, num in enumerate(disk_map):
#         if num != space:
#             checksum += i*num   # type: ignore
#     return checksum

def new_filesystem_checksum(input_file: str) -> int:
    checksum = 0
    with open(input_file) as f:
        data = f.read().strip()
    disk_map = []
    ID_file = -1
    space = '.'
    for i, value in enumerate(data):
        if i % 2 == 0:
            ID_file += 1
            if value != '0':
                disk_map.extend([[ID_file]*int(value)])
        else:
            disk_map.extend([[space]]*int(value))   # type: ignore
    # print(disk_map)
    start = 0
    end = len(disk_map)-1
    while end > start:
       if disk_map[end][0] != space:
           file_space = len(disk_map[end])
           while start < end:
               if disk_map[start][0] == space:
                   free_space = 1
                   while disk_map[start+free_space][0] == space:
                       free_space += 1
                   diff = free_space - file_space
                   if diff >= 0:
                       disk_map = (disk_map[:start] + disk_map[end:end+1] +
                                   disk_map[start+file_space:end] +
                                   disk_map[start:start+file_space] + disk_map[end+1:])
                       break
                   start += free_space-1
               start += 1
       end -= 1
       start = disk_map.index([space])   # type: ignore
       # print(disk_map)
    new_disk_map = []
    for file in disk_map:
        new_disk_map.extend(file)
    for i, num in enumerate(new_disk_map):
        if num != space:
            checksum += i*num
    return checksum

if __name__ == '__main__':
    print(filesystem_checksum('input_day9.txt'))
    print(new_filesystem_checksum('input_day9.txt'))
