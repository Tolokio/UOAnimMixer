# UOAnimTools
This is a set of tool created to make less painfull work with new UO anims.
It is in very early stage and needs many improvements, but u can already do many awsome anims with this in few minutes.

I am not programmer. I did this just thx to openai chat. Don't expect a clean code, smart code or best performance. Any suggestion or issue just create an issue on github.

Thx to @prapilk for helping me with the axis part.

NOTES:
```
-Only work with anims extracted with mulpatcher.
-All frames need to be in company of respective liste.txt
-Only work with .PNG files, could be done to work with .bmp but I think it is better this way for many reasons. There are 2 tools to convert the files from on file to another very fast.
-USer_INTERFACE.PY is recommended or to use "idle", as u will be able to check logs with the errors and prints. Otherwise cmd will close as soon it ends or get error.
-Combine this tool + photoshop's actions and u will be able to create awsome stuff.
-Converters will set background to black and transparent.
-There are more features under development, will be added once they are ended,fixed or improved to be more friendly with new users.
```
[HELP WANTED]
As I am not programer there are things I dont know how to do and dont have enought time to study for it. Check issues if u want to help with any.

[How to use]

-Install python and allow it to work on cmd. Look for a tutorial on internet. Einfach.
-Dclick on User_interface.py (if u folders are not created use "create folders" to set up folders.

Now u got a folder with many folders and many .py files. Each .py file need will use certain folders.

Template + Wereable.py-> Will paste frames from "WEREABLE" into frames from "TEMPLATE", and then will be saved as .png at OUTPUT

WEREABLE + WEREABLE2.py-> Will paste folder WEREABLE2 into WEREABLE1. For example if we want to merge helmet + bone helmet folders should be filled like this:
              TEMPLATE-> c_man or c_woman frames + liste.txt.
              WEREABLE-> helmet frames + liste.txt
              Wereable2-> Bone helmet + liste.txt
              Output->Where result will be saved.

WEREABLE - WEREABLE2.py-> Will remove the pixels that are not transparent from WEREABLE2 at WEREABLE folder. For example u can use a helmet to cut the head of c_man animation on all frames:
                Template->C_man + liste.txt
                WEREABLE-> c_man + list.txt
                WEREABLE2-> Bone helmet + list.txt
                OUTPUT-> U will get c_man animation but wihout head.

PNGTOBMP.py
BMPTOPNG.py-> This both uses only one folder. It will set black background on all frames, and will remove old files. Just but any .bmp or .png at ACONVERTER folder and use proper converter.

CreateFolders.py-> This will create any missing folder. IT is usefull as many times it is better to rename Folders than moving them to another folder.


                


