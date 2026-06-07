from vpython import *
from numpy import *
import numpy as np

earth = sphere(pos=vector(0,0,0), radius=10, texture=textures.earth)
satellite = sphere(pos=vector(0,0,0), radius=1, texture=textures.metal)

time = 0
orbitalvelocity = 2*np.pi/5
orbitalradius = 20
counter = 0

while True:
    while True:
        for counter in range(1,300):
            rate(120)
            time += 0.05
            x = orbitalradius * np.cos(orbitalvelocity * time)
            z = orbitalradius * np.sin(orbitalvelocity * time)
            satellite.pos = vector(x,0,z)
            counter += 1
        counter = 0
        break
    while True:
        for counter in range(1,300):
            rate(120)
            time += 0.05
            x = orbitalradius * np.cos(orbitalvelocity * time)
            y = orbitalradius * np.sin(orbitalvelocity * time)
            satellite.pos = vector(x, y, 0)
            counter += 1
        counter = 0
        break
    while True:
        for counter in range(1,300):
            rate(120)
            time += 0.05
            z = orbitalradius * np.cos(orbitalvelocity * time)
            y = orbitalradius * np.sin(orbitalvelocity * time)
            satellite.pos = vector(0, y, z)
            counter += 1
        counter = 0
        break