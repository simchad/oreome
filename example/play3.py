import numpy as np
import matplotlib.pyplot as plt

# Define the circles
def quarter_circle(x, y):
    return (x-20)**2 + y**2 <= 20**2

def half_circle(x, y):
    return x**2 + (y-10)**2 <= 10**2

# Define the Monte Carlo method
def monte_carlo(n_samples=3000000):
    xs = []
    ys = []
    count = 0
    for _ in range(n_samples):
        x = np.random.uniform(0, 20)
        y = np.random.uniform(0, 20)
        if quarter_circle(x, y) and half_circle(x, y):
            xs.append(x)
            ys.append(y)
            count += 1
    area = count / n_samples * 20 * 20
    return xs, ys, area

# Generate the points
xs, ys, area = monte_carlo()

# Define the square
square = plt.Rectangle((0,0),20,20,fill=False)

# Define the quarter circle
quarter_circle = plt.Circle((20, 0), 20, color='r', fill=False, clip_on=False)

# Define the half circle
half_circle = plt.Circle((0, 10), 10, color='b', fill=False, clip_on=False)

# Create the plot
fig, ax = plt.subplots()
ax.add_artist(square)
ax.add_artist(quarter_circle)
ax.add_artist(half_circle)
plt.scatter(xs, ys, s=1)
plt.xlim(0, 20)
plt.ylim(0, 20)
plt.gca().set_aspect('equal', adjustable='box')
plt.title(f'Estimated area between the two circles: {area:.3f} cm^2, n=3,000,000')
plt.show()
