import numpy as np
import math
import datetime

a = datetime.datetime.now()

time = 600

#t=0
L = 1 #larva
P = 0  #kukla
A = 0  #brouk

cla = 0.009
cll = 0.012
cpa = 0.004
mul = 0.267
mup = 0
b = 7.48

f = open('pocitej_output.txt', 'w')

for mua in np.arange(0.001,0.005,0.001):
    
    #s kanibalizmem
    for t in range(0, time-1):
        [L, P, A] = [
            b*A[t]*math.exp(-cla*A[t]-cll*L[t]),
            L[t]*(1-mul),
            P[t]*(1-mup)*math.exp(-cpa*A[t])+A[t]*(1-mua)
        ]

        #f.write(f'{L:.0f} {P:.0f} {A:.0f} ')
        

f.close()

#np.savetxt('pocitej_output.txt', np.c_[L,P,A], fmt='%.0f')

print(datetime.datetime.now()-a)