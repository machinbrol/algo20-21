#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randrange
from time import time

def swap(ls, a, b):
    ls[a], ls[b] = ls[b], ls[a]

#  fonction qui regroupe les éléments d’un lsleau composé exclusivement des entiers -1, 0 et 1 
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



# Ecrivez une fonction qui regroupe les éléments d’un lsleau d’entiers de façon à ce que tous les négatifs 
# soient au début (dans un ordre quelconque), suivis des 0 et, finalement des positifs
def regroupe_2(ls):
    # trois partitions
    # indexes de fin des partitions
    p1 = 0
    p3 = len(ls) - 1

    gauche = lambda x: x < 0
    droite = lambda x: x > 0
    # Si la valeur à l'index i est < 0, échange avec p1 et on incrément p1
    #  sauf si i == p1,
    #    alors on ne swap pas (inutile), on incrémente i et p1
    # sinon, si valeur à i > 0 , échange avec p3 et décrément p3
    # si c'est ni l'un ni l'autre (0), on avance
    i = 0
    while i <= p3:
        val = ls[i]

        if droite(val):
            swap(ls, i, p3)
            p3 -= 1

        elif gauche(val):
            if i == p1: # dans ce cas, le négatif est déjà à sa place, pas de swap mais on avance i ET p1
                i += 1
            else:
                swap(ls, i, p1)
            p1 += 1
  
        else: # on a un élément du milieu, on avance i
            i += 1


if __name__ == "__main__":
    ls = [0,-1,0,0,1,1,-1,0,-1,-1,-1,-1,1]
    ls = [0,-1,0,0,1,1,-1,0,-1,-1,-1,-1,0]
    ls = [0,-1,0,0,0,0,-1,0,-1,-1,-1,-1,0]
    ls = [0,-1,0,0,1,1,-1,0,-1,-1,0,0,0]
    #ls = [-1,-1,0,0,1,1,-1,0,-1,-1,0,0,0]
    ls = [1, 0, -1, -1, 0, 1, 1, 0, -1, 1, 0, 1, -1]

    print(ls)
    regroupe_1(ls)
    print(ls)

    print()
    ls = [0,-7,0,0,5,9,-4,0,-2,-9,-4,-8,2]
    ls = [1, 0, -1, -1, 0, 1, 1, 0, -1, 1, 0, 1, -1]
    ls = [8, 0, -2, -3, 0, 4, 5, 0, -1, 11, 0, 9, -10]
    # ls = [8, -1, -2, -3, 1, 4, 5, -2, -1, 11, 2, 9, -10]
    # ls = [-5, -1, -2, -3, 1, 4, 5, -2, -1, 11, 2, 9, -10]

    print(ls)
    regroupe_2(ls)
    print(ls)



