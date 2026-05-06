import numpy as np
import matplotlib.pyplot as plt

# Generate fake NDVI data
np.random.seed(42)

ndvi = np.random.rand(8, 50, 50)

# Simulate hotspot degradation
for t in range(8):
    ndvi[t, 20:30, 20:30] -= t * 0.05

# Compute slope
time = np.arange(8)

slope = np.polyfit(time, ndvi.reshape(8, -1), 1)[0]
slope_map = slope.reshape(50, 50)

# Detect hotspot
hotspot = slope_map < -0.02

# Plot hotspot
plt.imshow(hotspot, cmap='Reds')
plt.title("NDVI Hotspot Detection")
plt.colorbar()

# Save image
plt.savefig("hotspot.png")

plt.show()

print("Hotspot project completed!")