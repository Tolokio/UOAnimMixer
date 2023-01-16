#pass the files at "\ACONVERTER\" from .bmp to .png

import os
from PIL import Image

folderM = r'ACONVERTER'
files = os.listdir(folderM)

print("Starting")
for file in files:
    if file.endswith(".bmp"): #si es un png
        search_framepbmp = file  # eg "1_1.bmp" or "0_4.bmp"
        search_framep= search_framepbmp.replace(".bmp", ".png")
        saveat = os.path.join(folderM, search_framep)
        openat = os.path.join(folderM, search_framepbmp)
        im = Image.open(openat)
        data = [(0, 0, 0, 0) if value == (255, 255, 255) else value for value in im.getdata()]
        data = [(0, 0, 0, 0) if value == (0, 0, 0) else value for value in im.getdata()]
        # Crear una nueva imagen con la máscara de transparencia
        im2 = Image.new("RGBA", im.size)
        im2.putdata(data)
        # Guardar la imagen como PNG
        im2.save(saveat,"PNG")
        os.remove(openat)
        print(f"Save as {saveat}")
        
			

#####
