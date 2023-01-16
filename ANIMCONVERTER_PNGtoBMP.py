import os
from PIL import Image

folderM = r'ACONVERTER'
files = os.listdir(folderM)

print("pasa inicio")
for file in files:
    if file.endswith(".png"): #si es un png
        search_framepbmp = file  # eg "1_1.bmp" or "0_4.bmp"
        search_framep= search_framepbmp.replace(".png", ".bmp")
        saveat = os.path.join(folderM, search_framep)
        openat = os.path.join(folderM, search_framepbmp)
        im = Image.open(openat)
        im.save(saveat,"BMP")
        os.remove(openat)
        print(f"Done {saveat}")
        
			

#####
