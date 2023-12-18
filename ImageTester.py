from google.cloud import vision
import os
import io
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="client_file.json"
client = vision.ImageAnnotatorClient()
PathSource=r"C:\Users\Juan Pablo Lopez\PycharmProjects\ProjectJP\ImageTester"
PhotoNames=os.listdir(PathSource)
count=0
FinalLocation=["Inicio"]
Tracker=["p10","p20","p30","p40","p50","p60","p70","p80","p90","p10"]
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
   #print("Image number",count)
   #print(ExtractedText)
   FinalLocation.append(ExtractedText)
   for track in Tracker:
      if track in ExtractedText:
         Pos=ExtractedText.find(track)
   FolderName=ExtractedText[Pos-4:Pos+6]+"_"+str(count)
   print("the folder #",count," is called ",FolderName)

print("executed succesfully")
print(FinalLocation)