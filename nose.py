import face_recognition
import cv2
import PIL.Image
import PIL.ImageDraw
import os
from PIL import Image, ImageDraw

image=cv2.imread("16.png")
pil_image = PIL.Image.fromarray(image)
face_landmarks_list = face_recognition.face_landmarks(image)
d = ImageDraw.Draw(pil_image)
print(face_landmarks_list)
k = face_landmarks_list[0]['nose_bridge']
left =face_landmarks_list[0]['nose_bridge'][0][1]
for k1 in k :
    if(left>k1[1]):
        left = k1[1]

k = face_landmarks_list[0]['nose_tip']
right=face_landmarks_list[0]['nose_tip'][0][1]
top =bottom= face_landmarks_list[0]['nose_tip'][0][0]
for k1 in k :
	if(top>k1[0]):
		top=k1[0]
	if(bottom<k1[0]):
		bottom=k1[0]	
	if(right<k1[1]):
		right = k1[1]
print("ss")
#top,right,bottom,left =98, 613, 284, 428
#top,right,bottom,left =80,127,117,60
draw_shape = PIL.ImageDraw.Draw(pil_image)
im = PIL.Image.open("16.png")
im = im.crop((left-2, top-2, right+2, bottom+2))
im.save("m9.jpg")
print("sn")
draw_shape.rectangle([left, top, right, bottom],outline="blue")
