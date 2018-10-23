# Importing the important Libraries
import numpy as np
import pandas as pd  # for loading data into the notebook 
from matplotlib import pyplot as plt #for making line chart
# Importing the extracted Data Set
data = pd.read_csv("results.csv")
# function that calculates the MOVING AVERAGE (global)
def moving_avg(mA_range, data_input):
    output = data_input.rolling(window = mA_range, on = "temp_global").mean().dropna()
    return output

# Drawing the graph: Global Temperature
mA_value = 5 #global 9.556
chart_moving_avg = moving_avg(mA_value, data)
plt.plot(chart_moving_avg ['year'], chart_moving_avg ['temp_global'], label = 'Global')
plt.legend()
plt.xlabel ("Years")
plt.ylabel ("Temperature (°C)")
plt.title ("Global Average Temperature")
plt.show ()
data.tail(487)

# function that calculates the MOVING AVERAGE (local)
def moving_avg_local(mlocal_value, data_input):
    output = data_input.rolling(window = mlocal_value, on = "temp_city").mean().dropna()
    return output
# Drawing the graph: alexandria Temperature
mlocal_value =14 #local 13.256
chart_moving_avg_local = moving_avg_local(mlocal_value, data)
plt.plot(chart_moving_avg_local ['year'], chart_moving_avg_local ['temp_city'], label = 'Alexandria')
plt.legend()
plt.xlabel ("Years")
plt.ylabel ("Temperature (°C)")
plt.title ("Alexandria Average Temperature")
plt.show()
data.tail(10)




