import math 
#telescopes for a gaussian beams


wavelenght = 663 #nm wavelenght for a beam 
w = 0.5 #mm beam waist of the gaussian beam at the first lens
d_ideal = 2 # desided diameter of the beam after the second lens in mm
M_squared = 1 # beam quality factor (M^2 = 1 for a perfect gaussian beam, M^2 > 1 for real beams)

f1 = 100 #mm focal length of first lens
f2 = 200 #mm focal length of second lens

# unit conversions 
wavelenght_mm = wavelenght/1e6 # convert wavelenght to mm
# formulas for telescopes 
M = f2/f1 # magnification of the telescope
d = 2* w *M  # diameter of the beam after the second lens
fz = f1 + f2 # distance between the two lenses for a telescope


w0 = 2 * M_squared * wavelenght_mm * f1 / (math.pi * w) # beam waist after the first lens 


print("Magnification: ", M) 
print("Diameter: ", d) 
print("Distance between lenses: ", fz) 

calc = True # set to True for magic calculations!
if calc:
    Mag_needed = d_ideal/(2*w)
    print("Magnification needed for desired diameter: ", Mag_needed)

    f2_calc = d_ideal/(2*w) * f1
    print("Calculated focal length of second lens for desired diameter: ", f2_calc)

else: 
    pass
print("checking" )
