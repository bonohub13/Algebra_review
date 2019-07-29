#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Permutations:
    def __init__(self):
        self.permutations
        self.combinations

    def permutations(self, x=1, y=1):
        N = [a+1 for a in range(x)]
        N_R = [b+1 for b in range(x-y)]
        Pn, Pn_r = 1, 1
        for i in N:
            Pn *= i
        for j in N_R:
            Pn_r *= j
        return Pn/Pn_r

    def combinations(self, x=1, y=1):
        N = [a+1 for a in range(x)]
        n_R = [b+1 for b in range(x-y)]
        R = [c+1 for c in range(y)]
        n, r, n_r = 1, 1, 1
        for i in N:
            n *= i
        for j in n_R:
            n_r *= j
        for k in R:
            r *= k
        return n/(n_r*r)

# test lines
if __name__ == "__main__":
    P = Permutations()
    print(P.permutations)
    print(P.combinations)
