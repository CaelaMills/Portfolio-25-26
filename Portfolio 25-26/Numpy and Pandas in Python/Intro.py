import numpy as np

list1 = [1, 2, 3, 4, 5]

list2 = ["Caela Mills", 38, list1, True]

np1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(np1)

# The .shape function lets us know how many items there are in our array
print (np1.shape)

np2 = np.arange(10)
print (np2)

# You can make steps within an array, steps of 2 (i.e., 2, 4, 6, 8, etc.) or 3 (3, 6, 9, etc.)
np3 = np.arange(0,10, 2)
print (np3)

# You can make an array of zeros (in decimal form, not integers)
np4 = np.zeros(10)
print (np4)

# Multidimensional zeros
np5 = np.zeros((2,10))
print (np5)

# It will print two dimension of zeros like this:
# [[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]

# Slicing Numpy arrays
# ***All arrays start at 0
np6 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print (np6[1:5])

# Return from the middle to the end of an array
print(np6[3:]) # Should return numbers between 3 and 9 (not including 3, that's just 4-9)

# Return negatve slides
print(np6[-3:-1]) # Which will return 7 (starting from 9, including 9, and counting down 3 to seven
# Then counting down -1 which is 8
print(np6[1:5]) # Should print 2-5 (2, 3, 4, 5)

# Steps through an entire array
print(np6[::2]) # skipping numbers divisible by 2
