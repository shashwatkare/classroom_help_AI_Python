# Intro to Pandas
# what is pandas?
# pandas is a python library for data analysis and manipulation.
# Pandas provides two additional data structures to python, namely series and dataframe.
# these two data structures helps us to work on labeled and relational data.

# If you are using anaconda, you can install pandas using the following command:
# conda install pandas
# # or
# pip install pandas

### Why use Pandas?
# To achieve most efficient results in AI & ML space we need to work on large datasets,
# but it is just not about quantity but also about quality of data.
# pandas helps us to work on large datasets and also helps us to clean and prepare the data for further analysis.
# and for every training algorithm the data needs to be in a particular format, clear of any outliers.
# pandas helps us to achieve that.
# Allows the use of labels for rows and columns
# Can calculate rolling statistics on time series data
# Easy handling of NaN values
# Is able to load data of different formats into DataFrames
# Can join and merge different datasets together
# It integrates with NumPy and Matplotlib

# Creating pandas series

# what is pandas series?
# pandas series is a one-dimensional labeled array capable of holding data of any type
# (integer, string, float, python objects, etc.). The axis labels are collectively called index.
# Pandas series can be created using various inputs like −
# Array
# dict
# scalar value or constant

# difference between numpy array and pandas series
# what is the difference between numpy array and pandas series?
# In pandas series, the index is not just an integer but can be any value like string, integer, float, etc.
# numpy array is a collection of items of the same type and pandas series is a collection of items of different types.


import pandas as pd
import numpy as np

# # create a pandas series using a python list
# series = pd.Series([1, 2, 3, 4, 5])
# print(series)
#
# # create a pandas series using a numpy array
# series = pd.Series(np.array([1, 2, 3, 4, 5]))
# print(series)
#
# # create a pandas series using a python dictionary
# series = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
# print(series)
#
# # create a pandas series using a python list and specify the index
# series = pd.Series([1, 2, 3, 4, 5], index=['apple', 'banana', 'carrot', 'dates', 'egg'])
# print(series)
#
# # create a pandas series using a numpy array and specify the index
# series = pd.Series(np.array([1, 2, 3, 4, 5]), index=['apple', 'banana', 'carrot', 'dates', 'egg'])
# print(series)

# numpy array is a multi-dimensional array and pandas series is a one-dimensional array

# using attributes like shape, ndim, size, values, index
# # use pandas series attributes like shape, ndim, size, values, index
# create a pandas series using a python list and index and print the attributes
# series = pd.Series([1, 2, 3, 4, 5], index=['apple', 'banana', 'carrot', 'dates', 'egg'])
# print(series.shape)
# print(series.ndim)
# print(series.size)
# print(series.values)
# print(series.index)

# # shape
# print(series.shape)
# # ndim
# print(series.ndim)
# # size
# print(series.size)
# # values
# print(series.values)
# # index
# print(series.index)


# access elements in a pandas series
# # access elements in a pandas series
# create a pandas series using a python list and index and print the attributes
# series = pd.Series([1, 2, 3, 4, 5], index=['apple', 'banana', 'carrot', 'dates', 'egg'])
# print(series[0])
# print(series['apple'])
#
# # mutate elements in a pandas series
# # # mutate elements in a pandas series
# # create a pandas series using a python list and index and print the attributes
# series = pd.Series([1, 2, 3, 4, 5], index=['apple', 'banana', 'carrot', 'dates', 'egg'])
# series[0] = 10
# print(series)
# series['apple'] = 20
# print(series)
#
# # access elements using index
#
# # change elements using index
#
# # delete elements from a list of pandas series
# # # delete elements from a list of pandas series
# # create a pandas series using a python list and index and print the attributes
# series = pd.Series([1, 2, 3, 4, 5], index=['apple', 'banana', 'carrot', 'dates', 'egg'])
# print(series)
# del series['apple']
# print(series)
#
#
# # Arithmetic operations in pandas series
# # # Arithmetic operations in pandas series
# # create a pandas series using a python list and index and print the attributes
# # fruits= pd.Series(data = [10, 6, 3,], index = ['apples', 'oranges', 'bananas'])
# series1 = pd.Series([1, 2, 3, 4, 5], index=['apple', 'banana', 'carrot', 'dates', 'egg'])
# series2 = pd.Series([1, 2, 3, 4, 5], index=['apple', 'banana', 'carrot', 'dates', 'egg'])
# print(series1 + series2)
# print(series1 - series2)
# print(series1 * series2)
# print(series1 / series2)
#
#
# # basic arithmetic operations
#
# # Arithmetic operations on pandas series using numpy functions
# # # Arithmetic operations on pandas series using numpy functions
# # create a pandas series using a python list and index and print the attributes
# series1 = pd.Series([1, 2, 3, 4, 5], index=['apple', 'banana', 'carrot', 'dates', 'egg'])
# series2 = pd.Series([1, 2, 3, 4, 5], index=['apple', 'banana', 'carrot', 'dates', 'egg'])
# print(np.add(series1, series2))
# print(np.subtract(series1, series2))
# print(np.multiply(series1, series2))
# print(np.divide(series1, series2))

