import matplotlib
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = plt.axes()
ax.set_title('Test Animation')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Position (m)')
plt.show()