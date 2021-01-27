#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from time import time


def swap(ls, i, j):
    ls[i], ls[j] = ls[j], ls[i]


# partitionnne la sous-list start-end de ls en
# utilisant end-1 comme pivot

def partition(ls, start, end):
    if end == start:
        return start

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
    idx = k - 1
    if idx < 0 or idx > len(ls) - 1:
        raise Exception("Hors des limites de la liste")

    # k-1 pcq indexé à 0
    return kieme_aux(ls, 0, len(ls), idx)


# ------------- TESTS ---------------

# ls1 = [5, 3, 2, 6, 7, 10, 9, 1, 4, 8]

taille = 10000
ieme = int(taille/2)
ls1 = [i for i in range(1, taille + 1)]
random.shuffle(ls1)

nbr = 100
i = 0
res = kieme(ls1, ieme)

while res == ieme and i < nbr:
    random.shuffle(ls1)
    res = kieme(ls1, ieme)
    i += 1

print(res)