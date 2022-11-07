import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton


# Reading the Excel file
var = pd.read_excel("2023SoftwareInternAssignment.xlsx")

# declaring  x and y arrays for data storage
x = list(var['ReferenceDate'])
y = []

# dailyReturn% + 1 stored in temporary array
temp = list(var['DailyReturn']/100+1)

# This function does our total Return Calculation
def product(ending,arr):
    result = 1
    for i in range(0, ending):
        result *= arr[i]
    return (result-1)*100

# We calculate total return for all of our data points
for i in range(1, len(temp)+1):
    y.append(product(i,temp))

# Creating and initializing the line graph
plt.figure(figsize=(10, 10))
plt.style.use('_mpl-gallery')
plt.plot(x, y, linewidth=1.0)
plt.ylabel('Total Return', fontweight="bold")
plt.xlabel('Date', fontweight="bold")
plt.title("S&P 500 Daily Return", fontweight="bold")
plt.show()