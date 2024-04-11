# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:41:55 2024

@author: Asus
"""

import psutil
import matplotlib.pyplot as plt

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Create a line object to plot the CPU usage
cpu_line, = ax.plot([], [], label='CPU Usage')

# Create a line object to plot the memory usage
memory_line, = ax.plot([], [], label='Memory Usage')

# Set the x-axis label
ax.set_xlabel('Time (seconds)')

# Set the y-axis label
ax.set_ylabel('Usage (%)')

# Set the title of the plot
ax.set_title('CPU and Memory Usage')

# Show the legend
ax.legend()

# Start the animation
def animate(i):
    # Get the CPU and memory usage
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent

    # Update the line objects
    cpu_line.set_data(cpu_line.get_data()[0] + [i], cpu_line.get_data()[1] + [cpu_usage])
    memory_line.set_data(memory_line.get_data()[0] + [i], memory_line.get_data()[1] + [memory_usage])

    # Redraw the plot
    fig.canvas.draw()

# Call the animate function every 100 milliseconds
ani = animation.FuncAnimation(fig, animate, interval=100)

# Keep the plot alive
plt.show()