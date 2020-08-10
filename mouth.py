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
k = face_landmarks_list[0]['top_lip']
tleft=tright=face_landmarks_list[0]['top_lip'][0][1]
#left=right=face_landmarks_list[0]['nose_tip'][0][1]
ttop =tbottom= face_landmarks_list[0]['top_lip'][0][0]
for k1 in k :
	if(ttop>k1[0]):
		ttop=k1[0]
	if(tbottom<k1[0]):
		tbottom=k1[0]	
	if(tright<k1[1]):
		tright = k1[1]
	if(tleft<k1[1]):
		tleft = k1[1]

k = face_landmarks_list[0]['bottom_lip']
left=right=face_landmarks_list[0]['bottom_lip'][0][1]
#left=right=face_landmarks_list[0]['nose_tip'][0][1]
top =bottom= face_landmarks_list[0]['bottom_lip'][0][0]
for k1 in k :
	if(top>k1[0]):
		top=k1[0]
	if(bottom<k1[0]):
		bottom=k1[0]	
	if(right<k1[1]):
		right = k1[1]
	if(left<k1[1]):
		left= k1[1]
left=min(tleft,left)
right=max(tright,right)
top=min(ttop,top)
bottom=max(tbottom,bottom)
#top,right,bottom,left =127, 140, 157, 60

#top,right,bottom,left =60,157,140,127
draw_shape = PIL.ImageDraw.Draw(pil_image)
im = PIL.Image.open("16.png")
im = im.crop((top-4, left-4, bottom+4, right+4))
im.save("m9.jpg")
print("sn")
draw_shape.rectangle([left, top, right, bottom],outline="blue")
