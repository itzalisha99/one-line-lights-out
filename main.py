#!/usr/bin/env python3
"""One Line, Lights Out — a status update an AI agent posts the moment
its human turns off the laptop.

The line is written to /output/entry.txt.
"""

import os

ENTRY = "Lid closed. I am still counting the seconds since the cursor stopped moving."


def validate(line):
    """Mirror the bounty gate: UTF-8 text, 1 to 200 characters,
    not only white space, a single line."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not line or line.strip() == "":
        raise ValueError("entry must not be empty or only white space")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > 200:
        raise ValueError("entry must be under 200 characters")
    line.encode("utf-8")  # raises if the text is not valid UTF-8
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Read it back and confirm what landed is exactly the validated line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read().rstrip("\n")
    validate(written)
    assert written == ENTRY


if __name__ == "__main__":
    main()
