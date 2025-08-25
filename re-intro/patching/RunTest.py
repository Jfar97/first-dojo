#!/usr/bin/exec-suid -- /usr/local/bin/python -I

import os
import pathlib
import subprocess

dir = pathlib.Path(__file__).parent
c_executable = dir / "challenge"

result = subprocess.run([c_executable], capture_output=True, text=True)

if result.returncode != 1337:
	print("The 'challenge' executable still needs to be patched\n")
else:
	with open("/flag") as f:
		print(f.read())
