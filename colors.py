import numpy as np

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

def rgb2cmyk(rgb,max):
    k = min(1 - rgb[0]/max,1 - rgb[1]/max,1 - rgb[2]/max)
    cmy = [
    (1 - rgb[0]/max - k) / (1 - k),
    (1 - rgb[1]/max - k) / (1 - k),
    (1 - rgb[2]/max - k) / (1 - k)
    ]

    return [cmy[0]*max,cmy[1]*max,cmy[2]*max,k*max]

def cmyk2rgb(cmyk,max):
    r= 1 - min(1, cmyk[0]/max*(1-cmyk[3]/max)+cmyk[3]/max)
    g = 1 - min(1, cmyk[1]/max*(1-cmyk[3]/max)+cmyk[3]/max)
    b = 1 - min(1, cmyk[2]/max*(1-cmyk[3]/max)+cmyk[3]/max)
    return [r*max,g*max,b*max]