import numpy as np

def func(x):
    result = 3 + 4*x - 5*x**2 + 2*x**3 - x**4
    print (result)

#print(func(2)) 


# for x in range(1,6):
#     print(9*(x**2) - np.exp(3*x))

# def romberg(x):
#     r = 0.5*(x**2) + np.exp(3*x)

# for x in numpy.arange(-1.375, 3, 0.625):
#    print(0.5*(x**2) + np.exp(3*x))

def gq(x):
    return (0.5*(x**2) + np.exp(3*x))

# print (gq(-1.43649))
# print (gq(0.5))
# print (gq(2.43649))

def tutor(x):
    return (5*x*np.exp(-2*x))

# print (tutor(0.235))
# print (tutor(0.7))
# print (tutor(1.164))


for x in np.arange(2.5, 9.55, 2.35):
    print(3*np.exp(0.2*x))

w = []
z = []

# for x in range(9):
#     w.append(2.5+0.5875*x)
#     print(w[x])

# for x in range(len(w)):
#     print(3*np.exp(0.2*w[x]))
#     z.append(3*np.exp(0.2*w[x]))
# print(z[1:-1])
# z = z[1:-1]
# print(sum(z)*2)


c1 = 0.555555556
c2 = 0.888888889
c3 = 0.555555556
x1 = -0.77459669
x2 = 0
x3 = 0.77459669

def f(x):
    return((np.exp(x)*np.cos(x))/(2 + x**2))

# print((c1*f(2*x1+2)+c2*f(2*x2+2)+c3*f(2*x3+2))*2)

# print(c1*f(2*x1+2))
# print(c2*f(2*x2+2))
# print(c3*f(2*x3+2))

