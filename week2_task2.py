import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt
import math

def f(x):
    return math.sin(x/5)*math.exp(x/10)+5*math.exp(-x/2)

def y1(x,w):
    return w[0]+w[1]*x
A = np.array([[1,1],[1,15]],dtype=float)
b = np.array([f(1),f(15)])
b = np.reshape(b,(2,1))
print(A)
print(b)
w = scipy.linalg.solve(A,b)
print(w)

xs = np.arange(1,16)
f = [f(x) for x in xs]

g1 = [y1(x,w) for x in xs]

plt.plot(xs,f,g1)
plt.show()




