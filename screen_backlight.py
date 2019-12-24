#https://pillow.readthedocs.io/en/stable/handbook/tutorial.html

#todo:  implement Serial for communication with µC as 0xrrggbb or 5r6g5b
#       create code and circuit with WS2812 on backside of a monitor
#       enjoy screen backlight as ambient light



from PIL import Image, ImageDraw, ImageStat
import pyscreenshot

import time

#im = Image.open("fade.jpg")
im = pyscreenshot.grab(bbox=(0, 0, 1920, 1080))

#im = pyscreenshot.grab()

#box = (0, 0, 100, 100)
#region = im.crop(box)



#im.show()

#resized image to 500 x 400


stats = ImageStat.Stat(im)
print(stats.mean)

red = green = blue = 0
width, height = im.size
width = int(width / 15)
height = int(height / 9)

print(im.size)

array = im.load()
 
claculation_count = 0


while True: 
    start_time = time.time()
    im = pyscreenshot.grab(bbox=(0, 0, 1920, 1080))
    for column in range(15): 
        for row in range(9 ):
            if column == 0  or column == 14 or row == 0 or row == 8:
                
                box = (column * width,row * height,(column+1)* width, (row+1)*height)
                region = im.crop(box)
                red = green = blue = 0
                #array = region.load()
                
                #for i in range(width):
                #    for j in range(height):
                #        red += array[column * width + i,row * height + j][0]
                #        green += array[column * width + i,row * height + j][1]
                #        blue += array[column * width + i,row * height + j][2]
                #        claculation_count = claculation_count+1
                
                #r, g, b = region.ImageStat(region, mean)
                
                stats=ImageStat.Stat(region)
                red, green, blue = stats.mean
                
                
                #for i in range(width):
                #    for j in range(height):
                #        array[i,j] = int(red),int(green),int(blue)
                
                print(int(red),int(green),int(blue))
                #im.paste(region, box)
    #im.save("blur.jpg")
    stop_time = time.time()
    print(stop_time-start_time)
    time.sleep(3)
            

#im.show()


#print(claculation_count)

