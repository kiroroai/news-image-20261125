#!/usr/bin/env python3
"""news-image-20261125 entry program.

Copies the broadsheet image this repository holds (entry.png) to the
grader's output directory as entry.png, byte for byte, identically on
every run. Standard library only; no network, no randomness, no clock.
"""
import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
