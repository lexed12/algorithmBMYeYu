import cv2
import numpy as np
#from PIL import Image

print("Hello, World!")




image = cv2.cvtColor(cv2.imread('logo.jpg'), cv2.COLOR_BGR2GRAY)
rows, height = image.shape
channels = 1


Nc = (rows//8*height//8)*channels #количество встраиваемых бит


def segdiv(image):
    seg = []
    block_size = 8
    rows, height = image.shape
    print(height, rows, channels)
    Nc = (rows//8*height//8)*channels #количество встраиваемых бит
    for c in range(0, channels):
        for x in range(0, rows, block_size):
            for y in range(0, height, block_size):
                end_x = x + block_size
                end_y = y + block_size
                
                # Проверяем, чтобы блок не выходил за границы изображения
                if end_x <= rows and end_y <= height:
                    seg.append(image[x:end_x, y:end_y])
    return seg

#преобраззование в float32 подавал в uint8 выход тоже в uint8
def dct_blocks(seg):
    dct_seg = []
    seg_float32 = [np.array(block, dtype=np.float32) for block in seg]
    dct_seg = [cv2.dct(block/255.0) for block in seg_float32]
    return dct_seg

seg = segdiv(image)
dct_blocks(seg)













cv2.imshow('logo', image)
cv2.waitKey(0)