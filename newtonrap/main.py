import math

def f(x):
    return 4 * math.exp(-0.5 * x) - x

def df(x):
    return -2 * math.exp(-0.5 * x) - 1

def newton_raphson_iteration(x):
    return x - f(x) / df(x)


x0 = 2


iterations = 4


for _ in range(iterations):
    x0 = newton_raphson_iteration(x0)


print("Bulunan kök:", x0)