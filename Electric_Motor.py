# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 20:43:50 2022

@author: HP
"""
import math
from cmath import pi
import numpy as np
from matplotlib import pyplot as plt

# The Ford Mustang Mach E GT uses two 3 phase permanent magnet synchronous motor rated at 450 V and (assumed) 50 kVA.
#M-9000-MACHE Eluminator is a crate motor for the 2021 Ford Mustang Mach E GT offers max speed of 13,800 rpm with a gear ratio of 9.05:1.
# We are considering one of the motor for calculation.
# Assumptions: 4 poles, wye-connected, equivalent field source current = 310 A, Power factor = 1

p = 4
Pf = 1
Nominal_voltage = 450
#Rated Phase Voltage(Vs)
Vs = Nominal_voltage/math.sqrt(3) #volts

If = 310 # Ampere assume

Is = (50*1000)/(3*Vs)
print("Rated Stator Current = ",Is,"V")

#Motor_Speed(Wm) This one is maximum speed as motor has capacity 13800 rpm
Motor_Speed = 13800 #rpm
print("Motor Speed = ",Motor_Speed,"rpm")

#Synchronous_Speed(Ws)
Synchronous_Speed = (0.5*p*Motor_Speed*2*pi)/60
print("Synchronous Speed = ",Synchronous_Speed,"rad/sec")

#Motor_Torque(Tm)
Motor_Torque = 3*(p/Synchronous_Speed)*Vs*Is*Pf
print("Motor Torque = ",Motor_Torque,"Nm")

#Motor_Power(Pm)
Motor_Power = (Motor_Speed*Motor_Torque*(2*pi/60))/1000
print("Motor Power = ",Motor_Power,"kW")



#Assuming Base speed of motor
Base_Speed=2500
Max_Speed =13800

#Chracteristics of EV vehicle plot
Max_Motor_Power = Motor_Torque*2*pi*Base_Speed/60
Tm=[]
Ws=[]
Pm=[]



Ms = np.arange(0,13801)
#function for synchronous speed
def f(s):
    return ((p/2)*s*(2*pi/60))

#function for motor power
def fp(a):
    return ((2*pi*(a/60)*Motor_Torque)/1000)
    
s=0

for i in range(0,Max_Speed+1):
    
    if i <= 2500:
      a= ((2*pi*(i/60)*Motor_Torque)/1000)
      Tm.append(Motor_Torque)
      Ws.append(s)
      Pm.append(a)
      
    if 2500 < i < 13801:
      Tm.append(Max_Motor_Power/(2*pi*(i/60)))
      Ws.append(s)
      Pm.append((Max_Motor_Power/1000))
      




# Motor Torque vs Motor Speed
plt.plot(Ms,Tm, label="Motor Torque", color="green")

# Motor Power vs Motor Speed
plt.plot(Ms,Pm, label="Motor Power", color = "red",linestyle='--')
plt.legend(loc="upper right")

   
plt.xlabel("Motor Speed (rpm)",fontsize=14)
plt.ylabel("Motor Torque (Nm) and Motor Power (kW)",fontsize=14)
plt.title("Motor Torque vs Motor Speed",fontweight='bold',fontsize=16)
plt.grid()
plt.show()





