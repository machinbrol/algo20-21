#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def swap(ls, i, j):
    ls[i], ls[j] = ls[j], ls[i]

# partitionnne la sous-list start-end de ls en
# prenant un pivot au hasartd
def partition(ls, start, end):
    if end == start:
        return start

    # choix pivot au hasard et placement à la fin de la liste
    rand = random.choice(range(start, end))
    swap(ls, rand, end-1)

    pivot = end - 1
    droite = pivot
    gauche = start

    while gauche < droite:
        if ls[gauche] > ls[pivot]:
            swap(ls, gauche, droite-1)
            droite -= 1
        else:
            gauche += 1

    swap(ls, droite, pivot)

    return droite


def kieme_aux(ls, start, end, k):
    pivot = partition(ls, start, end)

    if pivot == k:
        return ls[k]
    elif pivot < k:
        return kieme_aux(ls, pivot+1, end, k)
    else:
        return kieme_aux(ls, start, pivot, k)


def kieme(ls, k):
    # k-1 pcq indexé à 0
    kie = k - 1

    if kie < 0 or kie > len(ls) - 1:
        raise Exception("Out of bounds")

    return kieme_aux(ls, 0, len(ls), kie)


# ------------- TESTS ---------------

# ls1 = [5, 3, 2, 6, 7, 10, 9, 1, 4, 8]

taille = 10000
ieme = int(taille/2)
ls1 = [i for i in range(1, taille + 1)]
random.shuffle(ls1)

nbr = 1
i = 0
res = kieme(ls1, ieme)

while res == ieme and i < nbr:
    random.shuffle(ls1)
    res = kieme(ls1, ieme)
    i += 1

print(res)