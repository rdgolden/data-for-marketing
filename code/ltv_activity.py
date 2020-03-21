import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats as st

data = pd.read_csv('./data.csv')

x = data['Lifetime Value']
y = data['Age']

def func(x, a, b):
    return a * x + b

popt, pcov = curve_fit(func, x, y)

plt.clf()

plt.scatter(x, y, label="Original Data")
plt.plot(x, func(x, *popt), 'r-', label="Linear Regression")

# Setting the Title, X- and Y-axis labels
plt.title("Age Vs. LTV")
plt.ylabel("Age")
plt.xlabel("Lifetime Value")

# Setting the labeling parameters for the X-axis
plt.xticks(rotation="vertical")

# Showing  grid lines
plt.grid(True)

# Showing the legend
plt.legend()

# Print the resulting bar graph
plt.show()