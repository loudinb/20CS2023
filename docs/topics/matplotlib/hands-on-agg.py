import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend
import matplotlib.pyplot as plt

plt.ioff()  # Turn off interactive mode

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])

fig.savefig("plot.png")  # Save the plot to a file

