import numpy as np

# Copy vs View in Numpy

np1 = np.array([0, 1, 2, 3, 4, 5])

# Create a view
np2 = np1.view() # The view function takes a snapshot of your original array but
# that you can view the changes to your copied array


print(f'Original NP1 {np1}')
print(f'Original NP2 {np2}')

np2[0] = 41 # Changing np1 to np2 means that we are connecting np1 to np2
# In other words, when we change 1st item in the np1 array using np2 and the view
# function, 0 wil become 41 and whatever is changed using np2 will be changed in
# the original np1 array.

print(f'Changed NP1 {np1}')
print(f'Original NP2 {np2}')

##############################

'''
# Create a Copy
np2 = np1.copy()
print(f'Original NP1 {np1}')
print(f'Original NP2 {np2}')

np1[0] = 41

print(f'Changed NP1 {np1}')
print(f'Original NP2 {np2}')
'''
