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

    regression(n, x, y)

# Function to calculate the needed variable then find the linear equation  
def regression(n, x, y):
    sumXY = 0
    sumX = 0
    sumY = 0
    sumSqX = 0
    for i in range(n):
        sumXY += x[i] * y[i]
        sumX += x[i]
        sumY += y[i]
        sumSqX += x[i] * x[i]
    
    # for debugging purpose 
    # print("Sum XY = " + str(sumXY) + "\n" + "Sum X = " + str(sumX) + "\n" + "Sum Y = " + str(sumY) + "\n" 
    #    + "Sum Square X = " + str(sumSqX) + "\n")

    b = ((n*sumXY) - (sumX * sumY)) / ((n * sumSqX) - (sumX*sumX))
    a = (sumY / n) - ((sumX / n) * b)

    sumError = 0
    for i in range(n):
        sumError = ((y[i] - a - b * x[i])**2)
    print("Y = %.3f + %.3fX" % (a, b))
    print("Sum of error = %.3f" %(sumError))
    

# Welcome Message
print("Welcome to Linear-Regression calculator!")
inputData()
