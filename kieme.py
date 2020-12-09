#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from time import time


def swap(ls, a, b):
    ls[a], ls[b] = ls[b], ls[a]


def kieme(ls, start, end, target):
    pivot = start
    i = pivot + 1 # idx de lecture
    
    while i <= end:
        if ls[i] <= ls[pivot]:
            swap(ls, pivot, pivot + 1) # déplacer le pivot à droite en swap avec le suivant
            if i > pivot + 1:
                swap(ls, pivot, i) # si c'est pas le suivant (déjà fait) qui doit être swap
            pivot += 1
        i += 1
    
    if pivot == target:
        return ls[pivot]

    if pivot < target:
        return kieme(ls, pivot + 1, end, target)
    else:
        return kieme(ls, start, pivot, target)


#########################
## Quick Sort (copié de https://www.geeksforgeeks.org/python-program-for-quicksort/)

 
def partition(arr, low, high):
    i = low-1         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
 
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
 
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return (i+1)
 
 
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr

    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

################## TEST ####################

ls1 = [5, 3, 2, 6, 7, 9, 0, 1, 4, 8]

ls1 = [i for i in range(100000)]
random.shuffle(ls1)

ls2 = ls1[:]

t0 = time()
res = kieme(ls1, 0, len(ls1)-1, 22)
print(time() - t0)
print(res)

t0 = time()
quickSort(ls2, 0, len(ls2)-1)
res = ls2[22]
print(time() - t0)
print(res)



