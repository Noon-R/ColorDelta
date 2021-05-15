import cv2
import numpy as np
import colors as cs
import random


width = 1024
height = 512

for num in range(7,20):

    startCol_rgb = [
        random.uniform(0, 255),
        random.uniform(0, 255),
        random.uniform(0, 255)
        ]

    endCol_rgb   = [
        random.uniform(0, 255),
        random.uniform(0, 255),
        random.uniform(0, 255)
        ]

    centerCol_rgb = [0,0,0]
    for i in range(0,3):
        centerCol_rgb[i] = (startCol_rgb[i] + endCol_rgb[i])/2
    print("rgb_center:")
    print(centerCol_rgb)
    rgb = np.linspace(startCol_rgb, endCol_rgb, width, endpoint=True)


    startCol_cmyk = cs.rgb2cmyk(startCol_rgb,255)
    endCol_cmyk = cs.rgb2cmyk(endCol_rgb,255)
    print("cmyk_start:")
    print([
        startCol_cmyk[0] * 100/255,
        startCol_cmyk[1] * 100/255,
        startCol_cmyk[2] * 100/255,
        startCol_cmyk[3] * 100/255
        ])
    print("cmyk_end:")
    print([
        endCol_cmyk[0] * 100/255,
        endCol_cmyk[1] * 100/255,
        endCol_cmyk[2] * 100/255,
        endCol_cmyk[3] * 100/255
        ])

    centerCol_cmyk = [0,0,0,0]
    for i in range(0,4):
        centerCol_cmyk[i] = (startCol_cmyk[i] + endCol_cmyk[i])/2
    print("cmyk_center:")
    print([
        centerCol_cmyk[0] * 100/255,
        centerCol_cmyk[1] * 100/255,
        centerCol_cmyk[2] * 100/255,
        centerCol_cmyk[3] * 100/255
        ])

    cmyk = np.linspace(startCol_cmyk, endCol_cmyk, width, endpoint=True)

    rgb_img = np.zeros((height, width, 3), np.uint8)
    rgb_c_img = np.zeros((height, width, 3), np.uint8)

    cmyk_img = np.zeros((height, width, 3), np.uint8)
    cmyk_c_img = np.zeros((height, width, 3), np.uint8)


    for h in range(0, height):
        for w in range(0, width):
            rgb_img[h, w] = [rgb[w][2], rgb[w][1], rgb[w][0]]
            rgb_c_img[h, w] = [centerCol_rgb[2], centerCol_rgb[1], centerCol_rgb[0]]  

            rgb_cmyk = cs.cmyk2rgb(cmyk[w],255)
            cmyk_img[h, w] = [rgb_cmyk[2],rgb_cmyk[1],rgb_cmyk[0]]

            rgb_c_cmyk = cs.cmyk2rgb(centerCol_cmyk,255)
            cmyk_c_img[h, w] = [rgb_c_cmyk[2], rgb_c_cmyk[1], rgb_c_cmyk[0]]  


    cv2.imwrite("./imgs/ColorGradation_"+str(num).zfill(2)+"_rgb.png", rgb_img)
    cv2.imwrite("./imgs/ColorGradation_"+str(num).zfill(2)+"_center_rgb.png", rgb_c_img)
    cv2.imwrite("./imgs/ColorGradation_"+str(num).zfill(2)+"_cmyk.png", cmyk_img)
    cv2.imwrite("./imgs/ColorGradation_"+str(num).zfill(2)+"_center_cmyk.png", cmyk_c_img)