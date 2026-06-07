import numpy as np # This imports numpy which is a module that adds more advanced maths capabilities to python.
import matplotlib.pyplot as plt # This imports Matplotlib which is a module that will allow me to plot the data from my orbit on a graph.

G = 6.67430 * 10**(-11) # Gravitational constant
M = 5.972 * 10**(24) # Earth mass
T = 2.36059151 * 10**(6) # Total time of the orbit, time taken for a full orbit of the earth
Timestep = 10 # This is the time step, basically the change in time in seconds between differences points in the orbit in my simulation. The lower this value is, the more accurate the simulation will be.
NumTimesteps = int(T / Timestep) # The amount of time steps or points within the orbit is given by this equation.

StartPos = np.array([3.716391230125518 * 10**(8), 8.921654945387672 * 10**(3)]) # This is a variable that stores the x and y coordinates of the starting position of the moon within the orbit.
Pos = StartPos # This is the current position variable, it sets the starting position as the current position.
MagPos = np.linalg.norm(Pos) # This uses the numpy module to calculate the magnitude of the distance of the moon relative to the earth.
Velocity = np.array([0, np.sqrt(G * M / MagPos)]) # This is a variable that stores the vector velocity of the moon.
# The initial x velocity is close to 0 as the moon is starting close to y = 0. This is a possible source of error in the program as in reality the moon will have some starting x velocity.

x = [] # List that stores all x positions that are calculated
y = [] # List that stores all y positions that are calculated

iteration = 0 # Variable that sets initial iteration to 0, this is used in the loop to allow the program to extract orbital data at certain points.

for n in range(0, NumTimesteps): # Loop that iterates through the physics of the program for NumTimesteps amount
    MagPos = np.linalg.norm(Pos) # Recalculates the magnitude of position of the mooon for every iteration of the loop. This is required to calculate the vector acceleration of the moon at different points.
    Acceleration = - G * M / MagPos **(3) * Pos # Calculation of the magnitude of the acceleration of the moon multiplied by the unit vector of position of the moon. This calculations the vector acceleration of the moon.
    Velocity = Velocity + Acceleration * Timestep  # Both variables, Velocity and Acceleration are vector quantities so can be added then multiplied by the timestep to find the new velocity. This is just v = u + at which is one of the most well known kinematic equations.
    Pos = Pos + Velocity * Timestep # Calculates the new position of the moon within orbit by adding Velocity * Timestep to the previous position.
    x.append(Pos[0]) # Adds the current x position to the variable that stores all x positions during the simulation.
    y.append(Pos[1]) # Adds the current y position to the variable that stores all y positions during the simulation.
    iteration += 1 # Adds 1 to the variable "Iteration" this is used by the if statement in the next line to check if data should be extracted at a point within the program.
    if iteration == 360: # If statement which runs the next lines of code if the Iteration variable is equal to 360. As the timestep is equal to 10 seconds this means that data will be extracted every hour in the simulation.
        with open("orbital_data.txt", 'a') as file: # This opens the text file in append mode, meaning data can be written into the file without deleting previous lines.
            file.write(f"{Pos[0]} {Pos[1]}\n") # Writes the x and y position into the file, the "\n" adds a new line in the text file.
        iteration = 0 # Sets the iteration variable back to 0 so data will be extracted after an hour again.

fig = plt.figure()
ax = plt.axes() # Adds axes to the graph
ax.set_title('A graph showing the orbit of the moon around the earth.') # Adds a total to the top of the graph.
ax.set_xlabel('Distance') # Labels x axis "Distance"
ax.set_ylabel('Distance') # Labels y axis "Distance"
plt.plot(x, y,) # Plots all of the data points that are stored in the lists x and y.
plt.plot(0,0, "o", markersize= 50, color='green') # This adds a green circle that represents the earth, not to scale.
plt.plot(3.84 * 10**(8),0,"o",markersize = 20, color="grey") # This adds a grey circle that represents the moon, not to scale.
plt.gca().set_aspect('equal', 'box') # This ensures the plot is not stretched in the x axis.
plt.show()
