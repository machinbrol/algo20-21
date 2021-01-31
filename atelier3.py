#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fusion(lst1, lst2):
    res = list()
    i = 0
    j = 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1
        
    if i == len(lst1):
        res.extend(lst2[j:])
    else:
        res.extend(lst1[i:])
    
    return res


if __name__ == "__main__":
    print(fusion([1, 2, 4, 4, 8], [3, 5, 6, 9]))
