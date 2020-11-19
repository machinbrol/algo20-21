#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import *
from random import randrange
from time import time


# Supprime élément d'une liste à l'index pos
def sup_at_pos(lst: List[int], pos: int) -> List[int]:
    # len(lst) - 1 pcq qu'on get pos + 1
    while pos < len(lst) - 1:
        lst[pos] = lst[pos + 1]
        pos += 1
    
    return lst[:-1]


# Supprime toutes les valeurs val de la liste et retourne une liste rétrécie
# complexité O(n) ? (dépend de manière linéaire du nombre d'éléments dans la liste)
def sup_all_val(lst: List[int], val: int) -> List[int]:
    # un idx d'insertion et un idx de lecture
    ins_idx = 0
    lect_idx = 0

    while lect_idx < len(lst):
        if lst[lect_idx] != val:
            lst[ins_idx] = lst[lect_idx]
            ins_idx += 1

        lect_idx += 1

    return lst[:ins_idx]


# crée une liste de taille `size` comprenant environ p% de valeurs `val`
def rand_list(size=10, p=50, val=0) -> List[int]:
    val_range = 10
    lst = list()

    for i in range(size):
        rnd = randrange(100)

        if rnd < 50:
            lst.append(val)
        else:
            # comme randrange peut choisir val, la distribution de `val` sera un peu plus grande que `p`.
            lst.append(randrange(val_range))
    
    return lst


# effectue `nbr_runs` de 'sup_all_val' sur liste de taille `lst_size` et retourne le temps total en milisecondes
def time_sup_all_val(lst_size: int, nbr_runs: int = 1) -> float:
    tot_time = 0
    lst = rand_list(lst_size)

    for i in range(nbr_runs):
        test_lst = lst.copy()

        t0 = time()
        sup_all_val(test_lst, 0)
        t1 = time()
        
        tot_time += t1 - t0

    return round(tot_time * 1000, 2)


# effectue nbr_runs de `time_sup_all_val`
def time_sup_all_val_all_sizes(sizes = [10000, 20000, 40000, 80000], nbr_runs = 4):
    for n in range(nbr_runs):
        print(f"--- run {n} ---")
        for size in sizes:
            time_ms = time_sup_all_val(size)
            print(f"{size}: {time_ms} milliseconds")
        print()
    

def main():
    # lst = [1, 4, 2, 3, 4, 4, 5, 6, 4]
    # print(lst)
    # lst = sup_at_pos(lst, 2)
    # print(lst)

    # lst = sup_all_val(lst, 4)
    # print(lst)

    # rand_list()

    time_sup_all_val_all_sizes()


if __name__ == "__main__":
    main()
