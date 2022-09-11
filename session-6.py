# # create a numpy array using python list
import numpy as np

# ------------------------------
# one_d = np.array([1, 2, 3, 4, 5])  # Note: np.array is a function and not a class
# print(one_d)
# # here a is a 1D array or one dimensional array
# # this is also called as rank 1 array and you can get the rank of an array using the ndim attribute
# print(one_d.ndim)
# #
# # here a is a 2D array or two dimensional array
# two_d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(two_d)
# print(two_d.ndim)
# #
# # here a is a 3D array or three dimensional array
# three_d = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]])
# print(three_d)
# print(three_d.ndim)
#
# np.shape() returns returns a tuple with each index having the number of corresponding elements.
# shape_arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(shape_arr.shape)  # the output is (2, 5) which means 2 rows and 5 columns
# # or if you read it the first list contains 2 elements and the second list contains 5 elements
# #
# # np.dtype() returns the data type of the array
# print(shape_arr.dtype)  # output is int64 which is a 64 bit integer
#
# ndarray of strings
str_arr = np.array(['a', 'b', 'c', 'd', 'e'])
# print(str_arr)
# print(str_arr.shape)  # output is (5,) which means 5 elements in a single list as this is a 1D array
# print(str_arr.dtype)  # output is <U1 which means unicode string of length 1
#
# mixed data type array
# mixed_arr = np.array([1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e'])
# print(mixed_arr)
# print(mixed_arr.shape)  # output is (10,) which means 10 elements in a single list as this is a 1D array
# print(mixed_arr.dtype)  # output is <U21 which means unicode string of length 21
# print(type(mixed_arr))  # output is <class 'numpy.ndarray'>
#
# # type casting in numpy array
# type_arr = np.array([1.5, 2.4, 3.87, 4.23, 5.65], dtype=np.float32)
# print(type_arr)
# print(type_arr.dtype)  # output is float64 which is a 64 bit float
#
# # saving and loading numpy array
# np.save('my_array', str_arr)  # save the array to a file with .npy extension
# load_arr = np.load('my_array.npy')  # load the array from the file
# print(load_arr)

# ---------------------------------------------------------------------------------------------
# # numpy array creation using built-in functions
#
# easy way to create a numpy array using np.zeros()
# zero_d = np.zeros(shape=(3, 4), dtype=float)  # shape is a tuple with the number of rows and columns
# print(zero_d)
# print(zero_d.ndim)
#
# easy way to create a numpy array using np.ones()
# one_d = np.ones(shape=(3, 4), dtype=int)  # shape is a tuple with the number of rows and columns
# print(one_d)
# print(one_d.ndim)
#
# easy way to create a numpy array using np.full()
# full_d = np.full(shape=(3, 4), fill_value=5, dtype=int)  # shape is a tuple with the number of rows and columns
# print(full_d)
# print(full_d.ndim)
#
# ---------------------------------------------------------------------------------------------
# # multiple other ways to create numpy array using
# # np.arange() - similar to range() function takes start, stop and step as arguments
# # np.linspace() Sometimes with np.arange() you can get unexpected results due to floating point precision.
# # thus we use np.linspace() which takes start, stop and number of elements as arguments
# # np.logspace(),
# # np.random.random(),
# # np.random.randint()
#
# --------------------------------------------------------------------------------------------- shaping & transposing
# np.reshape() - reshape an array note that this is a function and not an attribute or method
# reshape_arr = np.arange(1, 10)
# print(reshape_arr)
# print(reshape_arr.shape)
# #
# reshape_arr_func = np.reshape(reshape_arr, (3, 3))
# print(reshape_arr_func)
# print(reshape_arr_func.shape)
# #
# #
# reshape_arr = reshape_arr.reshape(3, 3)
# print(reshape_arr)
# print(reshape_arr.shape)
#
# # to understand the difference between function and method check following link
# # https://stackoverflow.com/questions/155609/whats-the-difference-between-a-method-and-a-function?rq=1
# arr = np.arange(1, 10)
# print(arr)
# # np.delete() - delete an element from an array
# arr = np.delete(arr, 0)
# print(arr)

# np.append() - append an element to an array
# arr = np.append(arr, 100)
# print(arr)
# #
# # np.insert() - insert an element to an array
# arr = np.insert(arr, 5, 100)
# print(arr)
#
# # np.concatenate() - concatenate two arrays
# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([6, 7, 8, 9, 10])
# arr = np.concatenate((arr1, arr2))
# print(arr)

# # np.copy() - copy an array
# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.copy(arr1)
# arr2 = np.append(arr2, 100)
# print(arr1)
# print(arr2)

# np.unique() - find unique elements in an array
# arr = np.array([[1, 2, 3], [5, 2, 8], [1, 2, 3]])
# print(arr.shape, arr.ndim)
# print(np.unique(arr))

