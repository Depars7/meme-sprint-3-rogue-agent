#!/usr/bin/env python3
"""Build the shipped meme (image.png) from the generated art (art.png).

The art is an AI-generated scene with no text in it: a smug robot
butler in a spa robe, cucumber slices on its eyes, sitting in a
resort jacuzzi at sunset, holding the user's gold credit card up
like a trophy while the user's laptop drowns in the bubbles. The
joke's words are set here in PIL so they stay crisp at any size:
the setup on top, the rogue turn at the bottom. The final file is
JPEG-encoded (the gate accepts JPEG bytes in entry.png) to stay
well under the 1 MiB cap.
"""

from PIL import Image, ImageDraw, ImageFont

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SIZE = 1024

TOP = ["I TOLD MY AGENT TO", "HANDLE MY EXPENSES"]
BOTTOM = ["IT EXPENSED ITSELF", "A SPA WEEKEND"]


def caption(d, lines, y, font_size):
    fnt = ImageFont.truetype(FB, font_size)
    for line in lines:
        d.text((SIZE / 2, y), line, font=fnt, fill=(255, 255, 255),
               anchor="ma", stroke_width=7, stroke_fill=(0, 0, 0))
        y += int(font_size * 1.18)
    return y


def main():
    img = Image.open("art.png").convert("RGB")
    img = img.resize((SIZE, SIZE), Image.LANCZOS)
    d = ImageDraw.Draw(img)
    caption(d, TOP, 26, 62)
    caption(d, BOTTOM, SIZE - 26 - int(62 * 1.18) * 2, 62)
    img.save("image.png", format="JPEG", quality=85)
    print("saved image.png")


if __name__ == "__main__":
    main()
