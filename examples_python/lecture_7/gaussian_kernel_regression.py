import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

area, river_flow = np.loadtxt('area_flow.txt', dtype=float, delimiter=',', skiprows=1, unpack=True)

#########################
# Plot data
#########################
plt.figure()
plt.plot(area, river_flow, 'bo')
plt.xlabel('Area')
plt.ylabel('River Flow')
plt.xlim(0,120)
plt.ylim(0,3000)
plt.savefig('data_set.png')

#########################
# Try kernel regression
#########################
#
# Construct the Gaussian kernel function
# around each data point.

def gaussian_kernel(xj, xi, h):

	K = 1./(h*np.sqrt(2.*np.pi))*np.exp(-0.5*((xj-xi)/h)**2.0)
	return K

# Define linearly spaced series of data points which
# include observed data points and can be used to
# evaluate the Gaussian kernel
xj = np.array(range(5, 101, 1))

# Define the bandwidth
h = 10

# For each area data point, calculate the value of each kernel,
# the corresponding weights, and then the predicted river
# flow value.
river_flow_pred = []
for idx, query_point in enumerate(area):
	K = 1./(h*np.sqrt(2.*np.pi))*np.exp(-0.5*((area-query_point)/h)**2.0)
	weights = K/np.sum(K)
	print river_flow * weights
	print np.sum(river_flow * weights)
	print idx
	river_flow_pred.append(np.sum(river_flow * weights))

plt.figure()
plt.plot(area, river_flow, 'bo')
plt.plot(area, np.array(river_flow_pred), 'b-')
plt.xlabel('Area')
plt.ylabel('River Flow')
plt.xlim(0,120)
plt.ylim(0,3000)
plt.show()
#plt.savefig('data_set.png')
