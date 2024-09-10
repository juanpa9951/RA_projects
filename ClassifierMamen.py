def ClassifierFunction(PathSource,PathDestination,PathLost,Path_debug,Mode):
    from PIL import Image
    from google.cloud import vision
    import os
    import io
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="client_file.json"  #this is the previous key
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "client_rewair.json"
    client = vision.ImageAnnotatorClient()
    # here I define the path of the folders
    #PathSource=r"C:\Users\Juan Pablo Lopez\PhotoClassification\Original"
    #PathDestination=r"C:\Users\Juan Pablo Lopez\PhotoClassification\Destination"
    #PathLost=r"C:\Users\Juan Pablo Lopez\PhotoClassification\Destination\Lost"

    if Mode==0:   ## check for debug mode
        PathSource=Path_debug
    PhotoNames=os.listdir(PathSource) #this extracts the names of the files inside source folder
    for k1 in PhotoNames:  # this is for eliminating the files that are not photos
        if k1.endswith("jpg")== False:        #jpg   vs JPG
         Path2Remove=f"{PathSource}\{k1}"
         os.remove(Path2Remove)
    PhotoNames=os.listdir(PathSource) # this is to update the names after deleting
    print(" TOTAL OF ",len(PhotoNames)," PHOTOS UPLOADED")

    #nomenclatures for VESTAS
    WebShell=["mw","tw","shl","shw","rfl","rfw","insert","til","rf"]  #aqui retire el te
    WebShell2 = ["mw", "tw", "shl", "shw", "rfl", "rfw", "insert", "til", "rf","olm","wlm","lte","lamination"]
    Preforms=["prl","prw","stl","stw"]
    Lamination=["olm","wlm","lte","lle","lamination"]
    #sub nomenclatures for webshell
    Main=["mw","tw"]
    Shell=["shl","shw","shell"]
    Return=["rfl","rfw","rf"]
    TE=["insert","til"]# quite TE
    #sub nomenclatures for lamination
    OLM=["olm"]
    WLM=["wlm"]

    #nomenclatures for NORDEX
    PreformNordex=["prs","prp"]
    Stack=["scs","scp"]
    GlassKit=["pacais","lrgb","rj","cp","cs","lbs","vcs","vcp","lp","ls","paca","ais","raca","racais","vss","vsp","glass"]
    KitsProceso=["process","process kit"]
    #sub nomenclatures for glasskit
    Nord_concha=["-cp","-cs","- cp","- cs"]
    Nord_larguero=["-lp","-ls","-lbs"]
    Nord_viga=["vcp","vcs","vss","vsp"]
    Nord_join=["rj"]
    Nord_acabados=["-paca","-raca","-ais","-racais","-pacais"]
    Nord_lrgb=["-lrgb"]
    #sub nomenclatures for NORDEX N87.5
    N87_Shell=["-cp","-cs"]
    N87_SW1=["-sw1"]
    N87_SW2=["-sw2"]
    N87_SC1=["-sc1"]
    N87_SC3=["-sc3"]
    N87_Bonding=["xxxxx"]    #this hasnt been defined
    N87_Overlamination=["xxxxxx"] #this hasnt been defined
    N87_Stack=["xxxxxx"] #this hasnt been defined
    N87_process=["xxxxxx"] #this hasnt been defined

    #tracker for folder name creation
    Tracker=["p10","p20","p30","p40","p50","p60","p70","p80","p90","p11","p12","p13","p14","p15","p16","p17","p18","p19","ps0","pso"]

    #..................................................
    FinalLocations=["Las fotos fueron guardadas en estas ubicaciones"]  #this to initialize the final locations list


    LostCount=0
    for Name in PhotoNames: # main loop for reading all the photos in the folder
       PathPhoto = f"{PathSource}\{Name}"
       # This is where the photo is processed with AI VISION to get the extracted text
       with io.open(PathPhoto, 'rb') as image_file:
        content = image_file.read()
       image = vision.Image(content=content)
       response = client.text_detection(image=image)
       texts = response.text_annotations
       if len(texts)!=0:
           ExtractedText = texts[0].description   # aqui estaba generando el error cuando la foto no tiene ningun texto
           ExtractedText = ExtractedText.lower()
       else:
           ExtractedText = ["not any photo"]
       trip=0 #the trip is for sending photos to Lost folder


       # Here I start the first classification based on PROJECT ####################################
       if "v136" in ExtractedText:
          Path0="004. V136"
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
          Path0="002. V126"
          c0=0
          c1=0
          # c2=0
          for Nomenclature in WebShell2:
              if Nomenclature in ExtractedText:
                c0=1
          for Nomenclature in Preforms:
              if Nomenclature in ExtractedText:
                c1=1
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
              for Nomenclature in Lamination:
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
                 Path2="5. Lamination"
              else:
                 trip=1
          # Continuation of 2nd classification
          elif c1!=0:
              Path1="2. Preforms"
              Path2="None"  # 3rd classification for Preforms is non existent
          else:
              trip=1


       # Continuation of classification based on PROJECT #####################################################
       elif "v150" in ExtractedText:
          Path0="001. EV150"
          c0=0
          c1=0
          # c2=0
          for Nomenclature in WebShell2:
              if Nomenclature in ExtractedText:
                c0=1
          for Nomenclature in Preforms:
              if Nomenclature in ExtractedText:
                c1=1
          if c0!=0:
              Path1="1. Web and Shell"
              c3=0
              c4=0
              c5=0
              c6=0
              c7=0
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
              for Nomenclature in Lamination:
                 if Nomenclature in ExtractedText:
                    c7=1
              # Here I start the 3rd classification based on blade sub-part (main,shell,return,TE) for Web and Shell
              if c3!=0:
                 Path2="1. Producto final Lectra"
              elif c4!=0:
                 Path2="3. Pack and Roll"
              elif c5!=0:
                 Path2="4. Return"
              elif c6!=0:
                 Path2="5. Te-insert"
              elif c7!=0:
                 Path2="7. Lamination"
              else:
                 trip=1
          # Continuation of 2nd classification
          elif c1!=0:
              Path1="2. Preformas"
              Path2="None"  # 3rd classification for Preforms is non existent
          else:
              trip=1


       # Continuation of classification based on PROJECT #####################################################
       elif "n81" in ExtractedText:
          if ("81.5-1" in ExtractedText) or ("5x" in ExtractedText) or ("81 5-1" in ExtractedText) or ("815-1" in ExtractedText) or ("81,5-1" in ExtractedText):
              Path000="5X"
          elif ("81.5-2" in ExtractedText) or ("6x" in ExtractedText) or ("81 5-2" in ExtractedText) or ("815-2" in ExtractedText) or ("81,5-2" in ExtractedText):
              Path000 ="6X"
          else:
              trip=1
              Path000="nothing" #this wont be used since trip=1
          Path00="003. NORDEX"
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
          elif c3!=0:
              Path1="04. Kit de Proceso"
              Path2="None"
          elif c2!=0:
              Path1="03. Glass Kit"
              c4=0
              c5=0
              c6=0
              c7=0
              c8=0
              c88=0  # 88 porque no sabia el orden en que iban
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
              for Nomenclature in Nord_acabados:
                 if Nomenclature in ExtractedText:
                    c8=1
              for Nomenclature in Nord_lrgb:
                 if Nomenclature in ExtractedText:
                    c88=1
              # Here I start the 3rd classification based on blade sub-part (main,shell,return,TE) for Web and Shell
              if c4!=0:
                 Path2="1. CONCHA"
              elif c5!=0:
                 Path2="3. LARGUEROS"
              elif c6!=0:
                 Path2="4. VIGAS"
              elif c7!=0:
                 Path2="7. ROOT JOIN"
              elif c8!=0:
                 Path2="5. ACABADOS"
              elif c88!=0:
                 Path2="6. LRGB"
              else:
                 trip=1
          # Continuation of 2nd classification
          elif c3!=0:
              Path1="04. Kit de Proceso"
              Path2="None"
          else:
              trip=1
       # Continuation of classification based on PROJECT #####################################################
       elif "n87" in ExtractedText:  # HERE STARTS THE NEW N87.5 CLASSIFICATION
          Path00="003. NORDEX"
          Path000 = "N87.5"
          Path0=f"{Path00}\{Path000}"
          c0=0
          c1=0
          c2=0
          c3=0
          c4=0
          c5=0
          c6=0
          c7=0
          c8=0
          for Nomenclature in N87_Shell:
              if Nomenclature in ExtractedText:
                c0=1
          for Nomenclature in N87_SW1:
              if Nomenclature in ExtractedText:
                c1=1
          for Nomenclature in N87_SW2:
              if Nomenclature in ExtractedText:
                c2=1
          for Nomenclature in N87_SC1:
              if Nomenclature in ExtractedText:
                c3=1
          for Nomenclature in N87_SC3:
              if Nomenclature in ExtractedText:
                c4=1
          for Nomenclature in N87_Bonding:
              if Nomenclature in ExtractedText:
                c5=1
          for Nomenclature in N87_Overlamination:
              if Nomenclature in ExtractedText:
                c6=1
          for Nomenclature in N87_Stack:
              if Nomenclature in ExtractedText:
                c7=1
          for Nomenclature in N87_process:
              if Nomenclature in ExtractedText:
                c8=1
          # Here I start the 2nd classification    SO FAR 3RD SUB CLASSIFICATION NON EXISTENT
          if c0!=0:
              Path1="01. SHELL"
              Path2="None"
          elif c1!=0:
              Path1="02. SW1"
              Path2="None"
          elif c2!=0:
              Path1="03. SW2"
              Path2="None"
          elif c3!=0:
              Path1="04. SC1"
              Path2 = "None"
          elif c4!=0:
              Path1="05. SC3"
              Path2="None"
          elif c5!=0:
              Path1="06. BONDING"
              Path2="None"
          elif c6!=0:
              Path1="07. OVERLAMINATION"
              Path2="None"  # 3rd classification for Preforms is non existent
          elif c7!=0:
              Path1="08. STACK"
              Path2="None"
          elif c8!=0:
              Path1="09. PROCESS KIT"
              Path2="None"
          else:
              trip=1


       #####  NEW PROJECT CLASSIFICATION  V236
       elif ("v236" in ExtractedText) or ("chordwise" in ExtractedText) or ("ado/cfm/ups" in ExtractedText) or ("winded r" in ExtractedText) or ("chorowise" in ExtractedText):
           Path00 = "006. V236"
           Path000 = "02. Shell"
           Path0 = f"{Path00}\{Path000}"

           if ("t01" in ExtractedText) or ("to1" in ExtractedText):
               Path1 = "T_01"
               Path2 = "None"
           elif "t05" in ExtractedText or ("to5" in ExtractedText):
               Path1 = "T_05"
               Path2 = "None"
           elif "t06" in ExtractedText or ("to6" in ExtractedText):
               Path1 = "T_06"
               Path2 = "None"
           elif ("p08 lw" in ExtractedText) or ("p08 ww" in ExtractedText) or ("po8 lw" in ExtractedText) or ("po8 ww" in ExtractedText):
               Path1 = "P_08"
               Path2 = "None"
           elif ("p09 lw" in ExtractedText) or ("p09 ww" in ExtractedText) or ("po9 lw" in ExtractedText) or ("po9 ww" in ExtractedText):
               Path1 = "P_09"
               Path2 = "None"
           elif ("p10 lw" in ExtractedText) or ("p10 ww" in ExtractedText) or ("p1o lw" in ExtractedText) or ("p1o ww" in ExtractedText):
               Path1 = "P_10"
               Path2 = "None"
           elif ("p11 lw" in ExtractedText) or ("p11 ww" in ExtractedText):
               Path1 = "P_11"
               Path2 = "None"
           else:
               trip = 1
               Path1='nothing/'
               Path2='nothing/'

       ######  no project name detected
       else:
          trip=1
          Path0 ='nothing/'
          Path1='nothing/'
          Path2='nothing/'

       if Mode==0:   ### If debug mode active then print the paths it found
           print('\n photo: ',Name)
           print(ExtractedText)
           print(Path0,'+',Path1,'+',Path2)

       # Here is the final destination setting, depends on trip=0 and trip2=1 and the existence of Path2 (3rd classification)
       trip2=0  #this trip is for verifying the label has the info complete to create a folder
       if trip==0:   #Here is necessary to sort out the false P+number in order to extract the odf number (folder name)
           for track in Tracker:
               if track in ExtractedText:
                   Pos0=ExtractedText.find(track) # possible position of the P+number
                   ODF=ExtractedText[Pos0 - 4:Pos0] # here I extract the possible odf number
                   ODF=ODF.replace(" ","") # here to remove empty spaces
                   if ODF.isnumeric()==True: # here I verify if ODF is in fact a number
                       Pos = Pos0 # here I extract the position of the P+number
                       trip2=1
       if (trip==0) and (trip2==1):
           FolderName = ExtractedText[Pos - 4:Pos]  # here I extract odf number which is the folder name
           FolderName = "".join(c for c in FolderName if c.isalnum())
           Prefix=ExtractedText[Pos+3:Pos+6]
           if Prefix[0]!='s':     ### this is to correct the name when PXX is >=100   e.g p100, p110, p120
               Prefix = ExtractedText[Pos + 4:Pos + 7]
           Prefix = "".join(c for c in Prefix if c.isalnum())  # this is to extract only alfa numeric values
           if Path2=="None":
              FolderPath = f"{PathDestination}\{Path0}\{Path1}\{FolderName}"
              if not os.path.exists(FolderPath):
                  os.mkdir(FolderPath)
              Name2=Prefix+"_"+Name
              PathFinal= f"{FolderPath}\{Name2}"
           else:
              FolderPath = f"{PathDestination}\{Path0}\{Path1}\{Path2}\{FolderName}"
              if not os.path.exists(FolderPath):
                  os.mkdir(FolderPath)
              Name2 = Prefix + "_" + Name
              PathFinal= f"{FolderPath}\{Name2}"
       else:
           PathFinal=f"{PathLost}\{Name}"
           LostCount +=1
       picture = Image.open(PathPhoto)
       picture = picture.save(PathFinal)
       FinalLocations.append(PathFinal)
       print(round((len(FinalLocations)-1)/len(PhotoNames)*100,2),"% Progress, Photo classified to ",PathFinal.replace("Users\Maria del Carmen\OneDrive - Rewair A S\Inspección - Fotos",""))  # here I print the progress and final destinations
       if Mode==1:   ## if mode is normal then empty the source folder
        Path2Remove=f"{PathSource}\{Name}"  # here I empty the original folder
        os.remove(Path2Remove)
    print("RESULTS: ",len(FinalLocations)-1-LostCount, "PHOTOS CLASSIFIED(",(len(FinalLocations)-1-LostCount)/len(PhotoNames)*100,"%) and ", LostCount, "PHOTOS LOST")
    return FinalLocations