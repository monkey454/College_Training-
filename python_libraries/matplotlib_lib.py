# Matplotlib - library in python for data visualization
# Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy.
# It provides an object-oriented API for embedding plots into applications that use general-purpose GUI toolkits,
# such as Tkinter, wxPython, Qt, or GTK.
# Matplotlib is widely used for data visualization in Python, allowing users to create static, animated, and interactive visualizations.   
# Application of Matplotlib in Python:
# data visualization, plotting graphs, creating charts, and visualizing data distributions.
# Example of Matplotlib usage in Python:
# Basic Plotting

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Line 1')
plt.title('Basic Plotting Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()    
plt.grid(True)
plt.show()
# Bar Chart
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 2, 5]
plt.bar(categories, values, color='g', label='Bar Chart')
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.legend()
plt.show()
# Histogram
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
plt.hist(data, bins=5, color='r', alpha=0.7, label='Histogram')
plt.title('Histogram Example')
plt.xlabel('Data Values')
plt.ylabel('Frequency')
plt.legend()
plt.show()
# Scatter Plot
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
sizes = [20, 50, 80, 100, 200]
plt.scatter(x, y, s=sizes, color='purple', alpha=0.5, label='Scatter Plot')
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')    
plt.legend()    
plt.grid(True)
plt.show()
# Pie Chart
labels = ['Category A', 'Category B', 'Category C', 'Category D']   
sizes = [15, 30, 45, 10]
colors = ['gold', 'lightcoral', 'lightskyblue', 'yellowgreen']
explode = (0.1, 0, 0, 0)  # explode the 1st slice
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Pie Chart Example')
plt.show()
# 3D Plotting
from mpl_toolkits.mplot3d import Axes3D
import numpy as np  
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)
ax.scatter(x, y, z, c='r', marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title('3D Scatter Plot Example')
plt.show()
# Customizing Plots
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Line 1')
plt.title('Customized Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # Rotate x-axis labels
plt.yticks(np.arange(0, 12, step=1))  # Set y-axis ticks
plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels
plt.show()
# Saving Plots
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Line 1')
plt.title('Save Plot Example')
plt.xlabel('X-axis')    
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.savefig('save_plot_example.png')  # Save the plot as a PNG file 

# data
x = [(i-5) for i in range(20,60)]
y = [(i+5) for i in range(20,60)]
plt.plot(x,y)

# customize the plot
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.scatter(x, y, color='red', label='Data Points')
plt.title('Scattered Line Plot')

# display the plot
plt.show()