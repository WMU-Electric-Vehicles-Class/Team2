from cmath import e
import numpy as np                              #import numpy
from matplotlib import pyplot as plt            #library call
from scipy import integrate
from scipy.integrate import quad

x=np.linspace(0,1,100)
y=np.linspace(0,1,100)
z=np.linspace(0,88,100)
a=np.linspace(0,200,100)


E_consumpt_per100 = 34.6
const_amp = 80

batt_cap=88000

volt = 3.6
cells = 94
nom_volt=cells*volt

batt_cap_Ah = batt_cap/nom_volt

print('\n')
print('Useable Battery Capacity:', batt_cap, 'kWh')
print('Nominal Voltage:', round(nom_volt,2), 'V')
print('Useable Battery Capacity:', round(batt_cap_Ah,2), 'Ah')
print('\n')


def f(x):
    return (((batt_cap/1000)*x)/E_consumpt_per100)*100
plt.title("EV Range")
plt.xlabel("SOC (%)")
plt.ylabel("Distance Traveled (miles)")                                                        
plt.grid()
plt.plot(x,f(x))
plt.show()

def f(y):
    return (y*(((batt_cap_Ah/const_amp))*60))
plt.title("Discharge Time")
plt.xlabel("Charge (%)")
plt.ylabel("Time (minutes)")                                                           
plt.grid()
plt.plot(y,f(y))
plt.show()

home_v = 120
home_a = 15
home_kw = (home_v * home_a)/1000
#print(home_kw)

improve_v = 240
improve_a = 25
improve_kw = (improve_v*improve_a)/1000
#print(improve_kw)

ford_v = 240
ford_a = 48
ford_kw = (ford_a*ford_v)/1000
#print(ford_kw)

print('\n')
avg_batt_eff = 0.9
print('Assumed Battery Efficiency:',avg_batt_eff,'%')




def f(z):
    return (z/(home_kw*avg_batt_eff))
plt.plot (z, f(z), label = 'Home 120V 15A Outlet')   

def f(z):
    return (z/(improve_kw*avg_batt_eff))
plt.plot (z,f(z), label = 'Home 240V 25A Outlet')   

def f(z):
    return (z/(ford_kw*avg_batt_eff))
plt.plot (z,f(z), label = 'Ford 240V 48A Outlet')   


plt.title("Compare Charge Options")
plt.xlabel("Charge (kWh)")                                                #x axis label
plt.ylabel("Time (Hours)")                                                  #y axis label
plt.legend()                                                              #show legend
plt.grid()
#plt.ylim([0, 1.01])
plt.axvline(x=88,color='Red')
plt.show()

home_time = (batt_cap/1000)/(home_kw*avg_batt_eff)
print('Hours to Charge with 120V 15A Home Outlet = ',round(home_time,2))

improve_home_time = ((batt_cap/1000)/(improve_kw*avg_batt_eff))
print('Hours to Charge with 240V 25A Home Outlet = ',round(improve_home_time,2))

ford_time = ((batt_cap/1000)/(ford_kw*avg_batt_eff))
print('Hours to Charge with 240V 48A Ford Outlet = ',round(ford_time,2))


gal = 3.70
mpg = 20
mpe = 3.46
utility = .14
print('Cost for Gallon of Gas = $',gal,'Assumed mpg for gas car =', mpg)
print('Cost for kWh of Electricity = $',utility,'Assumed kWh/mile for EV car =', mpe)


def f(a):
    return ((a/mpg)*(gal))
plt.plot (a,f(a),label = 'Gas Cost', color='Orange')  
def f(a):
    return ((a/mpe)*(utility))
plt.plot (a,f(a),label = 'Electricity Cost',color='Blue')   
plt.title("Cost Comparison")
plt.xlabel("Distance Traveled (miles)")
plt.ylabel("Cost (dollars)")                                                           
plt.grid()
plt.legend() 
plt.plot(a,f(a))
plt.show()

annual_mile = 20000

annual_gas = ((annual_mile/mpg)*(gal))
print('\n')
print('Annual Gas Cost: $', annual_gas)

annual_elec = ((annual_mile/mpe)*(utility))
print('Annual Electricity Cost: $', round(annual_elec,2))

annual_save = annual_gas-annual_elec
print('Annual Savings: $', round(annual_save,2))

vehicle_life_years = 20
savings_life = annual_save*vehicle_life_years
print('Savings Over Life of Vehicle (20yrs): $', round(savings_life,2))
print('\n')
print('\n')

