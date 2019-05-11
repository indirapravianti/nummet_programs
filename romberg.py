import numpy as np
import math
# import scipy

a = 2.5
b = 7.2
ts = []
fs = []
es = []

# two segments
def two():
    print("Two segment")
    h = (b-a)/2
    for x in np.arange(a, b+h, h):
        print(3*np.exp(0.2*x))
        ts.append(3*np.exp(0.2*x))
    ans1 = (h/2)*(ts[0]+ 2*ts[1] + ts[2])
    print ("Two segment romberg: ", ans1)
    
    
# four segment

def four():
    print("Four segment")
    h = (b-a)/4
    for x in np.arange(a, b+h, h):
        print(3*np.exp(0.2*x))
        fs.append(3*np.exp(0.2*x))
    z = fs[1:-1]
    ans2 = (h/2)*(fs[0]+ 2*(sum(z)) + fs[4])
    print ("Four segment romberg: ", ans2)

#eight segment

def eight():
    print("Eight segment")
    h = (b-a)/8
    for x in np.arange(a, b+h, h):
        print(3*np.exp(0.2*x))
        es.append(3*np.exp(0.2*x))
    v = es[1:-1]
    ans3 = (h/2)*(es[0]+ 2*(sum(v)) + es[8])
    print ("Eight segment romberg: ", ans3)


# two()
# four()
eight()