#Import all Libraries
import matplotlib
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os

name_list = "NameList.xlsx"
target_file = 'Target.jpg'
font_file = "Montserrat-ExtraBold.ttf"
x = 298.8298
y = 350.3404
fs = 500 #Put 10x larger Font size than u want here
max_width = 327.0638
max_h = 36.766


def Fitting_Text_in_Box():
    global fs, max_width, font_file, each_name, font, max_h
    while True:
        font = ImageFont.truetype(font_file, size = fs)
        if I1.textsize(each_name, font = font)[0] < max_width or I1.textsize(each_name, font = font)[1] < max_h:
            fs = fs + 1     
        else:
            break
    
    
    while True:
        font = ImageFont.truetype(font_file, size=fs)
        if I1.textsize(each_name, font = font)[0] > max_width or I1.textsize(each_name, font = font)[1] > max_h:
            fs = fs - 1     
        else:
            break

file_read = pd.read_excel(name_list)
names = file_read["Names"]

start = datetime.now()

for each_name in names:
    # Open an Image
    img = Image.open(target_file)
    font = ImageFont.truetype(font_file, size=fs)

    # Call draw Method to add 2D graphis in an image
    I1 = ImageDraw.Draw(img)

    #remove extra spaces
    each_name = " ".join(each_name.split()).title()

    Fitting_Text_in_Box()

    # Add Text to an image
    I1.text((x, y), each_name, fill='black', font=font, anchor='mm')
    
    # Create Directory to save generated files.
    try:
        os.mkdir("saved")
    except:
        pass
    
    
    # Save files
    img.save("saved/{}.jpg".format(each_name))
    
end = datetime.now()
tt = end-start
print(tt.seconds)