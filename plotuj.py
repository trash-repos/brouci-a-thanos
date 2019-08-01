import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from os.path import isfile, join



files = [fd for fd in ( join('data_1e8/', f) for f in listdir('data_1e8/') ) if isfile(fd)]

mu_all = []
L_all = []
P_all = []
A_all = []
A0_all = []

for f in files:
    matrix = np.loadtxt(f, usecols=range(5))
    mu= matrix[:,0]
    L = matrix[:,1]
    P = matrix[:,2]
    A = matrix[:,3]
    A0 = matrix[:,4]

    print(A0[0])

    mu_all.extend(mu)
    L_all.extend(L)
    P_all.extend(P)
    A_all.extend(A)
    A0_all.extend(A0)


count = len(mu_all)
indexRange = range(0, count)

total_all = [ L_all[i] + P_all[i] + A_all[i] for i in indexRange ]

####mohek................................................................................
from bokeh.plotting import figure, show, save, output_file

output_file('bifurcation_diagram.html', title='bifurcation_diagram')
fig = figure(plot_height=600, plot_width=1200,
             x_range=(0,1), y_range=(-5, 750),
             toolbar_location="below", x_axis_label='úmrtnost brouků',
             y_axis_label='populace')
fig.legend.location='top_left'

s = 1 #size óf points
fig.circle(x=mu_all, y=A_all, color='blue', size=s,legend='larvy')
fig.circle(x=mu_all, y=P_all, color='green', size=s, legend='kukly')
fig.circle(x=mu_all, y=L_all, color='red', size=s, legend='brouci')
fig.circle(x=mu_all, y=total_all, color='black', size=s,legend='larvy + kukly + brouci')

show(fig)



####matplotlib............................................................................
# fig = plt.figure()

# ax1 = fig.add_subplot(111)

# ax1.set_title("Bifurkační diagram")
# ax1.set_xlabel('mua')
# ax1.set_ylabel('populace')

# #ax1.plot(mu, A, c='b', label='the data')

# s=0.001
# ax1.scatter(mu_all, A_all, c='black', s=s, label='A')
# ax1.scatter(mu_all, P_all, c='r', s=s, label='P')
# ax1.scatter(mu_all, L_all, c='b', s=s, label='L')
# ax1.scatter(mu_all, total_all, c='purple', s=s, label='total')


# leg = ax1.legend()
# plt.savefig("bifurcation.png", dpi=3200)
# plt.show()
