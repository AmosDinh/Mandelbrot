import datetime

import numpy as np
from PIL import Image
#DIN A4 ist 21 x 29,7
# Höhe definiert 
import decimal
decimal.getcontext().prec = 100

def main():
    max_iter = 20
    res_h = 4

    # im_x1 = -1.7
    # im_x2 = 1.7
    # re_x1 = -2.4
    # re_x2 = 1.6
    im_x1 = 0.16111111111
    im_x2 = 0.16111111111111
    re_x1 = 0.20111111111
    re_x2 = 0.20111111111111
   
    res_w = res_h * ( abs(abs(re_x1)-abs(re_x2)) / abs(abs(im_x1)-abs(im_x2)) )
    res_w = int(res_w)

    img = np.zeros((res_h, res_w, 3), dtype=np.uint8)
    x = 0
    y = 0
    abs_h = abs(im_x1)+abs(im_x2)
    abs_w= abs(re_x1)+abs(re_x2)
    h_v = im_x1
    w_v = re_x1
    for temp_im in range(0,res_h):
       
        x = 0
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
                    print(k)
                    #img[y][x] = [0,0,(k/max_iter)*255]
                    img.itemset((y,x,2), (k/max_iter)*255)
                    img.itemset((y,x,1), (k/8)*255)
                    img.itemset((y,x,0), (k/2)*200)

    #  img.itemset((y,x,2), (k/max_iter)*255)
    #                 img.itemset((y,x,1), (k/8)*255)
    #                 img.itemset((y,x,0), (k/2)*200)

                    break

            x += 1
        
        y += 1
    
    image = Image.fromarray(img,'RGB')
    image.show()

main()
#image.save("mandelbrot"+str(datetime.datetime.timestamp(datetime.datetime.now()))+".png")

"""
cool settings

  im_x1 = 0.1211111
    im_x2 = 0.12111111
    re_x1 = 0.2011111
    re_x2 = 0.20111111
    img.itemset((y,x,2), (k/max_iter)*255)
    img.itemset((y,x,1), (k/8)*255)
    img.itemset((y,x,0), (k/2)*200)

"""