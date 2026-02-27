import numpy as np

# Create 1-D Numpy Array and Get Shape
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) # There are
# 12 items; the shape will return 12
print (np1)
print (np1.shape)

# Create 2-D array and get shape of two arrays
# Since these two arrays are in one single brackets []; so there are two items
# in the first array because of the two arrays themselves 
'''
np2 = np.array([[1, 2, 3, 4, 5, 6],[7, 8, 9, 10, 11, 12]])
print (np2)
print (np2.shape)
'''

# Reshape 2-D
np3 = np1.reshape(3, 4) # Print 3 different arrays with 4 items per array
print (np3)

# Reshape 3-D
np4 = np1.reshape(2, 3, 2) # 2 items per array, 2 rows and 3 columns of numbers
# note the line break between the sets of arrays
print (np4)

# Flatten a 1-D array
np5 = np4.reshape(-1)
print (np5)

'''
# Iterating using np1 array object again
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
for x in np1:
    print (x) # Prints every x which is every item or number

np2 = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
for x in np2:
    print (x)
    for y in x:
        print (y)
'''

np3 = np.array([[[1, 2, 3],[4, 5, 6], [7, 8,9],[10, 11, 12]]])
# The whole array (1-12) in between anotheer set of brackets with the
# individual arrays already enclosed in their own sets of brackets makes this
# entire array a 3 dimensional array...from what I understand

# Using np.nditer()
for x in np.nditer(np3):
    print (x)


