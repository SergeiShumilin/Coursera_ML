import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt
import math


def f(x):
    return math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2)


def y1(x, w):
    """Уравнение полинома первой степени"""
    return w[0] + w[1] * x


def y2(x, w):
    """Уравнение полинома второй степени"""
    return w[0] + w[1] * x + w[2] * (x ** 2)


def y3(x, w):
    """Уравнение полинома третьей степени"""
    return w[0] + w[1] * x + w[2] * (x ** 2) + w[3] * (x ** 3)


xs = np.arange(1, 16)  # значения х для всех полиномов
g = [f(x) for x in xs]  # исходная функция

# 1 степень
A = np.array([[1, 1], [1, 15]])
b = np.array([f(1), f(15)])
b = np.reshape(b, (2, 1))
w = scipy.linalg.solve(A, b)
g1 = [y1(x, w) for x in xs]  # значения для полинома 1ой степени

# 2 степень
A = np.array([[1, 1, 1 ** 2], [1, 6, 6 ** 2], [1, 15, 15 ** 2]])
b = np.array([f(1), f(6), f(15)])
b = np.reshape(b, (3, 1))
w = scipy.linalg.solve(A, b)
g2 = [y2(x, w) for x in xs]

# 3 степень
A = np.array([[1, 1, 1 ** 2, 1 ** 3], [1, 4, 4 ** 2, 4 ** 3], [1, 10, 10 ** 2, 10 ** 3], [1, 15, 15 ** 2, 15 ** 3]])
b = np.array([f(1), f(4), f(10), f(15)])
b = np.reshape(b, (4, 1))
w = scipy.linalg.solve(A, b)
g3 = [y3(x, w) for x in xs]
print(w)

plt.plot(xs, g, xs, g1, xs, g2, xs, g3)
plt.show()
