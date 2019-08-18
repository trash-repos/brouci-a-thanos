import numpy as np

b = 7.48


def logistikuj(x, mua, mup, mul, cpa, cla, cll):
    L2 = b*x[2]*np.exp(-cla*x[2]-cll*x[0])
    P2 = x[0]*(1.-mul)
    A2 = x[1]*(1.-mup)*np.exp(-cpa*x[2])+x[2]*(1.-mua)
    return np.array([L2, P2, A2])

d0 = np.array([0.,0.,10e-12])
x0 = np.array([100.,100.,100.])

#mua0 = 0.2
mup0 = 0.0
mul0 = 0.267

cla0 = 0.009
cll0 = 0.012
cpa0 = 0.004

for mua0 in np.linspace(0.8,1,10000):
    #Dojdi k atraktoru
    x1 = x0
    for x in range(500):
        x1 = logistikuj(x1, mua0, mup0, mul0, cpa0, cla0, cll0)
    xa = x1
    xb = x1 + d0
    sep = []
    for i in range(5000):
        xa = logistikuj(xa, mua0, mup0, mul0, cpa0, cla0, cll0)
        xb = logistikuj(xb, mua0, mup0, mul0, cpa0, cla0, cll0)
        d1 = xb-xa
        dd = np.sqrt(np.dot(d1, d1) / np.dot(d0, d0))
        sep.append(np.log(dd))
        xb = xa + (1./dd)*d1
    print(str(mua0) + " " + str(np.average(sep)))