# create a numpy array using np.random.randint()
# rand_arr = np.random.randint(low=1, high=10, size=(3, 3))
# print(rand_arr)
# print(rand_arr.shape)
# print(rand_arr.ndim)
#
# create a numpy array using np.random.normal()
# rand_arr = np.random.normal(loc=0.0, scale=1.0, size=(100, 100))
# print(rand_arr)
# print(rand_arr.shape)
# print(rand_arr.dtype)
# print(f"mean: {rand_arr.mean()}")  # mean
# print(f"median: {np.median(rand_arr)}")  # median
# print(f"standard deviation: {rand_arr.std()}")  # standard deviation
# print(f"variance: {rand_arr.var()}")  # variance
# print(f"min: {rand_arr.min()}")  # min
# print(f"max: {rand_arr.max()}")  # max
# print(f"sum: {rand_arr.sum()}")  # sum
# print(f"this has total {(rand_arr < 0).sum()} negative numbers")  # count of negative numbers
# print(f"this has total {(rand_arr > 0).sum()} positive numbers")  # count of positive numbers

# --------------------------------------------------------------------------------------------- dangers of numpy
# # few important note - you should not combine different shapes of arrays
# # for example
# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([1, 2, 3, 4, 5, 6])
# print(arr1 + arr2)  # this will throw an error

# # keep arrays of same data type
# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
# print(arr1 + arr2)  # this will not throw an error but the output will be float
#
# # numpy functions returns a view or a copy of the array. Altering the view will alter the original array

# --------------------------------------------------------------------------------------------- indexing & slicing
# numpy array indexing and slicing
# arr = np.arange(1, 10)
# print(arr)
# print(arr[0])  # indexing
# print(arr[0:3])  # slicing
# print(arr[0:3:2])  # slicing with step size 2
# print(arr[::-1])  # reverse the array using slicing with step size -1
# print(arr[::2])  # reverse the array with step size 2 using slicing
# print(arr[0:3:-1])  # reverse the array with step size -1 using slicing
#
# # numpy array indexing and slicing with 2D array
# from pprint import pprint
# arr = np.arange(1, 10).reshape(3, 3)
# print(arr)
# # pprint(arr[1, 2])  # indexing
# # pprint(arr[0:2, 0:2])  # slicing
# # print(arr[0:3, 0:3:2])  # slicing with step size 2
# print(arr[::-1, ::-1])  # reverse the array using slicing with step size -1
#
# modify the array using indexing
# arr[0] = 100
# print(arr)

#


# boolean indexing
# arr = np.arange(1, 10)
# print(arr)
# print(arr > 5)
# print(arr[arr > 5])
# print(arr[arr < 5])
# print(arr[arr == 5])
# print(arr[arr != 5])
# print(arr[(arr > 5) & (arr < 8)])
# print(arr[(arr > 5) | (arr < 8)])

# # set operations
# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([4, 5, 6, 7, 8])
# print(np.intersect1d(arr1, arr2))
# print(np.setdiff1d(arr1, arr2))
# print(np.union1d(arr1, arr2))
#
# sort an array
# arr = np.array([5, 2, 6, 8, 1, 9, 3, 4, 7])
# print(np.sort(arr))

# # sort a 2D array
# arr = np.array([[5, 2, 6], [8, 1, 9], [3, 4, 7]])
# print(np.sort(arr))
# #
# # # sort a 2D array by row
# arr = np.array([[5, 2, 6], [8, 1, 9], [3, 4, 7]])
# print(np.sort(arr, axis=0))

# --------------------------------------------------------------------------------------------- numpy mathemathical
# operations

# # arithmatic operations on numpy array
# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([6, 7, 8, 9, 10])
# print(arr1 + arr2)
# print(arr1 - arr2)
# print(arr1 * arr2)
# print(arr1 / arr2)
# print(arr1 // arr2)
# print(arr1 % arr2)
# print(arr1 ** arr2)
#
# # # arithemtic functions on numpy array
# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([6, 7, 8, 9, 10])
# print(np.add(arr1, arr2))
# print(np.subtract(arr1, arr2))
# print(np.multiply(arr1, arr2))
# print(np.divide(arr1, arr2))
# print(np.floor_divide(arr1, arr2))
# print(np.mod(arr1, arr2))
# print(np.power(arr1, arr2))

# numpy broadcasting
# arr1 = np.array([1, 2, 3, 4, 5])
# print(arr1.shape)
# arr2 = np.array([1.1, 2.0, 3.0, 4.0])
# print(arr1 + arr2)
# print(arr1 - arr2)
# print(arr1 * arr2)
# print(arr1 / arr2)
# print(arr1 // arr2)
# print(arr1 % arr2)
# print(arr1 ** arr2)


# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([1.0, 2.0, 3.0, 4.0])
# print(arr1 + arr2)
# print(arr1 - arr2)
# print(arr1 * arr2)
# print(arr1 / arr2)
# print(arr1 // arr2)
# print(arr1 % arr2)
# print(arr1 ** arr2)

# import numpy as np

a = np.array([[0.0, 0.0, 0.0], [10.0, 10.0, 10.0], [20.0, 20.0, 20.0], [30.0, 30.0, 30.0]])
print(a.shape, a.ndim)
b = np.array([1.0, 2.0, 3.0, 4.0])
print(b.shape, b.ndim)

print(a)
print(b)
print(a + b)
