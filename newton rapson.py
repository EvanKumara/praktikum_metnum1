import numpy as np
import matplotlib.pyplot as plt
from math import e

def f(x):
    return e**2+x - 8*x**2

def Df(x):
    return e**2+x - 16*x

def NewtonRaphson(x0, eps):
    step = 0
    print('\n\n** --Metode Newton Raphson-- **')
    xn = x0
    for n in range(0, 100):
        fxn=f(xn)
        if abs(fxn) < eps:
            print('\n Akar Persamaan Tersebut : %0.8f' % xn)
            return xn
        Dfxn=Df(xn)
        if Dfxn == 0:
            print('Solusi Tidak Ditemukan')
            return None
        xn=xn-(fxn/Dfxn)
        step = step + 1
        print('Iterasi-%d, x = %0.8f dan f(x) = %0.8f' % (step, xn, f(xn)))
    print('Iterasi Maksimum, Solusi Tidak Ditemukan')

x0 = float(input('x0: '))
eps = float(input('epsilon: '))
NewtonRaphson(x0,eps)