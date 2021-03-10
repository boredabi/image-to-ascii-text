from PIL import Image
import math

ascii = "#WSAo*~+-,."[::-1]
ascii_ar=list(ascii)
ascii_len=len(ascii_ar)
increment=(ascii_len/256)

character_h=21
character_w=13
div=character_w/character_h

text= open("output.txt","w")

def char(inp):
    return(ascii_ar[math.floor(inp*increment)])

img = Image.open("Desktop/pika.jpg")
img = img.convert('RGB')
w, h = img.size
down_scale=0.5
img=img.resize((int(down_scale*w), int((down_scale*h)*div)), Image.NEAREST)
w,h =img.size
pixel = (img.load())

for y in range(h):
    for x in range(w):
        r, g, b= pixel[x,y]
        m= int(r/3+g/3+b/3)
        pixel[x,y]=(m,m,m)
        text.write(char(m))
    text.write("\n")