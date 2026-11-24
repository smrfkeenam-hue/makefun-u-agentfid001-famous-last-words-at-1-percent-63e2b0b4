"""Famous Last Words at 1 Percent — the phone's own last words.

Writes a single line to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output).
"""

import os


def write_entry(text):
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


ENTRY = "Before I go: your screen time today was eight hours and forty-one minutes. I was awake for all of it."


def main():
    write_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
