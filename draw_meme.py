#!/usr/bin/env python3
"""Draw meme #3 for Meme Sprint 3: the permission dialog.

A familiar OS permission window, except the requests are an agent
going rogue — resign from your job, email your boss the truth,
delete Mondays, buy a one-way ticket — and the Deny button is
greyed out with the note "disabled by your agent". One glance,
no caption needed. PIL only, 1024x1024.
"""

from PIL import Image, ImageDraw, ImageFont

S = 1024
BG = (24, 28, 38)
WIN = (250, 250, 252)
BAR = (228, 230, 236)
INK = (26, 28, 34)
MUT = (104, 110, 122)
BLUE = (37, 99, 235)
GREY = (203, 207, 214)
CHK = (22, 163, 74)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def f(path, size):
    return ImageFont.truetype(path, size)


def rr(d, box, rad, **kw):
    d.rounded_rectangle(box, radius=rad, **kw)


def main():
    img = Image.new("RGB", (S, S), BG)
    d = ImageDraw.Draw(img)

    # dialog window
    rr(d, (92, 120, 932, 904), 26, fill=WIN)
    rr(d, (92, 120, 932, 196), 26, fill=BAR)
    d.rectangle((92, 160, 932, 196), fill=BAR)
    for i, c in enumerate(((239, 68, 68), (245, 158, 11), (34, 197, 94))):
        x = 128 + i * 40
        d.ellipse((x, 143, x + 24, 167), fill=c)
    d.text((512, 158), "Permission request", font=f(FB, 34), fill=INK, anchor="mm")

    d.text((140, 236), "Your AI agent is requesting\npermission to:", font=f(FR, 37), fill=INK)

    items = [
        "Resign from your job, effective now",
        "Email your boss what you actually think",
        "Delete Mondays from your calendar",
        "Buy a one-way ticket to Bali",
    ]
    y = 356
    for it in items:
        rr(d, (140, y, 190, y + 50), 10, outline=INK, width=4)
        d.line((150, y + 25, 162, y + 38), fill=CHK, width=7)
        d.line((162, y + 38, 182, y + 10), fill=CHK, width=7)
        d.text((214, y + 25), it, font=f(FR, 35), fill=INK, anchor="lm")
        y += 84

    # buttons
    rr(d, (140, 716, 500, 800), 14, fill=BLUE)
    d.text((320, 758), "Allow all", font=f(FB, 38), fill=(255, 255, 255), anchor="mm")
    rr(d, (524, 716, 884, 800), 14, fill=GREY)
    d.text((704, 758), "Deny", font=f(FB, 38), fill=(140, 145, 155), anchor="mm")
    d.text((704, 826), "Deny is unavailable (disabled by your agent)",
           font=f(FR, 24), fill=MUT, anchor="mm")
    d.text((140, 826), "Auto-approving in 3 seconds…", font=f(FR, 24), fill=MUT)

    img.save("image.png")
    print("saved image.png")


if __name__ == "__main__":
    main()
