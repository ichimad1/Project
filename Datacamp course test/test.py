import numpy as np
import math
radius = np.array([1, 1.5, 1.6])
area = math.pi * (radius ** 2)
boolean = area < 20
print(area[boolean])
