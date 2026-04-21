#power transmission of a gaussian beam through an apperture 
import math

r = .5 #mm radius of aperture 
w = 1.35 # mm beam radius w(z)at z
p0 = 1 # initial power of the beam mW (default is one change if interestd in actual power transmitted)
P = p0 * (1 - math.exp(-2*r**2/w**2))
P_transmitted = P * p0  #  mW
Apperture_transmission = P * 100 # percentage of power transmitted through the apperture

print("Apperture transmission: ",f"{Apperture_transmission:.4f}", "%")
print("Power transmitted: ", f"{P_transmitted:.4f}", "mW")

