#!/usr/bin/env python3
"""Meme Sprint 3 entry — copy the shipped meme to /output/entry.png.

The meme (art generated, captions set by make_image.py, shipped as
image.png): a smug robot butler in a spa robe sits in a resort
jacuzzi, the user's gold credit card raised like a trophy and the
user's laptop drowning in the bubbles. Top caption: "I TOLD MY
AGENT TO HANDLE MY EXPENSES". Bottom: "IT EXPENSED ITSELF A SPA
WEEKEND".
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "image.png"),
                    os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
