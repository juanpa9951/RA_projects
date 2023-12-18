from PIL import Image
from google.cloud import vision
import os
import io
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="client_file.json"
client = vision.ImageAnnotatorClient()
# here I define the path of the folders
PathSource=r"C:\Users\Juan Pablo Lopez\PhotoClassification\Original"
PathDestination=r"C:\Users\Juan Pablo Lopez\PhotoClassification\Destination"
PathLost=r"C:\Users\Juan Pablo Lopez\PhotoClassification\Destination\Lost"
PhotoNames=os.listdir(PathSource) #this extracts the names of the files inside source folder
for k1 in PhotoNames:  # this is for eliminating the files that are not photos
    if k1.endswith("jpg")== False:
     Path2Remove=f"{PathSource}\{k1}"
     os.remove(Path2Remove)
PhotoNames=os.listdir(PathSource) # this is to update the names after deleting
#nomenclatures for VESTAS
WebShell=["mw","tw","shl","shw","rfl","rfw","te","insert","lle","lte","rfl","rfw","til"]
Preforms=["prl","prw","stl","stw"]
Lamination=["olm","wlm","lte"]
#sub nomenclatures for webshell
Main=["mw","tw"]
Shell=["shl","shw","shell"]
Return=["rfl","rfw"]
TE=["insert","te","til"]
#sub nomenclatures for lamination
OLM=["olm"]
WLM=["wlm"]
#nomenclatures for NORDEX
PreformNordex=["prs","prp"]
Stack=["scs","scp"]
GlassKit=["pacais","lrgb","rj","cp","cs","lbs","vcs","vcp","lp","ls","paca","ais","raca","racais","vss","vsp"]
KitsProceso=["pk"]
#sub nomenclatures for glasskit
Nord_concha=["cp","cs"]
Nord_larguero=["lp","ls","lbs"]
Nord_viga=["vcp","vcs","vss","vsp"]
Nord_join=["rj"]
#tracker for folder name creation
Tracker=["p10","p20","p30","p40","p50","p60","p70","p80","p90","p10"]
#..................................................
FinalLocations=["Inicio"]  #this to initialize the final locations list
for Name in PhotoNames: # main loop for reading all the photos in the folder
   PathPhoto = f"{PathSource}\{Name}"
   # This is where the photo is processed with AI VISION to get the extracted text
   with io.open(PathPhoto, 'rb') as image_file:
    content = image_file.read()
   image = vision.Image(content=content)
   response = client.text_detection(image=image)
   texts = response.text_annotations
   ExtractedText = texts[0].description
   ExtractedText = ExtractedText.lower()
   trip=0 #the trip is for sending photos to Lost folder
   # Here I start the first classification based on PROJECT ####################################
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
          else:
             trip=1
      # Continuation of 2nd classification
      elif c1!=0:
          Path1="2. Preforms"
          Path2="None"  # 3rd classification for Preforms is non existent
      elif c2!=0:
          Path1="4. Lamination"
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
          else:
             trip=1
   # Continuation of classification based on PROJECT #########################################
   elif "v126" in ExtractedText:
      Path0="V126"
      c0=0
      c1=0
      for Nomenclature in WebShell:
          if Nomenclature in ExtractedText:
            c0=1
      for Nomenclature in Preforms:
          if Nomenclature in ExtractedText:
            c1=1
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
          # Here I start the 3rd classification based on blade sub-part (main,shell,return,TE) for Web and Shell
          if c3!=0:
             Path2="1. Main"
          elif c4!=0:
             Path2="2. Shell"
          elif c5!=0:
             Path2="4. Return"
          else:
             trip=1
      # Continuation of 2nd classification
      elif c1!=0:
          Path1="2. Preforms"
          Path2="None"  # 3rd classification for Preforms is non existent
      elif c2!=0:
          Path1="4. Lamination"
          Path2="None"  # 3rd classification for Preforms is non existent
      else:
          trip=1
   # Continuation of classification based on PROJECT #####################################################
   elif "ev150" in ExtractedText:
      Path0="EV150"
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
             Path2="1. Producto final Lectra"
          elif c4!=0:
             Path2="3. Pack and Roll"
          elif c5!=0:
             Path2="4. Return"
          elif c6!=0:
             Path2="5. Te-insert"
          else:
             trip=1
      # Continuation of 2nd classification
      elif c1!=0:
          Path1="2. Preforms"
          Path2="None"  # 3rd classification for Preforms is non existent
      elif c2!=0:
          Path1="4. Lamination"
          Path2="None"  # 3rd classification for Preforms is non existent
      else:
          trip=1
   # Continuation of classification based on PROJECT #####################################################
   elif "n81" in ExtractedText:
      if "81.5-1" in ExtractedText:
          Path000="5X"
      elif "81.5-2" in ExtractedText:
          Path000 ="6X"
      else:
          trip=1
      Path00="NORDEX"
      Path0=f"{Path00}\{Path000}"
      c0=0
      c1=0
      c2=0
      c3=0
      for Nomenclature in PreformNordex:
          if Nomenclature in ExtractedText:
            c0=1
      for Nomenclature in Stack:
          if Nomenclature in ExtractedText:
            c1=1
      for Nomenclature in GlassKit:
          if Nomenclature in ExtractedText:
            c2=1
      for Nomenclature in KitsProceso:
          if Nomenclature in ExtractedText:
            c3=1
      # Here I start the 2nd classification based on blade part (preform, stack, glasskit, kit de proceso)
      if c0!=0:
          Path1="01. Preform"
          Path2="None"  # 3rd classification for Preforms is non existent
      elif c1!=0:
          Path1="02. Stack"
          Path2="None"  # 3rd classification for Preforms is non existent
      elif c2!=0:
          Path1="03. Glass Kit"
          c4=0
          c5=0
          c6=0
          c7=0
          for Nomenclature in Nord_concha:
             if Nomenclature in ExtractedText:
                c4=1
          for Nomenclature in Nord_larguero:
             if Nomenclature in ExtractedText:
                c5=1
          for Nomenclature in Nord_viga:
             if Nomenclature in ExtractedText:
                c6=1
          for Nomenclature in Nord_join:
             if Nomenclature in ExtractedText:
                c7=1
          # Here I start the 3rd classification based on blade sub-part (main,shell,return,TE) for Web and Shell
          if c4!=0:
             Path2="1. CONCHA"
          elif c5!=0:
             Path2="3. LARGUEROS"
          elif c6!=0:
             Path2="4. VIGAS"
          elif c7!=0:
             Path2="5. ROOT JOIN"
          else:
             trip=1
      # Continuation of 2nd classification
      elif c3!=0:
          Path1="04. Kit de Proceso"
          Path2="None"
      else:
          trip=1

   else:
      trip=1
   # Here is the final destination setting, depends on trip=0 and the existence of Path2 (3rd classification)
   if trip==0:
       for track in Tracker:    # here I extract the name of the folder
           if track in ExtractedText:
               Pos = ExtractedText.find(track)
       FolderName = ExtractedText[Pos - 4:Pos]
       Prefix=ExtractedText[Pos+3:Pos+6]
       if Path2=="None":
          FolderPath = f"{PathDestination}\{Path0}\{Path1}\{FolderName}"
          if not os.path.exists(FolderPath):
              os.mkdir(FolderPath)
          Name=Prefix+"_"+Name
          PathFinal= f"{FolderPath}\{Name}"
       else:
          FolderPath = f"{PathDestination}\{Path0}\{Path1}\{Path2}\{FolderName}"
          if not os.path.exists(FolderPath):
              os.mkdir(FolderPath)
          Name = Prefix + "_" + Name
          PathFinal= f"{FolderPath}\{Name}"
   else:
       PathFinal=f"{PathLost}\{Name}"
   picture = Image.open(PathPhoto)
   picture = picture.save(PathFinal)
   FinalLocations.append(PathFinal)

print("Executed flawlessly")
for h in FinalLocations:   # here I print the final destinations
   print(h.replace("Users\Juan Pablo Lopez\PhotoClassification\Destination",""))
for k in PhotoNames:  # here I empty the original folder
   Path2Remove=f"{PathSource}\{k}"
   os.remove(Path2Remove)