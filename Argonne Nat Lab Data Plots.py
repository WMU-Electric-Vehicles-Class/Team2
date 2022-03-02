import numpy as np
from matplotlib import pyplot as plt

ftp = np.loadtxt('TestData.txt', dtype=int)


'''time_s = ftp[:,0]
SOC_Percent = ftp[:,9]
#plt.plot(time_s,np.percentile)
plt.plot(time_s,SOC_Percent)
plt.xlabel("Time (sec)")
plt.ylabel("SOC (%)")
plt.show()'''