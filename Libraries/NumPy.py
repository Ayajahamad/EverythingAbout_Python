"""
NumPy stands for Numerical Python. It is a powerful library used for numerical and scientific computing in Python. 
If you're dealing with numerical data, large multi-dimensional arrays, or matrices, NumPy is the go-to tool in Python.
"""

"""
What is NumPy?
NumPy is a library in Python used to work with large, multi-dimensional arrays and matrices, and it provides a collection 
of high-level mathematical functions to operate on these arrays. The core object in NumPy is the ndarray, which is a 
homogeneous n-dimensional array of fixed-size items.

NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.

ndarray: This is the main object of NumPy. It is a multi-dimensional array that allows you to store and manipulate large 
datasets efficiently.
"""

# To use NumPy in your Python code, you first need to import it. By convention, it is usually imported
import numpy as np

#--------------------------- Creating Arrays --------------------------------
# NumPy provides several methods to create arrays.

# 1. From List
arr = np.array([1,2,3,4,5])
print(f"arr = np.array([1,2,3,4,5]) =\n {arr}")

# 2. Create an array of zeros
arr1 = np.zeros((3,3))
print(f"arr1 = np.zeros((3,3)) =\n {arr1}")

# 3. Create an array of ones
arr2 = np.ones((3,3))
print(f"arr2 = np.ones((3,3)) =\n {arr2}")

# 4. Create an array with random values
arr3 = np.random.random((3,3))
print(f" arr3 = np.random.random((3,3)) =\n {arr3}")

# ------------- Array Indexing and Slicing ------------------ Same as List
# You can access and modify elements of a NumPy array using indexing and slicing.

# 1. Indexing
arr4 = np.array([10, 20, 30, 40])
print('Indexing = ' ,arr4[2])  # Output: 30

# 2. Slicing
arr5 = np.array([10, 20, 30, 40, 50])
print('Slicing = ', arr5[1:4])  # Output: [20 30 40]


# --------------------- Array Operations -------------------
# NumPy arrays support a wide range of mathematical operations.

# Element-wise operations (add, subtract, multiply, divide)
arr6 = np.array([1, 2, 3])
arr7 = np.array([4, 5, 6])

print(arr6 + arr7)  # Output: [5 7 9]
print(arr6 - arr7)  # Output: [-3 -3 -3]
print(arr6 * arr7)  # Output: [4 10 18]
print(arr6 / arr7)  # Output: [0.25 0.4 0.5]

# Matrix multiplication (dot product).
arr8 = np.array([[1, 2], [3, 4]])
arr9 = np.array([[5, 6], [7, 8]])
result = np.dot(arr8, arr9)
print(f"Matrix multiplication (dot product) =\n {result}")

# Element-wise comparison
arr10 = np.array([1, 2, 3, 4])
print('Element-wise comparison = ', arr10 > 2)  # Output: [False False  True  True]


# ---- Array shape and Reshape() ---

# In NumPy, the shape of an array refers to its dimensions, i.e., the number of elements along each axis (or axis lengths). 
# 1D array (vector)
arr1 = np.array([1, 2, 3, 4])
print(arr1.shape)  # Output: (4,) -- 1D array with 4 elements

# 2D array (matrix)
arr2 = np.array([[1, 2], [3, 4], [5, 6]])
print(arr2.shape)  # Output: (3, 2) -- 3 rows and 2 columns

# The reshape operation allows you to change the shape of an existing array without modifying its data
# numpy_array.reshape(new_shape)
# Create a 1D array with 6 elements
arr1 = np.array([1, 2, 3, 4, 5, 6])

# Reshape into a 2D array (2 rows, 3 columns)
arr2 = arr1.reshape(2, 3)
print(arr2)

# You can specify -1 in one of the dimensions of the shape, and NumPy will automatically calculate the correct dimension based on the other specified dimensions
arr = np.array([1, 2, 3, 4, 5, 6])

arr_reshaped = arr.reshape(-1, 3)
print(arr_reshaped)


