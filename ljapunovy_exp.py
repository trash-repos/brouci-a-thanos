import numpy as np




def logistikuj(x, mua, mup, mul, cpa, cla, cll, b):
    L2 = b*x[2]*np.exp(-cla*x[2]-cll*x[0])
    P2 = x[0]*(1.-mul)
    A2 = x[1]*(1.-mup)*np.exp(-cpa*x[2])+x[2]*(1.-mua)
    return np.array([L2, P2, A2])

d0 = np.array([0.,0.,10e-8])
x0 = np.array([100.,100.,100.])

b = 7.48

#mua0 = 0.0036
mup0 = 0.0
mul0 = 0.267

cla0 = 0.009
cll0 = 0.012
cpa0 = 0.004

for mua0 in np.linspace(0.95,1.,5000):
    #Dojdi k atraktoru
    x1 = x0
    for x in range(400):
        x1 = logistikuj(x1, mua0, mup0, mul0, cpa0, cla0, cll0, b)
    xa = x1
    xb = x1 + d0
    sep = []
    for i in range(3000):
        xa = logistikuj(xa, mua0, mup0, mul0, cpa0, cla0, cll0, b)
        xb = logistikuj(xb, mua0, mup0, mul0, cpa0, cla0, cll0, b)
        d1 = xb-xa
        dd = np.sqrt(np.dot(d1, d1) / np.dot(d0, d0))
        sep.append(np.log(dd))
        xb = xa + (1./dd)*d1
    print(str(mul0) + " " + str(np.average(sep)))
