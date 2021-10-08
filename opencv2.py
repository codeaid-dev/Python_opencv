import cv2
import sys

img1 = cv2.imread('./sample1.jpg', cv2.IMREAD_COLOR)
if img1 is None:
  sys.exit('画像が読み込めませんでした。')

img2 = cv2.imread('./sample1.jpg', cv2.IMREAD_GRAYSCALE)
if img2 is None:
  sys.exit('画像が読み込めませんでした。')

cv2.imshow('Display window', img1)
cv2.imshow('Display window: gray', img2)
k = cv2.waitKey(0)
cv2.destroyAllWindows()
