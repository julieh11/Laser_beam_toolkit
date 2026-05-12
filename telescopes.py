import math 
#telescopes for a gaussian beams


wavelenght = 663 #nm wavelenght for a beam 
w = 0.8375 #mm beam waist of the gaussian beam at the first lens
M_squared = 1 # beam quality factor (M^2 = 1 for a perfect gaussian beam, M^2 > 1 for real beams)


d_ideal = .85 # desided diameter of the beam after the second lens in mm
zr_ideal = 50  # desired Reilight after first lens in mm aka inside telescope 

f1 = 50 #mm focal length of first lens
f2 = 99.7 #mm focal length of second lens

# unit conversions 
wavelenght_mm = wavelenght/1e6 # convert wavelenght to mm
# formulas for telescopes 
M = f2/f1 # magnification of the telescope
d = 2* w *M  # diameter of the beam after the second lens
fz = f1 + f2 # distance between the two lenses for a telescope


w0 = 2 * M_squared * wavelenght_mm * f1 / (math.pi * w) # beam waist after the first lens 

zr = math.pi * w0**2 / (wavelenght_mm * M_squared) # Rayleigh range of the beam after the first lens
zr_full = zr * 2 #full rayleigh range includinmg both sides of the lenght 

print("Magnification: ", M) 
print("Diameter: ", d) 
print("Distance between lenses: ", fz) 
print("Beam waist after first lens: ", w0)
print("Rayleigh range: ", zr)
print("Full Rayleigh range: ", zr_full)


f = [25,30,35,40,50,60,75,100,125,150,200,250 ,300, 350,400,450,500,600,750,850] # focal lengths for plano convex lenses in mm
component_in_telescope = True 
component_lenght = 45 #mm lenght of the component to be placed in the telescope, should be less than rayleigh range and the distance between the lenses for it to fit in the telescope

if component_in_telescope:
    zr_range_component =  component_lenght + 10 #buffer of 10mm 

else: 
    pass 

calc = True # set to True for magic calculations!
if calc:
    Mag_needed = d_ideal/(2*w)
    print("Magnification needed for desired diameter: ", Mag_needed)

    f2_calc = d_ideal/(2*w) * f1
    print("Calculated focal length of second lens for desired diameter: ", f2_calc)

    f2_alt = Mag_needed * f1
    print("Alternative calculation for focal length of second lens if focal lenght of first lens is known: ", f2_alt)

else: 
    pass
print("checking" )
