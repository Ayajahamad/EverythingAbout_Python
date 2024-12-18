import pandas as pd

# """
# Correlation measures the relationship between two variables — how one changes in relation to the other.
# A positive correlation means both variables move in the same direction, and a negative correlation means they move in opposite directions.
# Pearson's correlation coefficient measures linear relationships.
# Spearman's and Kendall's coefficients measure monotonic (non-linear) relationships.

# Finding Relationships :
# A great aspect of the Pandas module is the corr() method.

# The corr() method calculates the relationship between each column in your data set
# """

df = pd.read_csv('https://www.w3schools.com/python/pandas/data.csv.txt')
print(df)


Correlation = df.corr()
print(Correlation)


"""
Plotting:
Pandas uses the plot() method to create diagrams.

We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.
"""
# Import pyplot from Matplotlib and visualize our DataFrame:
import matplotlib.pyplot as plt

df.plot()

plt.show()


"""
Scatter Plot:

Specify that you want a scatter plot with the kind argument:
kind = 'scatter'

A scatter plot needs an x- and a y-axis.

In the example below we will use "Duration" for the x-axis and "Calories" for the y-axis.

Include the x and y arguments like this:

x = 'Duration', y = 'Calories'
"""

df.plot(kind='scatter', x='Duration' , y='Pulse')
plt.show()


"""
Histogram:

Use the kind argument to specify that you want a histogram:

kind = 'hist'

A histogram needs only one column.

A histogram shows us the frequency of each interval, e.g. how many workouts lasted between 50 and 60 minutes?
"""

# df.plot(kind='hist',x='Duration' , y='Pulse')
# plt.show()

df["Duration"].plot(kind = 'hist')
plt.show()
