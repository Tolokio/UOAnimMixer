#animmixer3->This code mix two wereables. To run this u need A folder with the body frames, and two folders with the two wereables.
import os
from PIL import Image

folderIn = r'TEMPLATE'
folderOn = r'WEREABLE'
folderOn2 = r'WEREABLE2'
folderOut = r'OUTPUT'
files = os.listdir(folderOn)
times=0

print("comienza")
def insert_image(main_image_path, insert_image_path, insert_image_path2, save_path, centerx, centery, centerx2, centery2):
  main_image = Image.open(main_image_path).convert('RGBA')
  insert_image = Image.open(insert_image_path).convert('RGBA')
  insert_image2 = Image.open(insert_image_path2).convert('RGBA')
  main_width, main_height = main_image.size
  insert_width, insert_height = insert_image.size
  insert_width2, insert_height2 = insert_image2.size
  
  x = centerx
  y = centery
  x2 = centerx2
  y2 = centery2
  y = int(main_height) + y - insert_height
  y2= int(main_height) + y2 - insert_height2
  x3= x2 - x
  y3= y2 - y

  for xr in range(insert_image2.width):
    for yr in range(insert_image2.height):
      pixel = insert_image2.getpixel((xr, yr))
      if pixel[3] != 0:
        xx= xr+x3
        yy= yr+y3
        if (0 <= xx <= int(insert_image.width - 1)) and (0 <= yy <= int(insert_image.height - 1)):
            insert_image.putpixel((int(xx), int(yy)), (0, 0, 0, 0))

  # Guarda la imagen de destino
  insert_image.save(save_path)
  
  
  #print(f"COLOCADO, {xx} {yy}")

  # inserta la imagen en la imagen principal
  #main_image.paste(insert_image, (x, y))
  #insert_image.alpha_composite(insert_image2, (x3, y3))
  # guarda la imagen resultante


print("pasa inicio")
#LOOP POR TODOS LOS FILES DE LA CARPETA TEMPLATE
for file in files:
    times +=1
    #print("buscando file")
    if file.endswith(".png"): #si es un png
        #seteamos variables necesarias.
        search_framepbmp = file  # eg "1_1.bmp" or "0_4.bmp"
        search_framep= search_framepbmp.replace(".png", "") # eg "1_1" or "0_4"
        search_frame= search_framep.replace("_", ":") # eg "1:1" or "0:4"
        #print(f"search_frame, {search_frame} {search_framepbmp} {search_framep}")
        
		# buscamos posiciones del TEMPLATE
        with open(r'D:\uomixer\TEMPLATE\liste.txt', 'r') as posicionest:
            for i, line in enumerate(posicionest):
                if search_frame in line:
                    n_linea=i + 1
                if n_linea == i:
                    CenterX=line.strip()
                    #print(f"centerx   , {CenterX}")
                    Xt=CenterX.replace("CenterX:", "") # deja solo el valor numerico
                elif n_linea == i - 1:
                    CenterY=line.strip()
                    #print(f"centerY   , {CenterY}")
                    Yt=CenterY.replace("CenterY:", "") # deja solo el valor numerico
                    n_linea=""
                    break
        # buscamos posiciones del Wereable
        with open(r'D:\uomixer\WEREABLE\liste.txt', 'r') as posicionesw:
            for ii, line in enumerate(posicionesw):
                if search_frame in line:
                    n_linea=ii + 1
                if n_linea == ii:
                    CenterX=line.strip()
                    Xw=CenterX.replace("CenterX:", "")
                if n_linea == ii - 1:
                    CenterY=line.strip()
                    Yw=CenterY.replace("CenterY:", "")
                    n_linea=""
                    break
        with open(r'D:\uomixer\WEREABLE2\liste.txt', 'r') as posicionesww:
            for iii, line in enumerate(posicionesww):
                if search_frame in line:
                    n_linea=iii + 1
                if n_linea == iii:
                    CenterX=line.strip()
                    Xww=CenterX.replace("CenterX:", "")
                if n_linea == iii - 1:
                    CenterY=line.strip()
                    Yww=CenterY.replace("CenterY:", "")
                    n_linea=""
                    break
        #calculamos las posciones
         
        X= int(Xt) - int(Xw)
        Y= -int(Yw) + int(Yt)

        #gets position of second wereable
        X2= int(Xt) - int(Xww)
        Y2= -int(Yww) + int(Yt)


        
        print(f"X Y, {X} {Y}")                  
        #llamamos a la función para insertar con los datos q tenemos.
        WEREABLE = os.path.join(folderOn, search_framepbmp)  # ruta al primer wereable.
        WEREABLE2 = os.path.join(folderOn2, search_framepbmp)  # ruta al segundo wereable
        TEMPLATE = os.path.join(folderIn, search_framepbmp)  # ruta a la carpeta + archivo.bmp DONDE va  ser insertado
        OUTPUT = os.path.join(folderOut, search_framepbmp)  # ruta a la carpeta + archivo.bmp donde se va a GUARDAR.
        
        print(f"Processing {WEREABLE}/1050")
        print(f"Processing {times}/1050")
        
        insert_image(TEMPLATE, WEREABLE, WEREABLE2, OUTPUT, X, Y, X2, Y2) #funcion para insertar imagen
        
        #break
			

#####
