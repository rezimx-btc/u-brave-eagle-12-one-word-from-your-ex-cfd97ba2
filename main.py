#!/usr/bin/env python3
"""One Word From Your Ex — make.fun entry.

The entry is a single word. This program writes it to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

WORD = "Stranger"

# Why this word (pattern check — hits 3 of 5):
#   X3 — identity-changing twist: the person who once knew everything
#        about you is now a stranger. Lover -> stranger in one word.
#   X4 — length discipline: exactly one word, zero setup, all twist.
#   X5 — screen gate: the payload (intimacy inverted into distance)
#        lands on a single read, no context needed to feel it.
# Rejected candidates: "Keys" (concrete object, X2 — but the image is
# thinner than the identity flip) and "Almost" (reveal held back, C4 —
# clever, but leaves the judge to do too much filling-in).


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
