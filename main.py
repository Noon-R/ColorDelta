# usr/bin/env python3

import itertools
import numpy as np
import matplotlib.pyplot as plt
import colour 
import colour.plotting as cp

#RGBを0.0~0.1の間隔で分割し、組み合わせを列挙
col1 = [0.8,0.2,0.1]
col2 = [0.1,0.9,0.8]
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


#sRGBからXYZへ変換
XYZ = colour.sRGB_to_XYZ(rgb)
XYZ_c = colour.sRGB_to_XYZ(rgb_c)
#XYZからxyへ変換
xy = colour.XYZ_to_xy(XYZ)
xy_c = colour.XYZ_to_xy(XYZ_c)

cp.plot_chromaticity_diagram_CIE1931(bounding_box=(-0.1, 0.9, -0.1, 0.9), standalone=False)

#sRGB領域へプロット

plt.plot(xy[:,0], xy[:,1], 'o', markersize=2, label="rgb")
plt.plot(xy_c[:,0], xy_c[:,1], 'o', markersize=2, label="cmyk")
plt.legend() 

plt.savefig("r2g_4.jpg")