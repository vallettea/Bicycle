from math import *


# parameters to choose:
# rider
A = 82 # inseam height
cubit = 46 # from elbow to nails, hand opened
TM = 67 # torso measurment
AM = 66 # arm measurment

# bike
B = 27 # bottom braket height in cm
C = 4 # crotch clearance (4cm for touting 6cm for racing)
E = radians(73.2) # seat tube angle
HTA = radians(72) # head tube angle:70:resilient and confort (touring) 75: stiff (race)
FR = 4.5 # fork rake: + for touring - for race
R = 33.4 # wheel radius



# outputed parameters
D = A - B - C
ST = D/sin(E) # seat tube length
top_tube_from_seat_tube = {49.5 : 51.5, 51.0 : 52.7, 52.0 : 53.8, 53.0 : 54.3, 54.0 : 54.7, 55.0 : 55.4, 56.0 :56.1, 57.0 : 56.7, 58.0 : 57.3, 59.0 : 57.9, 60.0 : 58.5, 61.0 : 59.1, 62.0 : 59.5, 63.0 : 60.1, 64.0 : 60.5, 65 : 60.8}
TT = top_tube_from_seat_tube[int(ST)]
Stem = (TM+AM)/2.3 - TT

print "D : %s" % str(D)
print "ST : %s" % str(ST)
print "TT : %s" % str(TT)

# check
print "========== checks ==========="
print "Stem from torso:", Stem
Stem2 = 2.5 + cubit + 15 -TT
print "Stem form cubit:", Stem2
trail = (R*cos(HTA) - FR)/sin(HTA)
print "Trail (5 to 7): ", trail
print "Front center (around 58)"
print "chainstay (40 for race to 47 for touring"
print "check clearance"
