# -*- coding: utf-8 -*-
import random
import math
import sys


def pi(N=10000):
    try:
        N = int(sys.argv[1])
    except:
        N = 10000

    if N > 1E7:
        print('elija un número menor de iteraciones')
    else:
        inside = 0
        for ite in range(0, N):
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            c =  x**2 + y**2
            if c <= 1:
                inside += 1.
        pi = inside/N*4
        error = abs((pi - math.pi)/pi)* 100
        print('pi = {:7.5f}\nerror = {:5.3f} %'.format(pi, error))
        
pi()
