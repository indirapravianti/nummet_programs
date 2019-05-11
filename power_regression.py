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

    exponentialRegression(n, x, y)

# Function to calculate the needed variable then find the exponential equation
def exponentialRegression(n, x, y):
    sumXY = 0
    sumX = 0
    sumY = 0
    sumSqX = 0

    # duplicate the x and y
    x1 = x
    y1 = y

    # convert x and y to log x and log y
    x = np.log10(x)
    y = np.log10(y)

    # sum the variables
    for i in range(n):
        sumX += x[i]
        sumY += y[i]
        sumSqX += x[i] * x[i]
        sumXY += x[i] * y[i]
    
    # For debugging purpose
    # print("Sum X  = %.3f\nSum Y = %.3f\nSum Square X  = %.3f\nSum XY = %.3f" % (sumX, sumY, sumSqX, sumXY))
    
    # find a and b
    b = (n * sumXY - sumX * sumY) / (n * sumSqX - (sumX * sumX))
    a = 10**((sumY / n) - (b * (sumX / n)))
    print("y = %.5fx**%.3f" % (a, b))
    findJGK(n, a, b, x1, y1)

# Define function that find the Error (JGK)
def findJGK(n, a, b, x, y):
    y1 = []
    r1 = []
    rSquare = 0
    for i in range(n):
        y1.append(a * (x[i] ** b))
        r1.append(y[i]-y1[i])
        rSquare += r1[i]*r1[i]
    print("JGK = " + str(rSquare))



# Program starts here
print("Welcome to Exponential Regression calculator!")
inputData()

# For debugging purpose
# x = [35, 39, 43, 54,  56, 88, 95, 105, 112, 119]
# y = [1.73, 2.45, 3.31, 6.83, 6.99, 10.44, 16.36, 27.47, 29.06, 33.96]
# exponentialRegression(10, x, y)