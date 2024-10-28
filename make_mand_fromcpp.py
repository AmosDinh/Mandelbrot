import csv
import numpy as np
from PIL import Image
import pandas as pd
import threading
img_temp = []
with open('test.csv','r',newline='\n') as f:
    for i,row in enumerate(csv.reader(f,delimiter=',')):
        img_temp.append(row)
        


img = np.zeros((len(img_temp[0]), len(img_temp), 3), dtype=np.uint8)

for x in range(0,len(img_temp)):
    print(x)
    for y in range(0,len(img_temp[0])):
        k = int(img_temp[y][x])
        #img[y][x] = [(k/2)*200,(k/8)*255,(k/20)*255]
        img[y][x] = [0,0,(k/19)*255]
        # img.itemset((y,x,2), (k/20)*255)
        # img.itemset((y,x,1), (k/8)*255)
        # img.itemset((y,x,0), (k/2)*200)
print(img)
image = Image.fromarray(img,'RGB')
image.show()

