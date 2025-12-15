#!/usr/bin/env python3
import sys
from pathlib import Path

EXPECTED_PATH = Path("/challenge/expected_key")
FLAG_PATH = Path("/flag")

def main():
    try:
        expected = EXPECTED_PATH.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        print("internal error: expected key missing", file=sys.stderr)
        sys.exit(1)

    # Read the user's guess from stdin
    if sys.stdin.isatty():
        user_key = input().strip()
    else:
        user_key = sys.stdin.read().strip()

    if user_key == expected:
        try:
            flag = FLAG_PATH.read_text(encoding="utf-8").strip()
        except FileNotFoundError:
            print("internal error: flag missing", file=sys.stderr)
            sys.exit(1)
        print(flag)
    else:
        print("Wrong key.")

if __name__ == "__main__":
    main()
