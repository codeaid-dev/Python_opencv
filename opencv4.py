import cv2
import sys
import numpy as np

img = cv2.imread('./sample1.jpg', cv2.IMREAD_COLOR)
if img is None:
  sys.exit('画像が読み込めませんでした。')

height, width = img.shape[:2]
print(f'height:{height}, width:{width}')

zeros = np.zeros((height,width), img.dtype)

blue, green, red = cv2.split(img)
img_g = cv2.merge((zeros,green,zeros))

cv2.imshow('Display window: green', img_g)
cv2.waitKey(0)
cv2.destroyAllWindows()
