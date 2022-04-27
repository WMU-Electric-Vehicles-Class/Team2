import pandas as pd
import numpy as np
import math

from matplotlib import pyplot as plt
import seaborn as sns
sns.set()
udds = pd.read_csv("61508025 Test Data.txt", sep="\t")

# Vehicle
m = 2085  # kg
Cd = 0.259
A = 3.06  # m^2
Crr = 0.014
# Battery
Rint = 0.373  # ohm
Q = 400 * 3600  # C 
Voc = 338.4  # V

# Constants
rho = 1.2
g = 9.81
# Initial state of charge
SOC = 1.00
#udds["Target Speed (m/s)"] = udds["Target Speed (mph)"] * 0.44704

SOC_list = []

for i in range(len(udds)):
    t = udds["Time[sec]"].iloc[i]
    v = udds["Dyno_Speed[mph]"].iloc[i]
    
    # Calculate acceleration
    if i == 0:
        dv = 0
        dt = 1
    else:
        t_prev = udds["Time[sec]"].iloc[i-1]
        v_prev = udds["Dyno_Speed[mph]"].iloc[i-1]

        dv = v - v_prev
        dt = t - t_prev
    a = dv/dt

    # Vehicle dynamics
    F_drag = 1/2 * Cd * rho * A * v**2
    F_rr = Crr * m * g
    F_prop = F_drag + F_rr + m*a

    # Power (neglecting efficiencies)
    P = F_prop * v

    # Battery current
    try:
        I = (Voc - math.sqrt(Voc**2 - 4*P*Rint))  /  (2*Rint)
    except ValueError:
        I = Voc / (2*Rint)


    # SOC
    dSOC = -I/Q * dt
    SOC += dSOC
    if SOC < 0:
         SOC = 0
    SOC_list.append(SOC)
SOC_array = np.array(SOC_list)


# Create axes
fig, ax1 = plt.subplots(figsize=(10,5))
ax2 = ax1.twinx()

# Disable grids
ax1.grid(which='major', axis='y')
ax2.grid(which='major', axis='y')

# Axis labels
ax1.set_xlabel("Time (sec)")
ax1.set_ylabel("State of Charge (%)")
ax2.set_ylabel("Velocity (mph)")

# Plot
line1 = ax1.plot(udds["Time[sec]"], SOC_array*100, label="SOC", linewidth=3, color="red")
line2 = ax2.plot(udds["Time[sec]"], udds["Dyno_Speed[mph]"], color="blue", alpha=0.75, label="Velocity")

# Legend
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels)

plt.show()
