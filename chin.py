import face_recognition
import cv2
import PIL.Image
import PIL.ImageDraw
import os
from PIL import Image, ImageDraw
a="16.png"
image=cv2.imread(a)
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
print(bottom)
print(left)
print(right)
print(top)
#top,right,bottom,left =127, 140, 157, 60
#bottom=top
#top=166
#top=10
left=right
k = face_landmarks_list[0]['chin']
right=face_landmarks_list[0]['chin'][0][1]
for k1 in k :		
	if(right<k1[1]):
		right = k1[1]	
#right=227
#top,right,bottom,left =60,157,140,127
draw_shape = PIL.ImageDraw.Draw(pil_image)
im = PIL.Image.open(a)
im = im.crop((top-2, left, bottom+2, right+2))
im.save("m9.png")
print("sn")
draw_shape.rectangle([left, top, right, bottom],outline="blue")
