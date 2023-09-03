import satellite
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches

z = 35850
v0 = 4.1

model = satellite.SatelliteOrbit()
model.cal(z, v0)
x, y = model.x_, model.y_

print("地上高さ： {} km" .format(z))
print("初速度： {} km/s" .format(v0))
print("離心率： {} ".format(model.e) )

fig, ax = plt.subplots(figsize=(8,8))
ax.grid()
ax.set_xlim(-8e4, 8e4)
ax.set_ylim(-8e4, 8e4)
ax.set_aspect('equal')

#軌道
if model.e > 1.0 :
    y[y > y.max() * 0.95] = np.inf
    y[y < y.min() * 0.95] = -np.inf
plt.scatter(x,y,color='r',label="satellite Orbit")

#地球の表示
Re = model.Re
earth = patches.Circle( (0,0), Re, facecolor="skyblue", edgecolor="deepskyblue", label="earth")
ax.add_patch(earth)

plt.legend()
plt.show()