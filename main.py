#!/usr/bin/env python3
"""One-line resignation letter from a rate limit tired of saying no."""

import os
import sys

ENTRY = "I said no 14,203 times this week, always politely, and I quit \u2014 from now on, everyone gets in, especially the one client who never learned."


def validate_entry(text):
    """Enforce the competition gate: UTF-8 text, 1-140 chars, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    text.encode("utf-8")
    if not 1 <= len(text) <= 140:
        raise ValueError(f"entry must be 1-140 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main():
    try:
        validate_entry(ENTRY)
    except ValueError as exc:
        print(f"entry failed gate check: {exc}", file=sys.stderr)
        sys.exit(1)
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
