import numpy as np # This imports numpy which is a module that adds more advanced maths capabilities to python.
import matplotlib.pyplot as plt # This imports Matplotlib which is a module that will allow me to plot the data from my orbit on a graph.

G = 6.67430 * 10**(-11) # Gravitational constant
M = 5.972 * 10**(24) # Earth mass
T = 2.36059151 * 10**(6) # Total time of the orbit, time taken for a full orbit of the earth
TimeStep = 60 # Time step, the time in seconds between different points in my simulated orbit, this is set to 1 minute as it would have been difficult to calculate two positions of the moon only 1 second apart.
PreviousPos = np.array([383995000, -61200]) # This is the approximate position of the moon 1 minute before the starting position.
StartPos = np.array([384000000, 0]) # This is the starting position of the moon stored as a vector quantity using the array function with numpy.
Pos = StartPos # Sets the current position equal to the starting position.
NumTimeSteps = int(T / TimeStep) # The amount of time steps or points within the orbit is given by this equation.

x = [] # List that stores all x positions that are calculated
y = [] # List that stores all y positions that are calculated

iteration = 0 # Variable that sets initial iteration to 0, this is used in the loop to allow the program to extract orbital data at certain points.

for n in range(0, NumTimeSteps): # Loop that iterates through the physics of the program for NumTimesteps amount
    MagPos = np.linalg.norm(Pos) # Recalculates the magnitude of position of the mooon for every iteration of the loop. This is required to calculate the vector acceleration of the moon at different points.
    Acceleration = - G * M / MagPos ** (3) * Pos #  Calculation of the magnitude of the acceleration of the moon multiplied by the unit vector of position of the moon. This calculations the vector acceleration of the moon.
    NewPos = (2 * Pos) - PreviousPos + (Acceleration * TimeStep ** (2))
    x.append(Pos[0]) # Adds the current x position to the list that stores all x positions during the simulation.
    y.append(Pos[1]) # Adds the current y position to the list that stores all y positions during the simulation.
    PreviousPos = Pos
    Pos = NewPos
    iteration += 1 # Adds 1 to the variable "Iteration" this is used by the if statement in the next line to check if data should be extracted at a point within the program.
    if iteration == 60:
        with open("orbital_data_verlet.txt", 'a') as file:
            file.write(f"{Pos[0]} {Pos[1]}\n")
        iteration = 0

fig = plt.figure()
ax = plt.axes()
ax.set_title('Test Animation')
ax.set_xlabel('Distance')
ax.set_ylabel('Distance')
plt.plot(x, y,)
plt.plot(0,0, "o", markersize= 50, color='green')
plt.gca().set_aspect('equal', 'box') # This ensures the plot is not stretched in the x axis.
plt.show()


