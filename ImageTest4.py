from PIL import Image
from google.cloud import vision
import os
import io
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="client_file.json"
client = vision.ImageAnnotatorClient()

PathSource=r"C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\PhotoClassification\Original"
PathDestination=r"C:\Users\Juan Pablo Lopez\OneDrive - Rewair A S\Documents\PhotoClassification\Destination"
PhotoNames=os.listdir(PathSource)

#nomenclatures
WebShell=["mw","tw","shl","shw","rfl","rfw","ti"]
Preforms=["prl","prw"]
Lamination=["olm","wlm"]

Main=["mw","tw"]
Shell=["shl","shw","shell"]
Return=["rfl","rfw"]
TE=["insert","te"]

OLM=["olm"]
WLM=["wlm"]

#.........................................

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
   # Here I start the first classification based on PROJECT
   if "v136" in ExtractedText:
      Path0="V136"
      c0=0
      c1=0
      c2=0
      for Nomenclature in WebShell:
          if Nomenclature in ExtractedText:
            c0=1
      for Nomenclature in Preforms:
          if Nomenclature in ExtractedText:
            c1=1
      for Nomenclature in Lamination:
          if Nomenclature in ExtractedText:
            c2=1
      # Here I start the 2nd classification based on blade part (web,preform,lamination)
      if c0!=0:
          Path1="1. Web and Shell"
          c3=0
          c4=0
          c5=0
          c6=0
          for Nomenclature in Main:
             if Nomenclature in ExtractedText:
                c3=1
          for Nomenclature in Shell:
             if Nomenclature in ExtractedText:
                c4=1
          for Nomenclature in Return:
             if Nomenclature in ExtractedText:
                c5=1
          for Nomenclature in TE:
             if Nomenclature in ExtractedText:
                c6=1
          # Here I start the 3rd classification based on blade sub-part (main,shell,return,TE) for Web and Shell
          if c3!=0:
             Path2="1. Main"
          elif c4!=0:
             Path2="2. Shell"
          elif c5!=0:
             Path2="4. Return"
          elif c6!=0:
             Path2="5. Te-insert"
      # Continuation of 2nd classification
      if c1!=0:
          Path1="2. Preforms"
          Path2="None"  # 3rd classification for Preforms is non existent
      if c2!=0:
          Path1="4. Lamination"
          Path2="None"  # 3rd classification for Preforms is non existent
          c7=0
          c8=0
          for Nomenclature in OLM:
             if Nomenclature in ExtractedText:
                  c7 = 1
          for Nomenclature in WLM:
             if Nomenclature in ExtractedText:
                  c8 = 1
          # Here is 3rd classification for Lamination
          if c7!=0:
             Path2="01. OLM"
          elif c8!=0:
             Path2="02. WLM"
   # Here is the final destination setting, depends on the existence of Path2 (3rd classification)
   picture = Image.open(PathPhoto)
   if Path2=="None":
      PathFinal= f"{PathDestination}\{Path0}\{Path1}\{Name}"
   else:
      PathFinal = f"{PathDestination}\{Path0}\{Path1}\{Path2}\{Name}"
   picture = picture.save(PathFinal)




print("Executed flawlessly")