from random import random, seed
from math import exp

def sigmoid(x):
    return 1 / (1 + exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

seed(1)

x = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 1, 1, 0]

w1 = [[random(), random()],
      [random(), random()]]
b1 = [random(), random()]

w2 = [random(), random()]
b2 = random()

lr = 0.5

for _ in range(10000):
    for i in range(4):
        x0, x1 = x[i]

        h1_input = x0 * w1[0][0] + x1 * w1[1][0] + b1[0]
        h2_input = x0 * w1[0][1] + x1 * w1[1][1] + b1[1]

        h1 = sigmoid(h1_input)
        h2 = sigmoid(h2_input)

        o_input = h1 * w2[0] + h2 * w2[1] + b2
        o = sigmoid(o_input)

        error = y[i] - o

        d_out = error * sigmoid_derivative(o)
        d_h1 = d_out * w2[0] * sigmoid_derivative(h1)
        d_h2 = d_out * w2[1] * sigmoid_derivative(h2)

        w2[0] += lr * d_out * h1
        w2[1] += lr * d_out * h2
        b2 += lr * d_out

        w1[0][0] += lr * d_h1 * x0
        w1[1][0] += lr * d_h1 * x1
        w1[0][1] += lr * d_h2 * x0
        w1[1][1] += lr * d_h2 * x1
        b1[0] += lr * d_h1
        b1[1] += lr * d_h2

print("XOR outputs:")
for i in range(4):
    x0, x1 = x[i]
    h1 = sigmoid(x0 * w1[0][0] + x1 * w1[1][0] + b1[0])
    h2 = sigmoid(x0 * w1[0][1] + x1 * w1[1][1] + b1[1])
    o = sigmoid(h1 * w2[0] + h2 * w2[1] + b2)
    print(f"{x[i]} -> {round(o)}")
