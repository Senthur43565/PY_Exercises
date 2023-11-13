import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots()
sc = ax.scatter([], [], s=100)

# Set the axis limits
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1, 1)

# Initialize empty data
data = np.array([]).reshape(0, 2)

# Function to initialize the plot
def init():
    sc.set_offsets(data)
    return sc,

# Function to update the plot
def update(frame):
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x + frame)
    new_data = np.column_stack((x, y))
    data = np.vstack((data, new_data))
    sc.set_offsets(data)
    return sc,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 128),
                    init_func=init, blit=True)

# Display the animation
plt.show()
