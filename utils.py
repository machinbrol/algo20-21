#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randrange
from time import time


# crée une liste d'éléments aléatoires entre 0 et valrange, de taille `size`, comprenant environ p% de valeurs `val`
def rand_list(size=10, p=50, val=0, val_range = 10):
    lst = list()

    for i in range(size):
        rnd = randrange(100)

        if rnd < 50:
            lst.append(val)
        else:
            # comme randrange peut choisir val, la distribution de `val` sera un peu plus grande que `p`.
            lst.append(randrange(val_range))
    
    return lst



