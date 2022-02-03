import numpy as np
from matplotlib import pyplot as plt


#The New York City Cycle (NYCC) features low speed stop-and-go traffic conditions
nyc = np.loadtxt('nycccol.txt', dtype=int)
print(nyc[0,0])
print(nyc[1,0])
print(nyc[:,0])
print(nyc[:,1])

Velocity_mph = nyc[:,1]

# a. Velocity (kph) vs Time (sec) Plot:
Time_s = nyc[:,0]
Velocity_kph = nyc[:,1]*1.60934
plt.plot(Time_s,Velocity_kph,'r-')
plt.xlabel("Time (sec)")
plt.ylabel("Velocity (kph)")
plt.legend(["Velocity"])
plt.title("Time (sec) vs Velocity (kph)",fontweight='bold')
plt.grid()
plt.show()

# b. Velocity (mph) vs Distance (mi) Plot :
Velocity_mps = Velocity_mph*0.44704
Distance_mi = np.cumsum(Velocity_mps)
plt.plot(Distance_mi,Velocity_mph,color='orange',linestyle='--')
plt.xlabel("Distance (mi)")
plt.ylabel("Velocity (mph)")
plt.legend(["Velocity"])
plt.title("Distance (mi) vs Velocity (mph)",fontweight='bold')
plt.grid()
plt.show()


# c. Acceleration (g) vs Time (sec) Plot :
accel_mpss = np.diff(Velocity_mps,prepend=0)
plt.plot(Time_s,accel_mpss,color='purple',linewidth = 1)
plt.xlabel("Time (sec)")
plt.ylabel("Acceleration (m/sec^2)")
plt.legend(["Acceleration"])
plt.title("Time (sec) vs Acceleration (g)",fontweight='bold')
plt.grid()
plt.show()

#Utkarsh Karajgar