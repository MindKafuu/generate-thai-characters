from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
 
for i in range(0, 89):
    # print(chr(ord('ก') + i))
    img = Image.new('RGB', (40, 70), color = (0, 0, 0))
    
    fnt = ImageFont.truetype("34.ttf", 30)
    d = ImageDraw.Draw(img)
    d.text((15, 25), chr(ord('ก') + i), font = fnt, fill = (255, 255, 255))
    img.save(str(i) + '_28.png')