import numpy as np
import matplotlib as plot

# Constants

G = 6.67430 * 10**(-11) # Gravitational constant
EM = 5.972 * 10**(24) # Earths mass
MM = 7.347 * 10**(22) # Moons mass
T = 2358720 # Time taken for the moon to orbit the Earth

# Initial values

d = 3.84 * 10**(8) # Distance between the Earth and Moon

v_start = np.sqrt(G * EM / d)

v = np.array([0, v_start])

t = 0

# Equations

F = EM * MM / d**2 * G # Newton's law of Gravitation

a = F / MM # Newton's 2nd law

v = v + a * 10 # Velocity and acceleration equation


#



Pos = np.array([d,0])

for i in range(T):
    F = EM * MM / d**2 * G
    a = F / MM
    v = v + a * 10
    Pos = Pos + v * 10
    d = d + v
    t += 10

