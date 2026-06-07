from vpython import *
from numpy import *
import numpy as np

earth = sphere(pos=vector(0,0,0),radius=1, color=color.blue)
satellite = sphere(pos=vector(0,0,0),radius=1, color=color.white)

time = 0
orbitspeed = 2*np.pi/5

while True:
    rate(10)

    time += 1
    x = 10*np.cos(orbitspeed*time)
    y = 10*np.sin(orbitspeed*time)
    satellite.pos = vector(x,y,0)