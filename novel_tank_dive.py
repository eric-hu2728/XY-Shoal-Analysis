# Fish height during the novel tank dive can be an indicator of anxiety.
# Users can obtain a framewise list of Y coordinates from their preferred open-source tracking software.
# Import required libraries.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy import genfromtxt
import PIL
import os

# Enter the file path and name for the Y coordinate data.
# Note: Ensure that your video footage was captured with an orientation in which the target axis represent height.

my_path = 'path_to_Y_coordinates/'
my_file = 'file.csv'

# Convert csv data into a list, then into a numpy array.

y_vals = genfromtxt(my_path+my_file, delimiter=',')
y_array=np.array(y_vals)

# Remove NaN values

y_result = y_array[np.logical_not(np.isnan(y_array))]

# Determine min and max Y values to identify range
# We assume that the fish swam to both the bottom and top of the tank at least once during the tracking period.
# Fish that fail to swim to both the bottom and top of the tank should be excluded.

y_min = np.min(y_result)
y_max = np.max(y_result)

# Subtract max-min to get range. 
# Smaller values are higher up. Image coordinates originate at top left corner.
# Specifically, the variable "y_max" represents the bottom of the tank, and vice versa.

y_range = y_max-y_min

# Multiply y_range by .33333 to determine 1/3 length of y_range.
# Our novel tank dive considered three zones (bottom, middle, and top). Other protocols only consider two zones.

zone_size = y_range * .33333

# Define the lower boundary height of the top zone.

top_zone = y_min + zone_size

# Define minute intervals. Video was recorded at 60 fps. Therefore, one minute is 3600 frames.
# If user video was captured at a different frame rate, adjust these intervals accordingly.
# Note: When tracking, it is helpful to ensure that tracking time corresponds to actual test start time as closely as possible.
# Note: Any acclimation period is assumed to have taken place before frame zero. Adjust your protocol accordingly.

min1 = y_result[0:3600]
min2 = y_result[3601:7200]
min3 = y_result[7201:10800]
min4 = y_result[10801:14400]
min5 = y_result[14401:18000]

# Plot the framewise change in swim depth for each test minute.
# Using this plot, the number of top zone entries can be manually counted.
# Plot details can be adjusted

plt.gca().invert_yaxis()
plt.plot(min1, color='magenta', linewidth='1',mfc='pink' ) # Adjust color and line width
plt.xticks(range(0,len(min1)+1, 60))
plt.ylabel('Y position') # Set label for Y axis
plt.xlabel('time (120 frames per point)') # Set label for X axis
plt.axhline(y=top_zone)
plt.title("minute1") # Set title of plot
plt.savefig(my_path+'Minute_1.tif') #Save plot to same folder as original data.
plt.show() # This line can be commented out or deleted if user does not desire immediate viewing.

# Repeat for minutes 2 through 5

plt.plot(min2, color='magenta', linewidth='1',mfc='pink' )
plt.xticks(range(0,len(min2)+1, 60))
plt.ylabel('Y position') #set the label for y axis
plt.xlabel('time (120 frames per point)') #set the label for x-axis
plt.axhline(y=top_zone)
plt.title("minute2") #set the title of the graph
plt.savefig(my_path+'Minute_2.tif')
plt.show()

plt.plot(min3, color='magenta', linewidth='1',mfc='pink' )
plt.xticks(range(0,len(min3)+1, 60))
plt.ylabel('Y position') #set the label for y axis
plt.xlabel('time (120 frames per point)') #set the label for x-axis
plt.axhline(y=top_zone)
plt.title("minute3") #set the title of the graph
plt.savefig(my_path+'Minute_3.tif')
plt.show()

plt.plot(min4, color='magenta', linewidth='1',mfc='pink' )
plt.xticks(range(0,len(min4)+1, 60))
plt.ylabel('Y position') #set the label for y axis
plt.xlabel('time (120 frames per point)') #set the label for x-axis
plt.axhline(y=top_zone)
plt.title("minute4") #set the title of the graph
plt.savefig(my_path+'Minute_4.tif')
plt.show()

plt.plot(min5, color='magenta', linewidth='1',mfc='pink' )
plt.xticks(range(0,len(min5)+1, 60))
plt.ylabel('Y position') #set the label for y axis
plt.xlabel('time (120 frames per point)') #set the label for x-axis
plt.axhline(y=top_zone)
plt.title("minute5") #set the title of the graph
plt.savefig(my_path+'Minute_5.tif')
plt.show()

# Determine minute-wise time in top zone
# Identify the frames during which the fish was within the top zone.

min1_top = min1[min1<top_zone]
min2_top = min2[min2<top_zone]
min3_top = min3[min3<top_zone]
min4_top = min4[min4<top_zone]
min5_top = min5[min5<top_zone]

# Count the number of top zone frames.

min1_size = np.size(min1_top)
min2_size = np.size(min2_top)
min3_size = np.size(min3_top)
min4_size = np.size(min4_top)
min5_size = np.size(min5_top)

# Divide each minute by 60 (fps) to determine top zone time in seconds.

min1_time = min1_size/60
min2_time = min2_size/60
min3_time = min3_size/60
min4_time = min4_size/60
min5_time = min5_size/60

# Save these values to a csv.

results_header=('Min_1','Min_2','Min_3','Min_4','Min_5')
results=(min1_time, min2_time, min3_time, min4_time, min5_time)
dict= {'Test_Minute':results_header, 'Top_Zone_Time(sec)':results}
df = pd.DataFrame(dict)
df.to_csv(path+'top_zone_times.csv')
