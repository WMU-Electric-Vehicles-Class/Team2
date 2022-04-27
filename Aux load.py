# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 01:06:58 2022

@author: HP
"""

import numpy as np                              
from matplotlib import pyplot as plt            

x=np.linspace(0,1,100)
y=np.linspace(0,1,100)
x1=np.linspace(0,1,100)



E_consumpt_per100 = 34.6
const_amp = 80

batt_cap=93000
HVAC_batt_cap=91000


volt = 3.6
cells = 94
nom_volt=cells*volt

batt_cap_Ah = batt_cap/nom_volt
HVAC_batt_cap_Ah = HVAC_batt_cap/nom_volt
print('\n')
print('Useable Battery Capacity:', batt_cap, 'kWh')
print('Nominal Voltage:', round(nom_volt,2), 'V')
print('Useable Battery Capacity:', round(batt_cap_Ah,2), 'Ah')
print('\n')


def f(x):
    return (((batt_cap/1000)*x)/E_consumpt_per100)*100
plt.plot(x,f(x), label ='Original Range = 269 miles', color="blue")
print("Original Range",f(x))



#HVAC 
# def f(x1):
#     return (((HVAC_batt_cap/1000)*x1)/E_consumpt_per100)*100
# plt.plot (x1, f(x1), label = 'HVAC = 263 miles', color='green')
# print("HVAC",f(x1))

#Sound System
# x2=np.linspace(0,1,100)

# Sound_batt_cap=92000
# Sound_batt_cap_Ah = HVAC_batt_cap/nom_volt


# def f(x2):
#     return (((Sound_batt_cap/1000)*x2)/E_consumpt_per100)*100
# plt.plot(x2,f(x2), label = 'Audio system = 266 miles', color='red')
# print("Audio system",f(x2))


#Speed
# S_70=np.linspace(0,1,100)

# S_70_batt_cap=86000
# S_70_batt_cap_Ah = S_70_batt_cap/nom_volt

# x3=np.linspace(0,1,100)
# def f(x3):
#     return (((S_70_batt_cap/1000)*x3)/E_consumpt_per100)*100
# plt.plot(x3,f(x3), label = 'Speed at 70 mph = 248 miles', color='orange')
# print("Speed 70",f(x3))

# S_75=np.linspace(0,1,100)
# S_75_batt_cap=83500
# S_75_batt_cap_Ah = S_75_batt_cap/nom_volt

# x75=np.linspace(0,1,100)
# def f(x75):
#     return (((S_75_batt_cap/1000)*x75)/E_consumpt_per100)*100
# plt.plot(x75,f(x75), label = 'Speed at 75 mph = 241 miles', color='black')
# print("Speed 75",f(x75))

# S_80=np.linspace(0,1,100)
# S_80_batt_cap=76000
# S_80_batt_cap_Ah = S_80_batt_cap/nom_volt

# x80=np.linspace(0,1,100)
# def f(x80):
#     return (((S_80_batt_cap/1000)*x80)/E_consumpt_per100)*100
# plt.plot(x80,f(x80), label = 'Speed at 80 mph = 220 miles', color='magenta')
# print("Speed 80",f(x80))

# Combined Aux load
comb_AUX=np.linspace(0,1,100)

comb_AUX_batt_cap=80500
comb_AUX_batt_cap_Ah = comb_AUX_batt_cap/nom_volt

x4=np.linspace(0,1,100)
def f(x4):
    return (((comb_AUX_batt_cap/1000)*x4)/E_consumpt_per100)*100
plt.plot(x4,f(x4), label = 'Combined AUX load(75mph) = 233 miles', color='orange')
print("comb AUX load",f(x4))


plt.title("EV Range", fontweight='bold',fontsize=16)
plt.xlabel("SOC (%)",fontsize=14)
plt.ylabel("Range (miles)",fontsize=14)
plt.xticks(np.arange(0,1.1,0.1))  
plt.yticks(np.arange(0,280,20))                                                       
plt.grid()
plt.show()
plt.legend()
