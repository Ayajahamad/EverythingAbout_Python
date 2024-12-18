"""
Pandas is a Python library used for working with data sets.
It has functions for analyzing, cleaning, exploring, and manipulating data.
The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis"

Pandas allows us to analyze big data and make conclusions based on statistical theories.
Pandas can clean messy data sets, and make them readable and relevant.
Relevant data is very important in data science.
"""

# Installing pandas
   # pip install pandas

# Importing Pandas
import pandas as pd

# Check Version
print("Version : ",pd.__version__)

"""
What is a Series?
A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type.
"""
a = [1, 7, 2]

myvar = pd.Series(a)
print(myvar)

"""
Labels
If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc..

With the index argument, you can name your own labels.
"""
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)

# You can also use a key/value object, like a dictionary, when creating a Series.

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

"""
DataFrames
Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

Series is like a column, a DataFrame is the whole table.
"""

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)

"""
A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

Locate Row:
Pandas use the loc attribute to return one or more specified row(s)

Locate Named Indexes:
Use the named index in the loc attribute to return the specified row(s).
"""
#refer to the row index:
print(myvar.loc[1])


"""
Load Files Into a DataFrame:
If your data sets are stored in a file, Pandas can load them into a DataFrame.
"""
"""
Read CSV Files:
A simple way to store big data sets is to use CSV files (comma separated files).

CSV files contains plain text and is a well know format that can be read by everyone including Pandas.

In our examples we will be using a CSV file called 'data.csv'.
"""
# If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows

df = pd.read_csv('https://www.w3schools.com/python/pandas/data.csv.txt')
print(df)

# use to_string() to print the entire DataFrame.
print(df.to_string())

"""
max_rows:
The number of rows returned is defined in Pandas option settings.

You can check your system's maximum rows with the pd.options.display.max_rows statement.
"""
print("max_rows : ",pd.options.display.max_rows) 

"""
In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only 
the headers and the first and last 5 rows.

You can change the maximum rows number with the same statement.
"""
# Increase the maximum number of rows to display the entire DataFrame:

pd.options.display.max_rows = 9999
print(df) 
print("max_rows : ",pd.options.display.max_rows) 

"""
Read JSON:
Big data sets are often stored, or extracted as JSON.

JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.
"""

df = pd.read_json('https://www.w3schools.com/python/pandas/data.js')
print(df)

"""
JSON = Python Dictionary

JSON objects have the same format as Python dictionaries.

If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly:
Eg:
"""
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)
print(df)

"""
Viewing the Data:
One of the most used method for getting a quick overview of the DataFrame, is the head() method.

The head() method returns the headers and a specified number of rows, starting from the top.
"""
# if the number of rows is not specified, the head() method will return the top 5 rows.
print("The head(3) : ",df.head(3))

"""
There is also a tail() method for viewing the last rows of the DataFrame.
The tail() method returns the headers and a specified number of rows, starting from the bottom.
"""
print("The tail(3) : ",df.tail(3))

# -- The DataFrames object has a method called info(), that gives you more information about the data set.--
print("Information About Data : ",df.info())



