import cv2
import sys

img = cv2.imread('./sample1.jpg', cv2.IMREAD_COLOR)
if img is None:
  sys.exit('画像が読み込めませんでした。')

cv2.imshow('Display window', img)

size = (int(img.shape[1]/10), int(img.shape[0]/10))

dst1 = cv2.resize(img, size, interpolation=cv2.INTER_NEAREST)

dst2 = cv2.resize(dst1, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_NEAREST)

cv2.imshow('Display window: mozaic', dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
