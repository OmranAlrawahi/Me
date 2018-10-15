import random

# Set up variable
y0 = 50
x0 = 50
print (x0,y0)

# Random walk one step
if random.random() < 0.5:
    y0 += 1
    x0 += 1
else:
    y0 -= 1
    x0 -= 1
print (y0,x0)



# Set up variable
y1 = 50
x1 = 50

# Random walk one step
if random.random() < 0.5:
    y1 += 1
    x1 += 1
else:
    y1 -= 1
    x1 -= 1
print (y1,x1)



answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
print(answer)

"""
y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff
x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff
sum = y_diffsq + x_diffsq
answer = sum**0.5 
print (answer)
"""