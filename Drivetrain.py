# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 02:33:44 2022

@author: HP
"""

from cmath import pi
import numpy as np
from matplotlib import pyplot as plt

#The Ford Mustang Mach E GT is all wheel drive with 1 speed transmission with gear ratio 9.05.
GR=9.05

#Wheel radius of Ford Mach E GT is 10 inches

Wheel_radius = 10 #inch
print("Wheel Radius =",Wheel_radius,"inches")

Ms = np.zeros(131)

for i in range(0,131):
    Angular_Velocity = (((i/Wheel_radius)*60)/2*pi)
    Motor_Speed= Angular_Velocity*9.05
    Ms[i] = Motor_Speed


    
Velocity = np.arange(0,131)

plt.plot(Velocity,Ms, label="Velocity vs Motor Speed", color="orange")
plt.xlabel("Velocity (mph)")
plt.ylabel("Motor Speed (rpm)")
plt.title("Motor Speed vs Velocity", fontweight='bold')
plt.grid()
plt.legend()
plt.show()