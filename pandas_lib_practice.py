# ********************        pandas library practice   **********************

# Pandas provides high-performance, easy-to-use data structures and tools for working with 
# structured data, such as tabular data (e.g., spreadsheets, SQL tables) and time series data.

# The two primary data structures of pandas: 
#   --  Series (1-dimensional),  (capable of holding any data type eg. integers, strings, floats, Python objects, etc.)
#   --  DataFrame (2-dimensional) (a 2-d labeled data structure with columns of potentially different types)

# a dataframe is similar to a table in a relational database or an excel spreadsheet,

# 3rd Data Structure: Panel (3-dimensional) (a 3-d labeled data structure) (Deprecated) (replaced by MultiIndex DataFrames)



# First lets practice the core data sctructures in Pandas library

# 1. Series: 

# A Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floats, etc.). 
# It is similar to a column in a spreadsheet or a SQL table, or a single column in a DataFrame.

import pandas as pd

# Creating a Series by passing a list of values, letting pandas create a default integer index:

data = [1,2,3,4,5,6,7,8]
s = pd.Series(data)
#s = pd.Series([1, 3, 5, 7, 9])
print(s)   # printitng the series s. 


# Creating a Series by passing a list of values, and a list of index labels:

data1 = []   # creating an empty list

# using for loop to append the values in the list
for i in range(10):
    data1.append(i)

s1 = pd.Series(data1)

print(s1)  # printing the series s1


# Creating a Series by passing a custom index labels:

data2 = [10,20,30,40,50]

s3 = pd.Series(data2, index=['a', 'b', 'c', 'd', 'e'])

print(s3)  # printing the series s3


# Creating a Series by passing a dictionary:

data3 = {'a' : 0.00, 'b' : 1.00, 'c' : 2.12}

s4 = pd.Series(data3)

print(s4)  # printing the series s4

# Accessing the elements of the series using the index labels:

print(s4['a'])  # accessing the element of the series s4 using the index label 'a'




# 2. DataFrame:

# A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.

data = { 'Name' : ['Ajeet','Alice', 'Bob', 'Charlie'], 'Age': [35,25,30,35] , 'City' : ['Tucson','NYC','LA','SF'] }
df = pd.DataFrame(data)

print(df)

# To hide index value from table

print(df.to_string(index=False))


# print details about dataframe df
print(df.info())

