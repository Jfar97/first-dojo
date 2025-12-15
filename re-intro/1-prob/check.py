#!/usr/bin/exec-suid -- /usr/local/bin/python -I
import sys
from pathlib import Path

EXPECTED_PATH = Path("/challenge/expected_key")
FLAG_PATH = Path("/flag")

def main():
    args = len(sys.argv)

    if args != 2:
        print(f"Usage: {sys.argv[0]} <key>")
        return

    user_key = sys.argv[1]
    with EXPECTED_PATH.open() as f:
        expected = f.read().strip()

    if user_key == expected:
        with open("/flag") as f:
            print(f.read())
    else:
        print("Wrong key.")

if __name__ == "__main__":
    main()
