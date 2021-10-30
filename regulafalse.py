import numpy as np
import matplotlib.pyplot as plt
from math import e

def f(x):
    return e**x - 5*x**2

x0 = float(input('x0: '))
x1 = float(input('x1: '))
eps = float(input('epsilon: '))

def regulafalse (x0,x1,eps):
    step = 1
    print('\n\n** --Metode Regulafalsi-- **')
    condition = True
    while condition:
        x2 = x1-(f(x1)*(x1-x0)/(f(x1)-f(x0)))
        print('Iterasi-%d, x2 = %0.6f dan f(x2) = %0.6f' % (step, x2, f(x2)))
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        step = step + 1
        condition = abs(f(x2)) > eps

    print('\n Akar Persamaan Tersebut : %0.8f' % x2)

rr = np.linspace(0, 2, 100)
plt.plot(rr, f(rr))
plt.show()
plt.savefig("Lat1Regulasi.png")

if f(x0) * f(x1) > 0.0:
    print('Nilai yang diprediksi tidak mengurung akar')
    print('Silahkan mencoba ulang prediksi nilai baru')
else:
    regulafalse(x0,x1,eps)