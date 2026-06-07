import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430 * 10**(-11) # Gravitational constant
M = 5.972 * 10**(24) # Earth mass
T = 2.36059151 * 10**(6) # Total time of the orbit, time taken for a full orbit of the earth
dt = 10 # Delta t, change in time
StartPos = np.array([3.716391230125518 * 10**(8), 8.921654945387672])

#

Pos = StartPos # Moon's position relative to earth
MagPos = np.linalg.norm(Pos) # Magnitude of the distance between earth and moon

#

Magv = np.sqrt(G * M / MagPos) # Calculates the magnitude of the starting velocity of the moon
v = np.array([0, Magv])

N = int(T / dt) # N number of iterations is given by this

#
x = []
y = []


for n in range(0, N):
    MagPos = np.linalg.norm(Pos) # Recalculates the position of the moon every loop
    a = - G * M / MagPos **(3) * Pos # This calculates the vector acceleration acting on the moon
    v = v + a * dt # This calculates the magnitude of the new velocity V after a certain amount of time dt with an acceleration of a
    Pos = Pos + v * dt # This updates the position
    x.append(Pos[0])
    y.append(Pos[1])
    print(Pos[0], Pos[1])

fig = plt.figure()
ax = plt.axes()
ax.set_title('Test Animation')
ax.set_xlabel('Distance')
ax.set_ylabel('Distance')
plt.plot(x, y,)
plt.plot(0,0, "o", markersize= 50, color='green')
plt.plot(3.84 * 10**(8),0,"o",markersize = 20, color="grey")
plt.gca().set_aspect('equal', 'box') # This ensures the plot is not stretched in the x axis.
plt.show()
