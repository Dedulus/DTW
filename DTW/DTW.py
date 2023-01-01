# Usage:  Using DTW (Dynamic Time Warping algorithm) to match elevation data from Barometer and GPS

# Version: 1.0, Date: 25 December 2022

# Owner: Arnab Mitra

# Contact: papan.mitra.2121@gmail.com


import numpy as np
import matplotlib.pyplot as plt
import fastdtw

# Barometer to Elevation data
barometer_data = np.array([20.50,20.53,20.56,20.60,20.65,20.70,20.73,20.75,20.78,20.80])

# GPS Map Elevation data
gps_data = np.array([20.45,20.50,20.55,20.62,20.68,20.72,20.75,20.78,20.83,20.87])

# Calculate DTW Distance
distance, path = fastdtw.fastdtw(barometer_data, gps_data, dist=lambda x, y: abs(x - y))
print('DTW Distance : %f' % distance)

# Plot the graph
plt.plot(barometer_data, label='Barometer')
plt.plot(gps_data, label='GPS Map')
plt.title('Dynamic Time Warp')
plt.xlabel('Time')
plt.ylabel('Elevation')
plt.legend()
plt.show()
