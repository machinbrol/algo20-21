#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fusion(ls1, ls2):
    res = list()
    i = 0
    j = 0

    while i < len(ls1) and j < len(ls2):
        if ls1[i] < ls2[j]:
            res.append(ls1[i])
            i += 1
        else:
            res.append(ls2[j])
            j += 1
        
    if i == len(ls1):
        res.extend(ls2[j:])
    else:
        res.extend(ls1[i:])
    
    return res

if __name__ == "__main__":
    print(fusion([1,2,4,4,8], [3,5,6,9]))
