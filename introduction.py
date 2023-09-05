import matplotlib.pyplot as plt
import numpy as np

# Data For plotting
x = np.linspace(0.0, 1.0, 31)
f1 = x
f2 = x**2

# Plotting
fig = plt.figure()

plt.plot(x, f1, color="r", marker="o", linestyle="-.", label="f(x)=x")
plt.plot(x, f2, color="b", marker="x", linestyle="-.", label="f(x)=x^2")
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("Our first plot!")

# Draw the grid on the figure
plt.grid()

# Create the legend
plt.legend()

# Save the file to a file you can send to your friends
fig.savefig("pyplotexampleplot.png")

# Display the figure
plt.show()