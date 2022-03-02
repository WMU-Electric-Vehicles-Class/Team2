import numpy as np
from matplotlib import pyplot as plt
ftp = np.loadtxt('TestData.txt', dtype=int)

# print(ftp[0,0])
# print(ftp[1,0])
# print(ftp[:,0])
# print(ftp[:,1])


time_s = ftp[:,0]
speed_mph = ftp[:,9]
plt.plot(time_s,speed_mph)
plt.xlabel("Time (sec)")
plt.ylabel("SOC (%)")
plt.show()

time_s = ftp[:,0]
speed_mph = ftp[:,4]
plt.plot(time_s,speed_mph)
plt.xlabel("Time (sec)")
plt.ylabel("Dyno Speed (mph)")
plt.show()

time_s = ftp[:,0]
speed_mph = ftp[:,5]
plt.plot(time_s,speed_mph)
plt.xlabel("Time (sec)")
plt.ylabel("Dyno Tractive Effort (N)")
plt.show()

time_s = ftp[:,0]
speed_mph = ftp[:,6]
plt.plot(time_s,speed_mph)
plt.xlabel("Time (sec)")
plt.ylabel("Current (A)")
plt.show()

time_s = ftp[:,0]
speed_mph = ftp[:,7]
plt.plot(time_s,speed_mph)
plt.xlabel("Time (sec)")
plt.ylabel("Battery Voltage (V)")
plt.show()