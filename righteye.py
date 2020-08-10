import face_recognition
import cv2
import PIL.Image
import PIL.ImageDraw
import os
from PIL import Image, ImageDraw
import face_recognition
a="k.png"
# Load the jpg file into a numpy array
image = face_recognition.load_image_file(a)

# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image)

#print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

# Create a PIL imagedraw object so we can draw on the picture
pil_image = Image.fromarray(image)
d = ImageDraw.Draw(pil_image)
print(face_landmarks_list)
k = face_landmarks_list[0]['right_eye']
left =right=face_landmarks_list[0]['right_eye'][0][1]
top =bottom= face_landmarks_list[0]['right_eye'][0][0]
for k1 in k :
	if(top>k1[0]):
		top=k1[0]
	if(bottom<k1[0]):
		bottom=k1[0]
	if(left>k1[1]):
		left = k1[1]
	if(right<k1[1]):
		right = k1[1]
print(left,right,top,bottom)
#52 69 124 160
#'right_eye': [(124, 65), (134, 52), (149, 52), (160, 61), (151, 68), (136, 69)]
image=cv2.imread(a)
pil_image = PIL.Image.fromarray(image)
#top,right,bottom,left =98, 613, 284, 428
#top,right,bottom,left =138,581,148,475
draw_shape = PIL.ImageDraw.Draw(pil_image)
im = PIL.Image.open(a)
#im = im.crop((left-2, top-2, right+2, bottom+2))
im = im.crop((top-2, left-2, bottom+2,right+2))
im.save("m6.png")
draw_shape.rectangle([left, top, right, bottom],outline="blue")

