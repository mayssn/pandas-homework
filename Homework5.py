import numpy as np

# Creating an array
elements = np.array([1.0,22.4,5.0,35.0,4.0,6.7,3.0,8.0,40.0])

# Printing the array
print(elements)

# Experimenting with ndim and other
print(elements.ndim)    #the dimensions of an array, it is a line so 1
print(elements.shape)   #his is a tuple of integers indicating the size of the array in each dimension
print(elements.size)    #the total number of elements of the array.
print(elements.dtype)   # the data type (in which case is float)

# Creating a matrix
matrix= np.matrix([['a', 'b'],['c', 'd'],['3', '3']], dtype=object)
print(matrix)

#Create numpy 1 dimension array using each of the functions arange and rand
randomname=np.arange(19)
print(randomname)
print(randomname.ndim)

randomname2=np.random.rand(5)
print(randomname2)
print(randomname2.ndim)

#Create numpy 2 dimensions matrix using each of the functions zeros and rand
randomname3=np.eye(2, dtype= int)
print(randomname3)
print(randomname3.ndim)

randomname4=np.random.rand(5,6)
print(randomname4)
print(randomname4.ndim)

#Create an array containing 20 times the value 7. Reshape it to a 4 x 5 Matrix
randomname5a=np.ones((5, 4))
randomname5=randomname5a * 7
print(randomname5)

# Create a 6 x 6 matrix with all numbers up to 36
randomname6=np.arange(1,37) .reshape(6,6)
print(randomname6)  # just testing

#only the first element on it
print(randomname6[:1, :1])

# last two rows
print(randomname6[4:])

#only the two mid columns and 2 mid rows for it
print (randomname6[2:4, 2:4])

#sum values of each column
print(np.sum(a=randomname6, axis=0))
