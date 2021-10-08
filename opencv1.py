import cv2
import sys

img = cv2.imread('./sample1.jpg', cv2.IMREAD_COLOR)
if img is None:
  sys.exit('画像が読み込めませんでした。')

cv2.imshow('Display window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
