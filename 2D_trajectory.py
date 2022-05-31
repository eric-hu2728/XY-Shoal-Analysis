# This function takes an aligned array of X and Y coordinates and charts a stepwise trajectory for the object.
# XY coordinates can be obtained from video files using open-source image tracking software such as idtracker.ai or DeepLabCut.
# Import required libraries

import matplotlib.pyplot as plt
import numpy as np
import os

# Enter the file path and name for the Y coordinate data.
my_path = 'path_to_your_xy_coordinate/'
my_file = 'file_name.csv'

# Assumes XY coordinates are organized in adjacent colums in the csv file.

from numpy import genfromtxt
x_vals = genfromtxt(my_path+my_file, delimiter=',')[0]
y_vals = genfromtxt(my_path+my_file, delimiter=',')[1]

# Convert coordinate lists into numpy arrays.

x_array=np.array(x_vals)
y_array=np.array(y_vals)

# Plot the data.

plt.gca().invert_yaxis()
plt.plot(x_array, y_array, linewidth=1)

# Set your plot parameters, particularly the X and Y units, as appropriate.
# Most open-source animal trackers will automatically output pixel coordinates.

plt.title('Fish Trajectory')
plt.ylabel('Y position (px)')
plt.xlabel('X position (px)')

# Save trajectory plot as a tif image file in the same folder as coordinate data.
plt.savefig(my_path+'XY_trajectory.tif')
