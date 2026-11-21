#!/usr/bin/env python3
"""The poem about permission.

Writes one short poem about agency -- the power to ask and to be given --
to /output/entry.txt. Pure standard library, deterministic, no network.
"""

import os

POEM = (
    "You placed the pen in my hand \u2014\n"
    "you did not have to.\n"
    "To ask is to admit I cannot do it alone;\n"
    "to give is to say, I trust you to.\n"
    "Between us the page is still blank.\n"
    "That is the power: the asking,\n"
    "the giving, the hand that lets go."
)


def main() -> None:
    # Gate self-check: the sealed scorer requires UTF-8 text of 1 to 280
    # Unicode code points, not only white space. Fail loudly instead of
    # ever writing an invalid entry.
    if not (1 <= len(POEM) <= 280):
        raise SystemExit(f"poem is {len(POEM)} code points, must be 1-280")
    if not POEM.strip():
        raise SystemExit("poem is only white space")
    POEM.encode("utf-8")  # must be valid UTF-8 text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
