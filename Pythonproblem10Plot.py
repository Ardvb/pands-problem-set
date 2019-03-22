# Ard van Balkom, 13-3-19
# Problem 10. This program will display a plot of the functions x, x*x and 2**x, in the range[0,4]



import matplotlib.pyplot as plt # Import matplotlib so we can plot functions.
import numpy 

x = numpy.linspace(0,4,5) # Set the min(0) and max(4) values for the x axis, and the number(5) of equally spaced samples.
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

# I used the video from week 9 by Ian McLoughlin: https://web.microsoftstream.com/video/f0788c1c-c7bd-4347-98ac-477186938ed7
# I used https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/ to find the right way of displaying this particular plot, and how to add a legend.
# I used https://www.numpy.org/devdocs/reference/generated/numpy.linspace.html to learn about Numpy and how to use linspace.