# ------------- Statistical and Mathematical Operations --------------
# NumPy provides a variety of statistical and mathematical functions that can be applied to arrays.
arr = np.array([1, 2, 3, 4, 5])
print(np.sum(arr))  # Output: 15
print(np.mean(arr)) # Output: 3.0
print(np.min(arr))  # Output: 1
print(np.max(arr))  # Output: 5

# ----------- Broadcasting --------
# Broadcasting allows NumPy to perform operations on arrays of different shapes. It’s a way of automatically expanding the smaller array to match the shape of the larger array.
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([[6],[7],[8]])

result = arr1+arr2
print(result)

# ---------------- Linear Algebra --------------
# NumPy provides tools for linear algebra operations, like matrix multiplication, eigenvalues, etc.
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(np.matmul(A, B))

# Random Module
# NumPy also provides a random number generation module for tasks like simulations.
arr = np.random.rand(3, 3)  # Generate random numbers between 0 and 1
print(arr)



# View and Copy in NumPy
"""
In NumPy, view and copy refer to different ways that arrays can be handled when they are modified. Understanding the 
distinction is important because it can affect the behavior of your code, especially in terms of memory usage and 
performance.
"""

# 1. View in NumPy
"""
A view of a NumPy array is essentially another array that looks at the same data in memory as the original array. 
When you create a view, changes made to the view affect the original array and vice versa, because both the view and 
the original array share the same underlying data.
"""
# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Create a view of the original array
arr_view = arr[1:4]

print("Original Array:", arr)
print("View Array:", arr_view)

# Modify the view
arr_view[0] = 99

print("\nAfter modifying the view:")
print("Original Array:", arr)  # Notice that arr is also changed
print("View Array:", arr_view )

# 2. Copy in NumPy
"""
Creates a new array with its own independent copy of the data. Changes to the copy do not affect the original array, and changes to the original array do not 
affect the copy.
"""
# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Create a copy of the array
arr_copy = arr.copy()

print("Original Array:", arr)
print("Copy Array:", arr_copy)

# Modify the copy
arr_copy[0] = 99

print("\nAfter modifying the copy:")
print("Original Array:", arr)  # Notice that arr is not changed
print("Copy Array:", arr_copy)

"""
Memory Sharing:
View: Shares memory with the original array.
Copy: Creates a new independent copy in memory.

Modification Effects:
View: Modifications to the view affect the original array and vice versa.
Copy: Modifications to the copy do not affect the original array, and modifications to the original do not affect the copy.

Efficiency:
View: More memory efficient because it doesn’t create a new array; just gives a different perspective on the original array.
Copy: Less memory efficient because it duplicates the data in memory.
"""

# DataType Specify
"""
In NumPy, you can explicitly specify the data type (dtype) of an array when you create it. This is useful when you need to 
ensure that the array is created with a specific data type, which can help save memory or ensure compatibility with other 
computations or external libraries.

arr = np.array(data, dtype=desired_dtype)

data: The data to create the array (e.g., a list or another array).
dtype: The desired data type. You can use NumPy’s dtype objects or a Python type (like int, float, etc.).

# Here are some common NumPy data types (dtype):
int8, int16, int32, int64: Signed integers of 8, 16, 32, and 64 bits respectively.
uint8, uint16, uint32, uint64: Unsigned integers of 8, 16, 32, and 64 bits respectively.
float16, float32, float64: Floating-point numbers with 16, 32, and 64 bits respectively.
complex64, complex128: Complex numbers with 64 or 128 bits.
bool: Boolean type (True or False).
object: Generic Python object type.
str: String type.
"""
# Create an array of strings
arr_str = np.array(['apple', 'banana', 'cherry'], dtype=np.str_)

print("Array:", arr_str)
print("Data Type:", arr_str.dtype)  # Output: <U6 (Unicode string of max length 6)

# ------ Changing the Data Type After Creation -------
# You can also change the type of an existing array using the 'astype()' method:

# Change dtype of existing array
arr_float = np.array([1.1, 2.2, 3.3])
arr_int = arr_float.astype(np.int32)

print("Original Array:", arr_float)
print("Converted Array:", arr_int)


