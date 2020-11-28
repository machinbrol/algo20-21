#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randrange
from time import time


def swap(ls, a, b):
    ls[a], ls[b] = ls[b], ls[a]


# retourne une liste de taille 'size' composée de -1, 0 ou 1 distribués de manière aléatoire
def get_list(size):
    lst = []
    for i in range(size):
        lst.append(randrange(1,4) - 2)
    return lst


# ------- Exercice 4 -------

#  fonction qui regroupe les éléments d’un tableau composé exclusivement des entiers -1, 0 et 1 
#  de façon à ce que tous les -1 soient au début, suivis des 0 et, finalement des 1
def regroupe_1(ls):
    negs = 0
    zeros = 0

    for i in range(len(ls)):
        val = ls[i]
        if val == -1:
            negs += 1
        elif val == 0:
            zeros += 1
    
    for i in range(len(ls)):
        if i < negs:
            ls[i] = -1
        elif i < negs + zeros:
            ls[i] = 0
        else:
            ls[i] = 1


# ------- Exercice 5 -------

# Ecrivez une fonction qui regroupe les éléments d’un tableau d’entiers de façon à ce que tous les négatifs 
# soient au début (dans un ordre quelconque), suivis des 0 et, finalement des positifs
def regroupe_2(ls):
    # trois partitions
    # indexes de fin des partitions
    p1 = 0
    p3 = len(ls) - 1

    # Si la valeur à idx i > 0 , échange avec p3 et décrémente p3
    # Sinon, si la valeur à l'index i est < 0, échange avec p1 et on incrément p1
    #  SAUF si i == p1,
    #    dans ce cas on ne swap pas (inutile), on incrémente p1 ET i
    # Sinon, c'est ni l'un ni l'autre (0), on incrémente i
    i = 0
    while i <= p3:
        val = ls[i]

        if val > 0:
            swap(ls, i, p3)
            p3 -= 1

        elif val < 0:
            if i == p1: # dans ce cas, le négatif est déjà à sa place, pas de swap mais on avance i ET p1
                i += 1
            else:
                swap(ls, i, p1)
            p1 += 1
  
        else: # on a un élément du milieu, on avance i
            i += 1


# ---- version 2, moins 'tricky'  -----

# bi-partition autour d'un pivot
# si plus grand que pivot, swap à droite et incrémente partition
# sinon avance jusqu'à ce qu'on atteigne le début de la partition de droite
def part2(ls, end, pivot):
    p = end # idx d'écriture
    i = 0 # idx de lecture

    while i <= p:
        if ls[i] > pivot:
            swap(ls, i, p)
            p -= 1
        else:
            i += 1
    return p

# deux bi partitions, d'abord les positifs à droite
# puis dans sous-liste 0 à droite
def regroupe_3(ls):
    p =  len(ls)-1

    p = part2(ls, p, 0) # (x > 0) à droite
    part2(ls, p, -1) # (x > -1) à droite


# ----- mesure de la complexité moyenne des deux fonctions -----


def test_regroup(regroup, lsts):
    for name, lst in lsts:
        l = lst[:]

        t0 = time()
        regroup(l)
        t = (time() - t0) * 1000

        print("{:12}: {:.1f} msec".format(name, t))


def compare_2_et_3():
    l1 = get_list(10000)
    l2 = get_list(100000)
    l4 = get_list(1000000)
    l8 = get_list(10000000)

    lists = [("10 000", l1), ("100 000", l2), ("1000 000", l4), ("10 000 000", l8)]

    print("----- regroup_1 (exercice 4) -------")
    test_regroup(regroupe_1, lists)
    print()
    
    print("----- regroup_2 (exercice 5) -------")
    test_regroup(regroupe_2, lists)

    print()
    
    print("----- regroup3 (exercice 5) -------")
    test_regroup(regroupe_3, lists)


if __name__ == "__main__":
    print("test regroup1")
    ls = [1, 0, -1, -1, 0, 1, 1, 0, -1, 1, 0, 1, -1]

    print(ls)
    regroupe_1(ls)
    print(ls)

    l1 = [0, -7, 0, 0, 5, 9, -4, 0, -2, -9, -4, -8, 2]
    l2 = [-1, -1, 0, 0, -1, -1, 0, 1, 1, 0, -1, 1, 0, 1, -1]
    l3 = [8, 0, -2, -3, 0, 4, 5, 0, -1, 11, 0, 9, 10]
    l4 = [0, 0, 0, 0]
    l5 = [-5, -1, -2, -3, -1, -4]

    lists = [l1, l2, l3 ,l4, l5]

    print()

    print("test regroup2")
    for lst in lists:
        ls = lst[:]
        print(ls)
        regroupe_2(ls)
        print(ls)
        print()

    print()
    print("test regroup 3")
    for lst in lists:
        ls = lst[:]
        print(ls)
        regroupe_3(ls)
        print(ls)
        print()
    
    print()
    compare_2_et_3()


    