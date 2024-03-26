import numpy as np
import matplotlib.pyplot as plt

# Read data from space.txt
with open('space.txt', 'r') as space_file:
    space_data = space_file.readlines()

# Read data from time.txt
with open('time.txt', 'r') as time_file:
    time_data = time_file.readlines()

# Extract nodes and time values
nodes = {}
times = {}

for line in space_data:
    algo, node = line.strip().split(': ')
    nodes[algo] = int(node.split()[0])

for line in time_data:
    algo, time = line.strip().split(': ')
    times[algo] = float(time.split()[0])

# Create histograms
algos = list(nodes.keys())
x = np.arange(len(algos))
width = 0.35

fig, ax1 = plt.subplots()

ax1.bar(x - width/2, list(nodes.values()), width, label='Nodes', color='b')
ax1.set_ylabel('Nodes')
ax1.set_xticks(x)
ax1.set_xticklabels(algos)
ax1.legend(loc='upper left')

ax2 = ax1.twinx()
ax2.bar(x + width/2, list(times.values()), width, label='Time (seconds)', color='r')
ax2.set_ylabel('Time (seconds)')
ax2.legend(loc='upper right')

fig.tight_layout()

plt.title('Nodes and Time for Different Algorithms for 3x3 TicTac')
plt.show()
