import numpy as np

# Function that asks the user to input their data
def inputData():
    print("How many data do you have?")
    n = int(input())
    x = []
    y = []

    for i in range(n):
        print("Enter data for x [%d]" % i)
        x.append(float(input()))
        print("Enter data for y [%d]" % i)
        y.append(float(input()))

    polynomialRegression(n, x, y)

# Function to calculate the needed variable then find the polynomial equation
def polynomialRegression(n, x, y):
    xSum = 0
    ySum = 0
    XYSum = 0
    XSqSum = 0
    XSqYSum = 0
    Xpw3Sum = 0
    Xpw4Sum = 0
    
    m1 = []
    m2 = []
    m3 = []

    # sum the variables
    for i in range(n):
        xSum += x[i]
        ySum += y[i]
        XYSum += x[i] * y[i]
        XSqSum += x[i] ** 2
        XSqYSum += (x[i] ** 2) * y[i]
        Xpw3Sum += x[i] ** 3
        Xpw4Sum += x[i] ** 4

    # Matrix to find the polynomial regression
    m1 = [n, xSum, XSqSum]
    m2 = [xSum, XSqSum, Xpw3Sum]
    m3 = [XSqSum, Xpw3Sum, Xpw4Sum]

    # Inverse then dot the matrix
    m = np.linalg.inv(np.array([m1, m2, m3]))
    m = m.dot([ySum, XYSum, XSqYSum])

    # Print the polynomial equation
    print("y = %.5f + (%.5f)x + (%.5f)x**2" % (m[0], m[1], m[2]))

# Program starts here
print("Welcome to Polynomial Regression calculator!")
inputData()

# for debugging purpose
#x = [35, 39, 43, 54, 56, 88, 95, 105, 112, 119]
#y = [1.73, 2.45, 3.31, 6.83, 6.99, 10.44, 16.36, 27.47, 29.06, 33.96]
#polynomialRegression(10, x, y)