import numpy as np
import math
import datetime
from itertools import product
from multiprocessing import Pool
from os import listdir, remove
from os.path import isfile, join



files = [fd for fd in ( join('data/', f) for f in listdir('data/') ) if isfile(fd)]
for f in files:
    remove(f)


a = datetime.datetime.now()

time = 200


cla = 0.009
cll = 0.012
cpa = 0.004
mul = 0.267
mup = 0
b = 7.48


def vlakno(A):
    A0 = A
    with open('data/pocitej_output_' + str(A0) + '.txt', 'w') as f:
        for L in np.linspace(1,200,3):
            L0 = L
            for P in np.linspace(1,600,4):
                P0 = P
                for mua in np.linspace(0.98,1,50): #np.linspace(0.0000,1,200000): #0.0035
                    for t in range(0, time-1):
                        L2 = b*A*np.exp(-cla*A-cll*L)
                        P2 = L*(1-mul)
                        A2 = P*(1-mup)*np.exp(-cpa*A)+A*(1-mua)
                        
                        L,P,A = L2,P2,A2
                    f.write(f'{mua:.10f} {L:.5f} {P:.5f} {A:.5f} {L0:.0f} {P0:.0f} {A0:.5f} \n')
        f.close()


pool = Pool(8)
sums = pool.map(vlakno, np.linspace(0,0.05,8))

# def vlakno(A):
#     with open('data/pocitej_output_' + str(A) + '.txt', 'w') as f:
#         for L in np.linspace(1,200,3):
#             for P in np.linspace(1,600,4):
#                 for mua in np.linspace(0.0000,1,200000): #0.0035
#                     for t in range(0, time-1):
#                         L2 = b*A*np.exp(-cla*A-cll*L)
#                         P2 = L*(1-mul)
#                         A2 = P*(1-mup)*np.exp(-cpa*A)+A*(1-mua)
                        
#                         L,P,A = L2,P2,A2
#                     f.write(f'{mua:.10f} {L:.5f} {P:.5f} {A:.5f} \n')
#         f.close()


# pool = Pool(8)
# sums = pool.map(vlakno, np.linspace(0,70,8))


print(datetime.datetime.now()-a)