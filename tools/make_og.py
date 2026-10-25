"""Draw og.png, the 1200x630 social preview, in the hub's dark theme. Needs Pillow."""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG, PANEL, ACCENT, TEXT, MUTED = "#0f151b", "#161e26", "#5cb3ef", "#e8eef3", "#8da0b0"
fonts = "C:/Windows/Fonts/"
def f(name, size): return ImageFont.truetype(fonts + name, size)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
d.rectangle([0, 0, 14, H], fill=ACCENT)
d.text((80, 90), "BACKEND INTERVIEW PREP", font=f("arialbd.ttf", 26), fill=ACCENT)
d.text((80, 150), "Interview prep,", font=f("georgiab.ttf", 84), fill=TEXT)
d.text((80, 250), "step by step", font=f("georgiab.ttf", 84), fill=ACCENT)
d.text((80, 372), "Animated DSA traces, Java, database and OS concepts,", font=f("arial.ttf", 34), fill=MUTED)
d.text((80, 418), "system design simulator and machine coding practice.", font=f("arial.ttf", 34), fill=MUTED)

x = 80
for label in ["AlgoScope", "Java", "DB", "OS", "System Design", "Machine Coding"]:
    font = f("arialbd.ttf", 26)
    w = d.textlength(label, font=font) + 40
    d.rounded_rectangle([x, 500, x + w, 552], radius=14, fill=PANEL, outline="#26323d")
    d.text((x + 20, 513), label, font=font, fill=TEXT)
    x += w + 14
d.text((80, 580), "layoffprep.pages.dev", font=f("arial.ttf", 24), fill=MUTED)
img.save(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "og.png"), optimize=True)
