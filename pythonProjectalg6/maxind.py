#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def generate_random_tree_structure(depth, max_children, used_nodes=None):
    if used_nodes is None:
        used_nodes = list()
    if depth == 0:
        return {}

    tree = {}

    if not used_nodes:
        num_children = 1
    elif len(used_nodes) == 1:
        num_children = random.randint(1, max_children)
    else:
        num_children = random.randint(0, max_children)
    node = 1

    for _ in range(num_children):
        if node in used_nodes:
            node = used_nodes[-1] + 1

        used_nodes.append(node)
        child = generate_random_tree_structure(
            depth - 1, max_children, used_nodes)

        tree[node] = child

    return tree


def display_tree_structure(tree, level=0, levels=None):
    if levels is None:
        levels = []
    if not tree:
        return

    for i, (node, child) in enumerate(tree.items()):
        if i == len(tree) - 1 and level != 0:
            levels[level - 1] = False
        branch = ''.join('│   ' if lev else '    ' for lev in levels[:-1])
        branch += "└── " if i == len(tree) - 1 else "├── "
        if level == 0:
            print(str(node))
        else:
            print(branch + str(node))
        display_tree_structure(child, level + 1, levels + [True])


def find_maximum_independent_set(tree):
    global temp, node
    if tree == {}:
        return []
    leaves = []
    branches = set()

    def traverse(t, path):
        for node, child in t.items():
            current_path = path + [node]
            if child == {}:
                if len(current_path) != 1:
                    branches.add(tuple(current_path[:-1]))
                else:
                    branches.add((current_path[-1],))
                leaves.append(node)
            traverse(child, current_path)

    traverse(tree, [])
    mlist = list(branches)
    tempor = []
    sbranches = sorted(mlist, key=len, reverse=False)
    for branch in sbranches:
        branch1 = []
        for i in range(len(branch)):
            if branch[i] not in tempor:
                branch1.append(branch[i])
        parent = tree
        if len(branch1) != 1:
            for node in branch1[:-1]:
                temp = parent
                parent = parent[node]
        else:
            temp = tree

        for key, value in parent[branch1[-1]].copy().items():
            if value == {}:
                del parent[branch1[-1]][key]
            elif len(branch1) != 1:
                temp[node][key] = value
            else:
                temp[key] = value
        del parent[branch1[-1]]
        tempor.append(branch1[-1])

    print("\n\n")
    display_tree_structure(tree)
    leav = find_maximum_independent_set(tree)
    leaves.extend(leav)

    return leaves


if __name__ == '__main__':
    random_tree = generate_random_tree_structure(4, 3)
    display_tree_structure(random_tree)
    print("\n\n", find_maximum_independent_set(random_tree))
    display_tree_structure(random_tree)
