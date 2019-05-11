import numpy as np

# Function that asks the user to input their data
def inputData():
    print("How many data do you have?")
    n = int(input())
   
    print("Enter data for x (separated with comma or space)")
    x0 = input().replace(',', ' ')
    print("Enter data for y (seperated with comma or space)")
    y0 = input().replace(',', ' ')

    # split string to list of float
    x = [float(i) for i in x0.split()]
    y = [float(i) for i in y0.split()]

    exponentialRegression(n, x, y)

# Function to calculates the needed variable then find the exponential equation
def exponentialRegression(n, x, y):
    sumXY = 0
    sumX = 0
    sumY = 0
    sumSqX = 0

    # duplicate y
    y1 = y
    # convert y to ln y
    y = np.log(y)

    # sum the variables
    for i in range(n):
        sumX += x[i]
        sumY += y[i]
        sumSqX += x[i] * x[i]
        sumXY += x[i] * y[i]
    
    # find a and b
    b = (n * sumXY - sumX * sumY) / (n * sumSqX - (sumX * sumX))
    a = np.exp((sumY / n) - (b * (sumX / n)))
    print("y = %.3fe**%.3fx" % (a, b))
    findJGK(n, a, b, x, y1)

# Function that finds the Error (JGK)
def findJGK(n, a, b, x, y):
    y1 = []
    r1 = []
    rSquare = 0
    for i in range(n):
        y1.append(a * np.exp(b*x[i]))
        r1.append(y[i]-y1[i])
        rSquare += r1[i]*r1[i]
    print("JGK = %.4f" % rSquare)

# Program starts here
print("Welcome to Exponential Regression calculator!")
inputData()

# for debugging purpose
#x = [35, 39, 43, 54, 56, 88, 95, 105, 112, 119]
#y = [1.73, 2.45, 3.31, 6.83, 6.99, 10.44, 16.36, 27.47, 29.06, 33.96]
#exponentialRegression(10, x, y)