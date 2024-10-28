import datetime
import numpy as np
from PIL import Image
#DIN A4 ist 21 x 29,7
# Höhe definiert 
max_iter = 30
res_h = 200

rect = {
    "im": [-1.7,1.7],
    "re": [-2.4,1.6]
}
res_w = res_h * ( (abs(rect['re'][0])+abs(rect['re'][1])) / (abs(rect['im'][0])+abs(rect['im'][1])) )
res_w = int(res_w)

img = [[[0,0,0] for x in range(0,res_w)] for y in range(0,res_h)]

x = 0
y = 0
abs_h = abs(rect['im'][0])+abs(rect['im'][1])
abs_w= abs(rect['re'][0])+abs(rect['re'][1])
h_v = rect['im'][0]
w_v = rect['re'][0]
for temp_im in range(0,res_h):
    x = 0
    print(y)
    
    for re in range(0,res_w):
        im = (temp_im/res_h) * abs_h + h_v
        re = (re/res_w) * abs_w + w_v
        re_1 = re
        im_1 = im
        z = 0
        k = 0
        while k < max_iter:
            #mit n = 0,1,2,3,... und x0=y0=0
            temp_re = re
            re = re * re - im * im + re_1
            im = 2 * temp_re * im + im_1 
            
            z = re * re + im * im # z hoch 2
            
            k +=1

            if z>4:
                img[y][x] = [0,0,(k/max_iter)*255]
                break

        x += 1
    
    y += 1

image = Image.fromarray(np.array(img).astype('uint8'),'RGB')


image.show()
#image.save("mandelbrot"+str(datetime.datetime.timestamp(datetime.datetime.now()))+".png")