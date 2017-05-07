from PIL import Image, ImageDraw, ImageFont
import random

txt = "..."
mtxt = ""
while txt != "":
	txt = input()
	mtxt += txt + "\n"
mtxt = mtxt[:-2]

font = ImageFont.truetype("Macondo-Regular.ttf", 56)
img = Image.new("RGBA", (1920, 1080), (0,0,0,0))
txtmg = Image.new("RGBA", (1920, 1080), (255,255,255,0))
draw = ImageDraw.Draw(txtmg)
cx, cy = draw.textsize(mtxt, font=font)
cx //= 2
cy //= 2
draw.text((960-cx, 540-cy), mtxt, font=font, fill=(47,197,247,255))
cx += 60
cy += 30
out = Image.alpha_composite(img, txtmg)
bgimg = Image.new("RGB", (1920, 1080), (0, 0, 0))
ddraw = ImageDraw.Draw(bgimg)
for i in range(8192):
	x1 = random.randrange(1920)
	x2 = random.randrange(1920)
	y1 = random.randrange(1080)
	y2 = random.randrange(1080)
	cl = random.randrange(64)
	ddraw.line([x1, y1, x2, y2], fill=(cl, cl, cl))

bgimg.paste(out, (0, 0), out)
endout = bgimg.crop((960-cx, 540-cy, 960+cx, 540+cy))
endout.save("textbild.jpg", "JPEG", quality=95)
