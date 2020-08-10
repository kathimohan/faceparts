import face_recognition
import cv2
import PIL.Image
import PIL.ImageDraw
import os
from PIL import Image, ImageDraw
import face_recognition
a="kn.png"
# Load the jpg file into a numpy array
image = face_recognition.load_image_file(a)

# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image)

#print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

# Create a PIL imagedraw object so we can draw on the picture
pil_image = Image.fromarray(image)
d = ImageDraw.Draw(pil_image)
print(face_landmarks_list)
k = face_landmarks_list[0]['left_eye']
top =bottom=face_landmarks_list[0]['left_eye'][0][1]
left =right= face_landmarks_list[0]['left_eye'][0][0]
for k1 in k :
	if(left>k1[0]):
		left=k1[0]
	if(right<k1[0]):
		right=k1[0]
	if(top>k1[1]):
		top = k1[1]
	if(bottom<k1[1]):
		bottom = k1[1]
print(top,right,left,bottom)
image=cv2.imread(a)
draw_shape = PIL.ImageDraw.Draw(pil_image)
im = PIL.Image.open(a)
im = im.crop((left-2, top-2, right+2,bottom+2))
im.save("m5.png")
draw_shape.rectangle([left, top, right, bottom],outline="blue")

