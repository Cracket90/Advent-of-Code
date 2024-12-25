# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 07:32:00 2024

@author: andre
"""

# import networkx as nx
# from tqdm import tqdm

def find_connected_computers(input_file: str) -> int:
    with open(input_file) as f:
        connections = f.read().strip().split('\n')
    all_connections: dict[str,set[str]] = {}
    for connection in connections:
        pc1, pc2 = connection.split('-')
        all_connections[pc1] = all_connections.get(pc1, set()) | {pc2}
        all_connections[pc2] = all_connections.get(pc2, set()) | {pc1}
    three_connected_computers: list[set[str]] = []
    pcs = list(all_connections)
    for pc1 in pcs:
        for pc2 in all_connections[pc1]:
            for pc3 in all_connections[pc2]:
                if pc1 < pc2 < pc3 and pc3 in all_connections[pc1] and 't' in [pc1[0], pc2[0], pc3[0]]:
                    three_connected_computers.append({pc1, pc2, pc3})
    # num_pcs = len(pcs)
    # len_set = 3
    # for i in range(num_pcs-len_set+1):
    #     pc1 = pcs[i]
    #     for j in range(i+1, num_pcs-len_set+2):
    #         pc2 = pcs[j]
    #         for k in range(j+1, num_pcs-len_set+3):
    #             pc3 = pcs[k]
    #             if ({pc2, pc3}.issubset(all_connections[pc1]) and
    #                 {pc1, pc3}.issubset(all_connections[pc2]) and
    #                 {pc1, pc2}.issubset(all_connections[pc3]) and
    #                 (pc1.startswith('t') or pc2.startswith('t') or pc3.startswith('t'))):
    #                 three_connected_computers.append({pc1, pc2, pc3})
    return len(three_connected_computers)

# def find_LAN_password(input_file: str) -> str:
#     with open(input_file) as f:
#         connections = f.read().strip().split('\n')
#     G = nx.read_edgelist(connections, delimiter= '-')
#     max_clique = max(nx.algorithms.clique.find_cliques(G), key= len)
#     return ','.join(sorted(max_clique))

def find_LAN_password(input_file: str) -> str:
    with open(input_file) as f:
        connections = f.read().strip().split('\n')
    all_connections: dict[str,set[str]] = {}
    for connection in connections:
        pc1, pc2 = connection.split('-')
        all_connections[pc1] = all_connections.get(pc1, set()) | {pc2}
        all_connections[pc2] = all_connections.get(pc2, set()) | {pc1}
    max_clique = find_max_clique(set(all_connections), all_connections)
    return ','.join(sorted(max_clique))

def find_max_clique(pcs_to_control: set[str], all_connections: dict[str,set[str]],
                    clique: list[str]|None = None) -> list[str]:
    if clique is None:
        clique = []
    if not pcs_to_control:
        return clique
    max_cliques = []
    for pc in pcs_to_control:
        next_clique = clique + [pc]
        next_pcs_to_control = all_connections[pc] & pcs_to_control
        next_pcs_to_control = {el for el in next_pcs_to_control if el > pc}
        max_cliques.append(find_max_clique(next_pcs_to_control, all_connections, next_clique))
    return max(max_cliques, key= len)

if __name__ == '__main__':
    print(find_connected_computers('input_day23.txt'))
    print(find_LAN_password('input_day23.txt'))