# Perform arithmetic operations on selected elements


# selective arithmetic operation

# creating pandas dataframe

# manually creating pandas dataframe

# creating pandas dataframe using dictionary
# create a dictionary of Pandas Series without indexes
dict = {'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
        'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
        'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8])}
# create a dataframe
df = pd.DataFrame(dict)
# print the output.
print(df)

# creating pandas dataframe using list
# create a list of Pandas Series
list = [pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
        pd.Series([25, 26, 25, 23, 30, 29, 23]),
        pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8])]
# create a dataframe
df = pd.DataFrame(list)
# print the output.
print(df)

# creating pandas dataframe using numpy array
# create a numpy array of Pandas Series
array = np.array([pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
                  pd.Series([25, 26, 25, 23, 30, 29, 23]),
                  pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8])])
# create a dataframe
df = pd.DataFrame(array)
# print the output.
print(df)

# creating pandas dataframe using list of dictionaries
# create a list of dictionaries
list = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
# create a dataframe
df = pd.DataFrame(list)
# print the output.
print(df)

# creating pandas dataframe using dictionary of dictionaries
# create a dictionary of dictionaries
dict = {'one': {'a': 1, 'b': 2, 'c': 3},
        'two': {'a': 5, 'b': 10, 'c': 20}}
#


# attributes of pandas dataframe

# get rows from a dataframe

# get columns from a dataframe

# create dataframe from csv file

# create datframe from dict of lists

# create dataframe from list of dicts

# select specific row from a dataframe


# access elements in a pandas dataframe
# # access elements in a pandas dataframe
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35},
          {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants': 5}]

store_items = pd.DataFrame(items2, index=['store 1', 'store 2'])

print(store_items, '\n')

print('How many bikes are in each store:\n', store_items[['bikes']])
#


# adding column to dataframe - df.insert(loc, column, value, allow_duplicates=False)

# df.pop(column_name) - remove column from dataframe

# deleting column from dataframe - df.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')

# adding row to dataframe - df.append(other, ignore_index=False, verify_integrity=False, sort=None)

# df.pop(row_name) - remove row from dataframe

# deleting row from dataframe - df.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')

# renaming column label
# df.rename(columns={'old_name': 'new_name'}, inplace=True)

# renaming row label
# df.rename(index={'old_name': 'new_name'}, inplace=True)


# dealing with NaN or missing data
# create dataframe with NaN
# pip install -U pandas
# import pandas as pd
#
# # 7 columns and 3 rows
# items2 = [{'bikes': 20, 'pants': 30, 'watches': 35, 'shirts': 15, 'shoes': 8, 'suits': 45},
#           {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants': 5, 'shirts': 2, 'shoes': 5, 'suits': 7},
#           {'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4, 'shoes': 10}]
#
# store_items = pd.DataFrame(items2, index=['store 1', 'store 2', 'store 3'])
#
# print(store_items)
