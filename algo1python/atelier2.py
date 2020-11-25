#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randrange
from time import time


#  fonction qui regroupe les éléments d’un tableau composé exclusivement des entiers -1, 0 et 1 
#  de façon à ce que tous les -1 soient au début, suivis des 0 et, finalement des 1
def regroupe_1(tab):
    # trois partitions
    # indexes de fin des partitions
    part1 = 0
    part3 = len(tab) - 1

    # si la valeur à l'index i est < 0, échange avec part1 et incrémente part1
    # sinon, si valeur à i > 0 , échange avec part3 et décrémente part3
    # les 0 se retrouvent au centre
    for i in range(len(tab)):
        if tab[i] < 0:
            tab[part1], tab[i] = tab[i], tab[part1]
            part1 += 1

        elif tab[i] > 0 and i < part3:
            tab[part3], tab[i] = tab[i], tab[part3]
            part3 -= 1
    
        print(i, tab)


if __name__ == "__main__":
    tab = [0,-1,0,0,1,1,-1,0,-1,-1,-1,-1,1]
    tab = [0,-1,0,0,1,1,-1,0,-1,-1,-1,-1,0]
    tab = [0,-1,0,0,0,0,-1,0,-1,-1,-1,-1,0]
    tab = [0,-1,0,0,1,1,-1,0,-1,-1,0,0,0]
    tab = [-1,-1,0,0,1,1,-1,0,-1,-1,0,0,0]

    print(tab)
    regroupe_1(tab)
    print(tab)


