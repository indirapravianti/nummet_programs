import numpy as np

c = [0.555555556, 0.88888889, 0.555555556]
t = [-0.774596669, 0, 0.774596669]


b = 3
a = -2
# equation = ((0.5*(w[i]**2))+np.exp(3*w[i]))

w = []
q=  []
e = []
for i in range(len(t)):
    print(((b-a)/2*t[i]) + ((b+a)/2))
    w.append(((b-a)/2*t[i]) + ((b+a)/2))

for i in range(len(w)):
    print(((0.5*(w[i]**2))+np.exp(3*w[i])))
    q.append((0.5*(w[i]**2))+np.exp(3*w[i]))

for (m, n) in zip(c, q):
    print(m*n)
    e.append(m*n)

print(2.5*sum(e))


# x = [1,2,3]
# y = [4,5,6]

# for a,b in zip(x,y):
#     print(a+b)