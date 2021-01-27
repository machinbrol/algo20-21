#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# complexité
# ex 1: O(n)
# ex 2: O(n) 
# ex 3, haskell, complexité: O(n)
# supAllVal x (y:ys)
#  | x == y = supAllVal x ys
#  | otherwise = y:suppAllVal x ys
#

# fn recursive calcul le max d'une liste. Déclenche exception si liste vide
# elle est récursive terminale

# en Haskell ?
# max [] = error "Liste vide"
# max ls = maxAux ls m where
#   maxAux [] m     = m
#   maxAux (x:xs) m =
#    | x > m     = maxAux xs x
#    | otherwise = maxAux xs m


def maxAux(ls, start, max):
    if start >= len(ls):
        return max
  
    if ls[start] > max:
        max = ls[start]

    return maxAux(ls, start+1, max)

def max(ls):
    if not len(ls):
        raise Exception("Liste vide")
    return maxAux(ls, 1, ls[0])

print(max([1, 8, 5, 9, 10]))