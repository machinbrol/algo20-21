#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randrange
from time import time


#  fonction qui regroupe les éléments d’un tableau composé exclusivement des entiers -1, 0 et 1 
#  de façon à ce que tous les -1 soient au début, suivis des 0 et, finalement des 1
def regroupe_1(tab):
    negs = 0
    zeros = 0

    for i in range(len(tab)):
        val = tab[i]
        if val == -1:
            negs += 1
        elif val == 0:
            zeros += 1
    
    for i in range(len(tab)):
        if i < negs:
            tab[i] = -1
        elif i < negs + zeros:
            tab[i] = 0
        else:
            tab[i] = 1



# Ecrivez une fonction qui regroupe les éléments d’un tableau d’entiers de façon à ce que tous les négatifs 
# soient au début (dans un ordre quelconque), suivis des 0 et, finalement des positifs
def regroupe_2(tab):
    # trois partitions
    # indexes de fin des partitions
    part1 = 0
    part3 = len(tab) - 1

    # si la valeur à l'index i est < 0, échange avec part1 et incrémente part1
    # sinon, si valeur à i > 0 , échange avec part3 et décrémente part3
    # les 0 se retrouvent au centre
    i = 0
    while i <= part3:
        if tab[i] < 0:
            tab[part1], tab[i] = tab[i], tab[part1]
            part1 += 1

        elif tab[i] > 0: # s'arrêter au début de part3
            tab[part3], tab[i] = tab[i], tab[part3]
            part3 -= 1
        
        i += 1


if __name__ == "__main__":
    tab = [0,-1,0,0,1,1,-1,0,-1,-1,-1,-1,1]
    tab = [0,-1,0,0,1,1,-1,0,-1,-1,-1,-1,0]
    tab = [0,-1,0,0,0,0,-1,0,-1,-1,-1,-1,0]
    tab = [0,-1,0,0,1,1,-1,0,-1,-1,0,0,0]
    tab = [-1,-1,0,0,1,1,-1,0,-1,-1,0,0,0]

    print(tab)
    regroupe_1(tab)
    print(tab)

    print()
    tab = [0,-7,0,0,5,9,-4,0,-2,-9,-4,-8,2]

    print(tab)
    regroupe_2(tab)
    print(tab)



