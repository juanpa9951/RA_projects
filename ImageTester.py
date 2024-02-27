from google.cloud import vision
import os
import io
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="client_rewair.json"
client = vision.ImageAnnotatorClient()
PathSource=r"C:\Users\Juan Pablo Lopez\PycharmProjects\ProjectJP\ImageTester"
PhotoNames=os.listdir(PathSource)
count=0
FinalLocation=["Inicio"]
for Name in PhotoNames:
   PathPhoto = f"{PathSource}\{Name}"
   # This is where the photo is processed with AI VISION to get the extracted text
   with io.open(PathPhoto, 'rb') as image_file:
    content = image_file.read()
   image = vision.Image(content=content)
   response = client.text_detection(image=image)
   texts = response.text_annotations
   ExtractedText = texts[0].description
   ExtractedText = ExtractedText.lower()
   count=count+1
   print("Image number",count)
   print(ExtractedText)
   FinalLocation.append(ExtractedText)

print("executed succesfully")
print(FinalLocation)