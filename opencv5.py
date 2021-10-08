import cv2
import sys
import numpy as np

img = cv2.imread('./sample1.jpg', cv2.IMREAD_COLOR)
if img is None:
  sys.exit('画像が読み込めませんでした。')

height, width = img.shape[:2]
print(f'height:{height}, width:{width}')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
blue, green, red = cv2.split(img)
blue = (blue[:,:]*0.4).astype(np.uint8)
green = (green[:,:]*0.7).astype(np.uint8)
sepia = cv2.merge((blue,green,red))

#sepia = cv2.applyColorMap(img, cv2.COLORMAP_PINK)

cv2.imshow('Display window: sepia', sepia)
cv2.waitKey(0)
cv2.destroyAllWindows()
