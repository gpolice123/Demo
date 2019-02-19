from yolo import YOLO
from PIL import Image
import cv2
import time

cap = cv2.VideoCapture(0)
time.sleep(1)
ret,frame=cap.read()
#cv2.imwrite('led.jpg',frame)
cap.release()

image = Image.open('led.jpg')
image.show()

yolo = YOLO()
r_image = yolo.detect_image(image)
r_image.show()
r_image.save('led_find.jpg')
