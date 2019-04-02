from PIL import Image, ImageDraw


image_xl = Image.open("/Users/shucan/Desktop/111.PNG")
image_sc = Image.open("/Users/shucan/Desktop/222.jpeg")

image_tmp = image_sc.resize((100,100))
print(image_tmp.size)
print(image_tmp.split())
r,g,b = image_tmp.split()

draw = ImageDraw.Draw(image_xl)
draw.bitmap((0,0), r, fill=(255,0,0))
draw.bitmap((100,100), g, fill=(0,255,0))
draw.bitmap((200,200), b, fill=(0,0,255))


#
# print(image_xl.size)
#
# draw.line((0,0) + image_xl.size, fill=(255,0,0))
#
# draw.line((0, image_xl.size[1], image_xl.size[0], 0), fill=255)

image_xl.show()
del image_xl