from mpl_toolkits.mplot3d import axes3d

import numpy as np
import matplotlib.pyplot as plt

print("Numpy is ready")

x = np.arange(-10, 10.01, 0.01)
#plt.plot(x, x**2)
#plt.show()

#plt.plot(x, np.sin(x), x, np.cos(x), x, -x)
#plt.xlabel(r'$x$')
#plt.ylabel(r'$f(x)$')
#plt.title(r'$f_1(x)=\sin(x),\ f_2(x)=\cos(x),\ f_3(x)=-x$')
#plt.grid(True)
#plt.plot(x, -x)


#plt.figure(figsize=(10,5))
#plt.plot(x, np.sin(x), label=r'$f_1(x)=\sin(x)$')
#plt.plot(x, np.cos(x), label=r'$f_2(x)=\cos(x)$')
#plt.plot(x, -x, label=r'$f_3(x)=-x$')
#plt.xlabel(r'$x$', fontsize=14)
#plt.ylabel(r'$f(x)$', fontsize=14)
#plt.grid(True)
#plt.legend(loc='best', fontsize=12)
#plt.savefig('figure_with)legend.png')


#t = np.arange(-10, 11, 1)

##subplot 1
#sp = plt.subplot(221)
#plt.plot(x, np.sin(x))
#plt.title(r'$\sin(x)$')
#plt.grid(True)

##subplot 2
#sp = plt.subplot(222)
#plt.plot(x, np.cos(x), 'g')
#plt.axis('equal')
#plt.title(r'$cos(x)$')
#plt.grid(True)

##subplot 3
#sp = plt.subplot(223)
#plt.plot(x, x**2, t, t**2, 'ro')
#plt.title(r'$x^2$')

##subplot 4
#sp = plt.subplot(224)
#plt.plot(x, x)
#sp.spines['left'].set_position('center')
#sp.spines['bottom'].set_position('center')
#plt.title(r'$x$')



#plt.subplot(111, polar=True)
#phi = np.arange(0, 2*np.pi, 0.01)
#rho = 2*phi
#plt.plot(phi, rho, lw=2)



#t = np.arange(0, 2*np.pi, 0.01)
#r = 4
#plt.plot(r*np.sin(t), r*np.cos(t), lw=3)
#plt.axis('equal')



ax = axes3d.Axes3D(plt.figure())
i = np.arange(-1, 1, 0.01)
X, Y = np.meshgrid(i, i)
Z = X**2 - Y**2
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()
