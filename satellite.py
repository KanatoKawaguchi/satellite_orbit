import numpy as np

class SatelliteOrbit :
    def __init__(self):
        self.Re = 6378
        self.v1 = 7.908 
        self.e = None
        self.x_ = None
        self.y_ = None

    def cal(self, z, v0):
        theta = np.linspace(0, 2 * np.pi, 360)
        h = (self.Re + z) * v0
        K = self.Re * self.v1**2
        l = h**2 / K                                                   #半直弦
        e = ((self.Re + z) * v0**2 ) / (self.Re * self.v1**2) - 1      #離心率

        self.x_ = (l * np.cos(theta)) / (1 + e*np.cos(theta))
        self.y_ = (l * np.sin(theta)) / (1 + e*np.cos(theta))
        self.e = e