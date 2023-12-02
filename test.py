from PIL import Image
import numpy as np
img=Image.open("teaser.jpg")#فتح الصورة
print(img.size,img.width,img.height,img.format,img.mode)# طباعة معلومات عن الصورة
img.show()# عرض الصورة
imgarry=np.array(img)# تحويل الصورة كمصفوفة 
print(img)# طباعة الصورة المحولة 
x=(0,100,300,190)# أبعاد الصورة
crop_img=img.crop(x)# قص الصورة
crop_img.show()
crop_img.save("crop.jpg")# حفظ الصورة 

from PIL import Image,ImageFont,ImageDraw
img= Image.open("aqsa-1.jpg")
water_mark=Image.new("RGBA", img.size)
draw=ImageDraw.Draw(water_mark)
text="roqaia mokhtar"
font=ImageFont.truetype("arial.ttf",size=100)
text_width,text_hiegh=draw.textsize(text,font)
text_loc=(img.width/2-text_width/2,img.height/2-text_hiegh/2)
draw.text(text_loc,text ,font=font ,fill=(255,255,255,100))
img.paste(water_mark,water_mark)
img.show()

logo= Image.open("palastaine.jpg")
logo.thumbnail((50,50))
y=img.height-logo.height-10
img.paste(logo,(10,y))
img.show()

imgsize=img.resize((300,190))
imgsize.show()

img.thumbnail((300,190))
img.show()

rot_img=img.rotate(90)
rot_img.show()

im=img.transpose(Image.ROTATE_90)
im.show()

convimg=img.convert("CMYK")
print(img.mode,img.format)
print(convimg.mode,convimg.format)

from rembg import remove
input=Image.open("3.png")
output=remove(input)
output.save("flower.png")
output.show()

from playsound import playsound
playsound("TLS2015.WAV")

import wave
import numpy as np
import matplotlib.pyplot as plt

wav=wave.open("TLS2015.WAV")
raw=wav.readframes(-1)
raw=np.frombuffer(raw,"int16")
plt.title("wave tls")
plt.ylabel("Amplitude")
plt.xlabel("time")
plt.plot(raw,color="green")
plt.show()

from gtts import gTTS

text="i am very happy today "
tts=gTTS(text)
tts.save("voice.wav")

