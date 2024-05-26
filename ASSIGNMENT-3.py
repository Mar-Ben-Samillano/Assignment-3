
import numpy as np

# Saving and writing array to a csv file
print('EXAMPLE 1')
data1 = np.array([[1, 4], [6, 7]])
np.savetxt('data1.csv', data1, delimiter=',')

# loading data files from a csv file
array = np.loadtxt('data1.csv', delimiter=',')

print('Array: \n', array)

print()

print('EXAMPLE 2')
# saving an array to a binary file
data2 = np.array([[1, 2, 3], [4, 5, 6], [9, 8, 7]])
np.save('data2.npy', data2)

# loading data from a binary file
array = np.load('data2.npy')

print('Array: \n', array)

print()

print('EXAMPLE 3')
# saving an array to a compressed file
a = np.array([[10, 5, 1], [8, 6, 0]])
b = np.array([[11, 3, 5], [10, 7, 3]])
c = np.array([[12, 4, 10], [14, 8, 6]])
np.savez('arrays.npz', arr1=a, arr2=b, arr3=c)

# loading data from a compressed file
arrays = np.load('arrays.npz')

arr1 = arrays['arr1']
arr2 = arrays['arr2']
arr3 = arrays['arr3']

print('Array 1: \n', arr1, '\nArray 2: \n', arr2, '\nArray 3: \n', arr3)
