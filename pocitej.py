import numpy as np
import math
import datetime

a = datetime.datetime.now()

time = 600

#t=0
L = 5 #larva
P = 0  #kukla
A = 0  #brouk

cla = 0.009
cll = 0.012
cpa = 0.004
mup = 0
b = 7.48

f = open('pocitej_output.txt', 'w')

for mul in np.linspace(0.1,0.4,50): #0.267
    for mua in np.linspace(0.001,0.005,50): #0.0035
        
        for t in range(0, time-1):
            L2 = b*A*math.exp(-cla*A-cll*L)
            P2 = L*(1-mul)
            A2 = P*(1-mup)*math.exp(-cpa*A)+A*(1-mua)
            
            L,P,A = L2,P2,A2

            f.write(f'{L:.0f} {P:.0f} {A:.0f} \n')
    f.write('\n')
    f.close()

#np.savetxt('pocitej_output.txt', np.c_[L,P,A], fmt='%.0f')

print(datetime.datetime.now()-a)