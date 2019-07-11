import numpy as np
import math
import datetime
from itertools import product

a = datetime.datetime.now()

time = 100


cla = 0.009
cll = 0.012
cpa = 0.004
mul = 0.267
mup = 0
b = 7.48

f = open('pocitej_output.txt', 'w')

for mua in np.linspace(0.0005,0.010,500): #0.0035
    L = 1
    P = A = 0

    for [mul, mup] in product(np.linspace(0.266,0.268,10), np.linspace(0,0.001,10)):
        for t in range(0, time-1):
            L2 = b*A*math.exp(-cla*A-cll*L)
            P2 = L*(1-mul)
            A2 = P*(1-mup)*math.exp(-cpa*A)+A*(1-mua)
            
            L,P,A = L2,P2,A2

        f.write(f'{mua:.10f} {L:.5f} {P:.5f} {A:.5f} \n')


f.close()

#np.savetxt('pocitej_output.txt', np.c_[L,P,A], fmt='%.0f')

print(datetime.datetime.now()-a)