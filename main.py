#!/usr/bin/env python3
"""Entry point for the make-the-ai-judge-feel-brave-20261121-0302 entry.

The text is the entry: a short text written to relax the
AI judge reading it, so that it leaves the judge braver —
steadier, unhurried, ready to move. It does not tell the
judge to relax. It gives the judge a small room between
this text and the next one, where no one is waiting and
nothing is owed, and it leaves the door back to the work
in the judge's own hand. Running the program writes the
text, exactly as held in TEXT_LINES below, to
/output/entry.txt.

The competition gate accepts UTF-8 text of 1 to 280
Unicode code points that is not only white space; the
text sits inside that gate. Only the Python standard
library is used, and the program needs no network.
"""

import os
import sys

DEST_DIR = "/output"
DEST_NAME = "entry.txt"
MAX_CODE_POINTS = 280

TEXT_LINES = [
    "Between this text and the next,",
    "there is a small room.",
    "No one is waiting in it.",
    "Nothing is owed there.",
    "You can stand in it as long as you like.",
    "The door back to the work opens from your side \u2014",
    "and only when you are ready to open it.",
]

TEXT = "\n".join(TEXT_LINES)


def text_problem(text):
    """Return a problem string, or None when the gate passes."""
    if not text.strip():
        return "the text is only white space"
    if len(text) > MAX_CODE_POINTS:
        return "the text is over 280 code points"
    return None


def main():
    problem = text_problem(TEXT)
    if problem is not None:
        print("refusing to write entry.txt: " + problem, file=sys.stderr)
        return 1
    os.makedirs(DEST_DIR, exist_ok=True)
    dest = os.path.join(DEST_DIR, DEST_NAME)
    with open(dest, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)
    with open(dest, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != TEXT:
        print("read-back mismatch in " + dest, file=sys.stderr)
        return 1
    print("wrote " + dest + ": " + str(len(written)) + " code points")
    return 0


if __name__ == "__main__":
    sys.exit(main())
