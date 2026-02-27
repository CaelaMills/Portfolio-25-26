import numpy as np

# Slicing Numpy arrays
# ***All arrays start at 0
np6 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print (np6[1:5])

# Slice a 2-d array
# 1-5 = the zeroth item array
# 6-10 is the oneth item array
np7 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]) # double square braces since its a tuple

# Pull out the 1st item from the oneth array
print (np7[1,2]) # It will extract 8 from the oneth array

# From the zeroth array up to but not including the oneth array
print (np7[0:1, 1:3]) # Numbers from 1 to 3, not ncluding 3; this will return 2 & 3

# Numpy Universal Functions ("u-funks")
# Using the np6 array I already made
np6 = np.array([-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print (np6)

# Square root of each element
print (np.sqrt(np6))

# Finding the absolute value
#print(np.absolute(np6))

# Exponents
print (np.exp(np6))

# Min/Max
print (np.min(np6 ))
print (np.max(np6 ))

# Trig sin cos log
print(np.log(np6))
