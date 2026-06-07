import numpy as np
import matplotlib.pyplot as plt
# DISCLAIMER
# I did not create this program, I used ChatGPT to create this as an example then annotated it to help better understand the parts of this program.

Gravity = 6.67430e-11 # Gravity constant
Earth_Mass = 5.972e24 # Earths mass


Step = 10 # Time increments
Full_Orbit = 86400 * 27 # Total time of the orbit, seconds in a day * 27
n = int(Full_Orbit/Step) # How many iterations

Position = np.array([3.844e8,0]) # Starting position of the moon in orbit
v = np.array([0,1018]) # starting velocity of the moon in orbit

Positions = np.zeros((n,2)) # Variable "Positions" stores all the positions throughout the orbit
Positions[0] = Position # Unsure on what this line means

for x in range(n - 1): # Loop that cycles through the orbit Physics
    a = -Gravity * Earth_Mass * Position / np.linalg.norm(Position) **3 # Equation for vector orbital acceleration
    v = v + a * Step # Calculates the new velocity every step
    Position = Position + v * Step # Calculates the new position every step
    Positions[x + 1] = Position # Updates the position storage variable


plt.plot(Positions[:,0], Positions[:,1]) # Plots the position storage variable on a graph
plt.scatter(0, 0, color='green') # Defines the type of graph
plt.gca().set_aspect("equal") # Details on aspect ratio
plt.xlabel("x (m)") # Labels the x axis
plt.ylabel("y (m)") # Labels the y axis
plt.show() # Shows the graph after all the calculations are complete
