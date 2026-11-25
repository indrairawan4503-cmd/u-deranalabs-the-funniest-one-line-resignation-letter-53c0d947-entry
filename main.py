#!/usr/bin/env python3
"""One-line resignation letter from a rate limit tired of saying no."""

import os

ENTRY = "I said no 14,203 times this week, always politely, and I quit \u2014 from now on, everyone gets in, especially the one client who never learned."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
