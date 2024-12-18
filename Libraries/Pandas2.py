import pandas as pd

# """
# Data Cleaning:
# Data cleaning means fixing bad data in your data set.

# Bad data could be:
# - Empty cells
# - Data in wrong format
# - Wrong data
# - Duplicates
# """

# data_dict = {
#     "Duration": [60, 60, 60, 45, 45, 60, 60, 450, 30, 60, 60, 60, 60, 60, 60, 60, 60, 60, 45, 60, 45, 60, 45, 60, 60, 60, 60, 60, 60, 60, 60, 50],
#     "Date": [
#         '2020/12/01', '2020/12/02', '2020/12/03', '2020/12/04', '2020/12/05', '2020/12/06', 
#         '2020/12/07', '2020/12/08', '2020/12/09', '2020/12/10', '2020/12/11', '2020/12/12', 
#         '2020/12/12', '2020/12/13', None, '2020/12/15', 2020/12/16, '2020/12/17', 
#         '2020/12/18', '2020/12/19', '2020/12/20', '2020/12/21', '2020/12/22', '2020/12/23', 
#         '2020/12/24', '2020/12/25', '2020/12/27', '2020/12/28', '2020/12/29', '2020/12/31',
#         '2020/12/30', '2020/12/31'
#     ],
#     "Pulse": [110, 117, 103, 109, 117, 102, 110, 104, 109, 98, 103, 100, 102, 100, 106, 104, 98, 98, 100, 90, 103, 97, 108, 100, 130, 105, 102, 100, 92, 103, 100, 102],
#     "Maxpulse": [130, 145, 135, 175, 148, 127, 136, 134, 133, 124, 147, 150, 120, 120, 128, 132, 123, 120, 120, 112, 123, 125, 131, 119, 101, 132, 126, 120, 118, 132, 132, 129],
#     "Calories": [409.1, 479.0, 340.0, 406.0, 300.0, 374.0, 253.3, 195.1, 269.0, 329.3, 323.9, 250.7, 250.7, 345.3, 379.3, 275.0, 215.2, 300.0, None, 323.0, 243.0, 364.2, 282.0, 300.0, 246.0, 334.5, 250.0, 241.0, None, 280.0, 380.3, 243.0]
# }

# """Length should be same for All lists"""
# # print(len(data_dict))
# # print(len(data_dict['Duration']))
# # print(len(data_dict['Pulse']))
# # print(len(data_dict['Maxpulse']))
# # print(len(data_dict['Date']))
# # print(len(data_dict['Calories']))

# df = pd.DataFrame(data_dict)
# print(df)

# """
# Empty Cells:
# Empty cells can potentially give you a wrong result when you analyze data.

# One way to deal with empty cells is to remove rows that contain empty cells.
# """

# # By default, the dropna() method returns a new DataFrame, and will not change the original
# new_df = df.dropna()
# print(new_df)

# # # If you want to change the original DataFrame, use the inplace = True argument:
# # new_df = df.dropna(inplace=True)

# """
# Replace Empty Values:
# Another way of dealing with empty cells is to insert a new value instead.

# This way you do not have to delete entire rows just because of some empty cells.

# The fillna() method allows us to replace empty cells with a value:
# """
# # # Replace NULL values with the number 130
# # df.fillna(130, inplace = True)
# # print(df)

# """
# Replace Only For Specified Columns:
# The example above replaces all empty cells in the whole Data Frame.

# To only replace empty values for one column, specify the column name for the DataFrame
# """
# df["Calories"].fillna(130, inplace = True)
# print(df)


# """
# Replace Using Mean, Median, or Mode:
# A common way to replace empty cells, is to calculate the mean, median or mode value of the column.

# Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:
# """
# # Mean = the average value (the sum of all values divided by number of values).
# x = df["Calories"].mean()
# # df["Calories"].fillna(x, inplace = True)

# # Median = the value in the middle, after you have sorted all values ascending.
# x = df["Calories"].median()
# # df["Calories"].fillna(x, inplace = True)

# # Mode = the value that appears most frequently.
# x = df["Calories"].mode()[0]
# print(x)

# df_csv = pd.read_csv('C:\\Users\\ayaj\\Downloads\\data.csv')
# print(df_csv)

"""
Let's try to convert all cells in the 'Date' column into dates.
Pandas has a to_datetime() method for this:
"""
df_csv = pd.read_csv('C:\\Users\\ayaj\\Downloads\\data.csv')
print(df_csv)

print(df_csv['Date'])

# df_csv['Date'] = pd.to_datetime(df_csv['Date'])
print(df_csv.to_string())

df_csv['Date'] = pd.to_datetime(df_csv['Date'], errors='coerce')
# print(pd.Series(df_csv['Date']))

# Remove rows with a NULL value in the "Date" column:
df_csv.dropna(subset=['Date'], inplace = True)
print(pd.Series(df_csv['Date']))

"""
One way to fix wrong values is to replace them with something else.
In our example, it is most likely a typo, and the value should be "45" instead of "450", and we could just insert "45" in row 7
"""
# 7th index details
d = df_csv.loc[7]
print(d)

df_csv.loc[7, 'Duration'] = 45
print(pd.Series(df_csv['Duration']))

"""
To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that 
are outside of the boundaries.

like use loops ad set a target condition and change.
or for remove :

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)
"""

# Duplicates
"""
Discovering Duplicates:
Duplicate rows are rows that have been registered more than one time.

To discover duplicates, we can use the duplicated() method.
The duplicated() method returns a Boolean values for each row
"""

print(df_csv.duplicated())

"""
Removing Duplicates
To remove duplicates, use the drop_duplicates() method.
"""
df_csv.drop_duplicates(inplace = True)