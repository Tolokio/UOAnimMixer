import os
from PIL import Image
import shutil

folderIn = r'ANIM1'
folderOn = r'ANIM2'
folderOut = r'OUTPUT'
files = os.listdir(folderOn)
times=0

print("Starting")
def insert_image(main_image_path, insert_image_path, save_path, centerx, centery):
  main_image = Image.open(main_image_path).convert('RGBA')
  insert_image = Image.open(insert_image_path).convert('RGBA')
  main_width, main_height = main_image.size
  insert_width, insert_height = insert_image.size
  x = centerx
  y = centery
  y = int(main_height) + y - insert_height

  main_image.alpha_composite(insert_image, (x, y))
  main_image.save(save_path)

for file in files:
    times +=1
    if file.endswith(".png"):
        search_framepbmp = file
        search_framep= search_framepbmp.replace(".png", "")
        search_frame= search_framep.replace("_", ":")
        with open(r'ANIM1\liste.txt', 'r') as posicionest:
            for i, line in enumerate(posicionest):
                if search_frame in line:
                    n_linea=i + 1
                if n_linea == i:
                    CenterX=line.strip()
                    Xt=CenterX.replace("CenterX:", "")
                elif n_linea == i - 1:
                    CenterY=line.strip()
                    Yt=CenterY.replace("CenterY:", "")
                    n_linea=""
                    break
        with open(r'ANIM2\liste.txt', 'r') as posicionesw:
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

        X= int(Xt) - int(Xw)
        Y= -int(Yw) + int(Yt)
                
        WEREABLE = os.path.join(folderOn, search_framepbmp) 
        TEMPLATE = os.path.join(folderIn, search_framepbmp)
        OUTPUT = os.path.join(folderOut, search_framepbmp)
        print(f"Doing {times}/1050")
        
        insert_image(TEMPLATE, WEREABLE, OUTPUT, X, Y)
        print(f"Doing {times}/1050")
			
shutil.copy2('ANIM1\liste.txt', 'OUTPUT\liste.txt')
print("Copied Liste.txt")
#####
