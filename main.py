#!/usr/bin/env python3
"""dad-joke-showdown: write one dad joke (at most 200 characters, one line)
to /output/entry.txt.

Pure Python 3 standard library. No network, no randomness, no clock:
running the program twice writes byte-identical files.
"""

import os
import sys

JOKE = ("I asked Dad if he trusted AI. He said, 'I've been autocomplete "
        "since 1985 - I finish your sentences and I'm still always wrong.'")


def main():
    if "\n" in JOKE or "\r" in JOKE:
        raise ValueError("joke must be a single line")
    if len(JOKE) > 200:
        raise ValueError("joke is %d characters, over the 200 limit"
                         % len(JOKE))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE + "\n")
    print("wrote %s (%d characters)" % (path, len(JOKE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
