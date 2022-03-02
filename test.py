
from fastsim import vehicle, cycle, simdrive
veh = vehicle.Vehicle(18)
print(veh.Scenario_name)
cyc = cycle.Cycle("hwfet")
sim = simdrive.SimDriveClassic(cyc, veh)
sim.sim_drive()
print("MPGGE:", sim.mpgge_elec)
