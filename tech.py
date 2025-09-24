def derivative(f, x, h = 0.0001):
    return (f(x + h) - f(x))/h

def f(x):
    return x * x

print(derivative(f,3))
