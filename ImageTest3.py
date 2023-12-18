from PIL import Image
from google.cloud import vision
import os
import io
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="client_file.json"
client = vision.ImageAnnotatorClient()

PathSource=r"C:\Users\Juan Pablo Lopez\PycharmProjects\ProjectJP\OriginalPhoto"
PathDestination=r"C:\Users\Juan Pablo Lopez\PycharmProjects\ProjectJP\Photos"
PhotoNames=os.listdir(PathSource)
for Name in PhotoNames:
 PathPhoto = f"{PathSource}\{Name}"

 with io.open(PathPhoto, 'rb') as image_file:
  content = image_file.read()
 image = vision.Image(content=content)
 response = client.text_detection(image=image)
 texts = response.text_annotations
 WholeText = texts[0].description
 WholeText = WholeText.lower()

 if "v136" in WholeText:
  picture = Image.open(PathPhoto)
  Path4= f"{PathDestination}\{Name}"
  picture = picture.save(Path4)

print("Executed")