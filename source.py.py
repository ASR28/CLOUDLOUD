import pprint
import boto3
from PIL import Image,ImageDraw
rek =boto3.client('rekognition')
with open('download.jpg' , 'rb') as f:
image_bytes = f.read()
response = rek.detect_labels(Image={'Bytes':image_bytes})
pprint.pprint(response)
###################
response = rek.detect_faces(Image={'Bytes':image_bytes},Attributes=['ALL'])
pprint.pprint(response)
####################
src = Image.open('download.jpg')
draw1 = ImageDraw.Draw(src)
width , height = src.size
img = Image.new("RGB",src.size)
draw = ImageDraw.Draw(img)
img.paste(src , (0,0))
for face in response["FaceDetails"]:
for point in face["Landmarks"]:
x=point["X"] * width
y=point["Y"] * height
r = 5
draw.ellipse((x-r,y-r,x+r,y+r),fill="red")
img.save('download-rek.jpg')
#######################################
with open('pikest.jpg','rb') as f:
image_bytes = f.read()
response = rek.detect_text(Image={'Bytes':image_bytes})
pprint.pprint(response)
##########################################
src = Image.open('pikest.jpg')
draw1=ImageDraw.Draw(src)
width,height=src.size
img=Image.new("RGB",src.size)
draw = ImageDraw.Draw(img)
img.paste(src , (0,0))
for text in response["TextDetections"]:
points = [(point['X']*width , point['Y']*height)for point in text["Geometry"]["Polygon"]]
points.append(points[0])
draw.line(points , fill="red",width=9)

import csv import boto3
with open('credentials.csv' , 'r') as input: next(input)
reader = csv.reader(input) for line in reader:
access_key_id = line[2] secret_access_key = line[3]
photo = 'mix.jpg'
client = boto3.client('rekognition' , aws_access_key_id = access_key_id , aws_secret_access_key = secret_access_key)
with open(photo , 'rb') as source_image: source_bytes = source_image.read()
response = client.recognize_celebrities(Image={'S3Object':{'Bucket':'umangpincha','Name':photo}} )
for key, value in response.items(): if key=='CelebrityFaces':
for people in value: print (people)
img.save("pikest-rek.jpg")
