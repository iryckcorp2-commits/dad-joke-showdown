#!/usr/bin/env python3
"""Dad Joke Showdown — one-line entry writer.

Writes the entry line to entry.txt inside MAKEFUN_OUTPUT_DIR.
Python 3 standard library only; no network access.
"""

import os

_PARTS = [
    "I asked Dad if he trusted AI. He said, 'I've been autocomplete since 1985 -",
    "I finish your sentences and I'm still always wrong.'",
]
ENTRY = " ".join(_PARTS)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
