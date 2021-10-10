import cv2
import sys

img = cv2.imread('./face1.jpg', cv2.IMREAD_COLOR)
if img is None:
  sys.exit('画像が読み込めませんでした。')

filename = 'C:/Users/birdy/anaconda3/pkgs/libopencv-4.0.1-hbb9e17c_0/Library/etc/haarcascades/haarcascade_frontalface_default.xml'
cascade = cv2.CascadeClassifier(filename)
if cascade is None:
  sys.exit('ファイルが見つかりません。')

face = cascade.detectMultiScale(img)

if len(face) > 0:
  for r in face:
    x, y = r[0:2]
    width, height = r[0:2] + r[2:4]
    cv2.rectangle(img, (x,y), (width,height), (255,255,0), thickness=2)
else:
    print('顔が見つかりません。')

cv2.imshow('Display window: detect face', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
