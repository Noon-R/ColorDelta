# usr/bin/env python3

import itertools
import numpy as np
import matplotlib.pyplot as plt
import colour 
import colour.plotting as cp
from mpl_toolkits.mplot3d import Axes3D
import cv2

def rgb2hsv(rgb):
    ret = np.empty((3,len(rgb[0])))
    for i in range(len(rgb[0])) :
        r = rgb[0][i]
        g = rgb[1][i]
        b = rgb[2][i]
        mx, mn = max(r,g,b), min(r,g,b)
        diff = mx - mn

        if mx == mn : h = 0
        elif mx == r : h = 60 * ((g-b)/diff)     
        elif mx == g : h = 60 * ((b-r)/diff) + 120  
        elif mx == b : h = 60 * ((r-g)/diff) + 240
        if h < 0 : h = h + 360

        if mx != 0:s = diff/mx       
        else: s = 0

        v = mx
        ret[0][i] = h/360
        ret[1][i] = s
        ret[2][i] = v

    return ret

#RGBを0.0~0.1の間隔で分割し、組み合わせを列挙
col1 = [0.2,0.2,0.9]
col2 = [0.8,0.7,0.5]
r = np.linspace(col1[0], col2[0], 15, endpoint=True)
g = np.linspace(col1[1], col2[1], 15, endpoint=True)
b = np.linspace(col1[2], col2[2], 15, endpoint=True)

col1_k = min(1 - col1[0],1 - col1[1],1 - col1[2])
col1_cmy = [
    (1 - col1[0] - col1_k) / (1 - col1_k),
    (1 - col1[1] - col1_k) / (1 - col1_k),
    (1 - col1[2] - col1_k) / (1 - col1_k)
]

col2_k = min(1 - col2[0],1 - col2[1],1 - col2[2]) 
col2_cmy = [
    (1 - col2[0] - col2_k) / (1 - col2_k),
    (1 - col2[1] - col2_k) / (1 - col2_k),
    (1 - col2[2] - col2_k) / (1 - col2_k)
]
c = np.linspace(col1_cmy[0], col2_cmy[0], 15, endpoint=True)
m = np.linspace(col1_cmy[1], col2_cmy[1], 15, endpoint=True)
y = np.linspace(col1_cmy[2], col2_cmy[2], 15, endpoint=True)
k = np.linspace(col1_k, col2_k, 15, endpoint=True)

rgb_c = np.empty((0,3),dtype=np.float)
rgb = np.empty((0,3),dtype=np.float)
#rgb = np.array(list(itertools.product(r,g,b)),dtype=np.float)
#print(rgb)
for idx in range(len(r)):
    rgb = np.append(rgb, np.array([[r[idx],g[idx],b[idx]]]),axis=0 )

    r_c = 1 - min(1, c[idx]*(1-k[idx])+k[idx])
    g_c = 1 - min(1, m[idx]*(1-k[idx])+k[idx])
    b_c = 1 - min(1, y[idx]*(1-k[idx])+k[idx])
    rgb_c = np.append(rgb_c, np.array([[r_c,g_c,b_c]]),axis=0 )

rgb = np.ravel(rgb)
rgb_c = np.ravel(rgb_c)

rgb_c = np.reshape(rgb_c, (3,-1),order="F")
rgb = np.reshape(rgb, (3,-1),order='F')

hsv = rgb2hsv(rgb)
hsv_c = rgb2hsv(rgb_c)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#ax.set_xlabel("R")
#ax.set_ylabel("G")
#ax.set_zlabel("B")

ax.set_xlabel("H")
ax.set_ylabel("S")
ax.set_zlabel("V")

ax.set_xlim(1, 0)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)

#ax.scatter3D(rgb[0], rgb[1], rgb[2])
#ax.scatter3D(rgb_c[0], rgb_c[1], rgb_c[2],c="red")

ax.scatter3D(hsv[0], hsv[1], hsv[2])
ax.scatter3D(hsv_c[0], hsv_c[1], hsv_c[2],c="red")

ax.set_title("Color Lerp")
plt.savefig("3dLerp_1.jpg")
plt.show()
