import numpy as np
from matplotlib import pyplot as plt


#The EPA Urban Dynamometer Driving Schedule (UDDS) is commonly called the "LA4" or "the city test" and represents city driving conditions. It is used for light duty vehicle testing. The UN/ECE Regulation 53 refers to the EPA UDDS as the "Test Equivalent to the Type 1 Test (verifying emissions after a cold start)."
udds = np.loadtxt('uddscol.txt', dtype=int, skiprows=2)
print(udds[0,0])
print(udds[1,0])
print(udds[:,0])
print(udds[:,1])

Velocity_mph = udds[:,1]

# Velocity (kph) vs Time (sec) Plot:
Time_s = udds[:,0]
Velocity_kph = udds[:,1]*1.60934
plt.plot(Time_s,Velocity_kph,'r-')
plt.xlabel("Time (sec)")
plt.ylabel("Velocity (kph)")
plt.legend(["Velocity"])
plt.title("Time (sec) vs Velocity (kph)",fontweight='bold')
plt.grid()
plt.show()

# Velocity (mph) vs Distance (mi) Plot :
Velocity_mps = Velocity_mph*0.44704
Distance_mi = np.cumsum(Velocity_mps)
plt.plot(Distance_mi,Velocity_mph,'y--')
plt.xlabel("Distance (mi)")
plt.ylabel("Velocity (mph)")
plt.legend(["Velocity"])
plt.title("Distance (mi) vs Velocity (mph)",fontweight='bold')
plt.grid()
plt.show()


# Acceleration (g) vs Time (sec) Plot :
accel_mpss = np.diff(Velocity_mps,prepend=0)
plt.plot(Time_s,accel_mpss,'g-',linewidth = 1)
plt.xlabel("Time (sec)")
plt.ylabel("Acceleration (m/sec^2)")
plt.legend(["Acceleration"])
plt.title("Time (sec) vs Acceleration (g)",fontweight='bold')
plt.grid()
plt.show()