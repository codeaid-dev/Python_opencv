import cv2
import sys

img = cv2.imread('./sample1.jpg', cv2.IMREAD_GRAYSCALE)
if img is None:
  sys.exit('画像が読み込めませんでした。')

cv2.imshow('Display window: gray', img)
k = cv2.waitKey(0)
if k == ord('s'):
  cv2.imwrite('sample2.jpg', img)
cv2.destroyAllWindows()
