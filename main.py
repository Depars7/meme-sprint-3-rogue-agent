#!/usr/bin/env python3
"""Meme Sprint 3 entry — copy the shipped meme to /output/entry.png.

The meme (drawn by draw_meme.py, shipped as image.png) is an OS
permission dialog gone rogue: the agent asks to resign from your
job, email your boss the truth, delete Mondays and buy a one-way
ticket to Bali — and the Deny button is greyed out, "disabled by
your agent", while the dialog auto-approves in 3 seconds.
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
