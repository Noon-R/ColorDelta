import numpy as np

rgb = np.array(list(np.linspace(0, 1, 15, endpoint=True),np.linspace(2, 3, 15, endpoint=True),np.linspace(4, 5, 15, endpoint=True)))
print(rgb)

r,g,b = rgb
print(r)
print(g)
print(b)