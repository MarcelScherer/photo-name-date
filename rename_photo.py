import os
import glob
from PIL import Image
from PIL.ExifTags import TAGS
import time  

def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret

os.chdir("/media/marcel/0012-D687/Fotob.2018 Bauernhof + Center Parc/")

files = glob.glob("*.jpg")

for file in files:
    try:
        print(file)
        time = get_exif(file)["DateTimeOriginal"]

        time = time.replace(":", "")
        time = time.replace(" ", "_")
        number = 0
        new_name = time+"_additional_information.jpg"
        if new_name == file:
            print(new_name, "already ok")
            continue
        while os.path.exists(new_name):
            number += 1
            new_name = time+"_"+str(number)+"_additional_information.jpg"
        os.rename(file, new_name)
    except Exception as e:
        print("error: %s", e)

