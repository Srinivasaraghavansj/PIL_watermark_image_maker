from PIL import Image, ImageDraw, ImageFont

width =  1000
height = 1000
name = "Student Name here"
email = "studentemailhere@email.com"
font = ImageFont.truetype("SvargeRegular-lgaLe.ttf", size=55)
img = Image.new('RGBA', (width, height), color=(255, 255, 255, 0))
imgDraw = ImageDraw.Draw(img)

_,__,textWidth1, textHeight1 = imgDraw.textbbox((0,0),name, font=font)
xText1 = (width - textWidth1) / 2
yText1 = (height - textHeight1) / 2.2
imgDraw.text((xText1, yText1), name, font=font, fill=(120, 120, 120))

_,__,textWidth2, textHeight2 = imgDraw.textbbox((0,0),email, font=font)
xText2 = (width - textWidth2) / 2
yText2 = (height - textHeight2) / 1.8
imgDraw.text((xText2, yText2), email, font=font, fill=(120, 120, 120))

img = img.rotate(45,expand=True, fillcolor=(255, 255, 255, 0))
img.save('result.png')