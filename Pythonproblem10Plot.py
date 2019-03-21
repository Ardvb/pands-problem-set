# Ard van Balkom
# This program will display a plot of the functions x, x*x and 2**x, in the range[0,4]



import matplotlib.pyplot as plt # Import matplotlib
import numpy as np # Import Numpy for maths and working with arrays

x = np.linspace(0,4,5) # Set the min(0) and max(4) values for the x axis, and the number(5) of equally spaced samples.
# Connect the points for x = 0, x = 1, x = 2, x = 3 and x = 4.

y1 = x # These are the 3 functions that will be plotted.
y2 = x**2
y3 = 2**x

plt.plot(y1, label="x") # Plot y1 and label it "x"
plt.plot(y2, label="x square") # Plot y2 and label it "x square"
plt.plot(y3, label="2**x") # Plot y2 and label it "2**x"
    
plt.xlabel("X") # Label the X-axis "X"
plt.ylabel("Y") # Label the Y-axis "Y"
    
plt.title("Functions of x in range [0,4]") # Give the plot a title

plt.legend() # Show the labels above the plot, so it is clear what each of the coloured lines represent.

plt.show() # Show the plot
