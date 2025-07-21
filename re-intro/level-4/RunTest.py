#!/usr/bin/env python3

import sys
import subprocess
import os


# SET UP SECTION
# Arugment check for file inputs
if len(sys.argv) != 2:
	print("This file must be run with your C file\n")
	sys.exit(1)


# Grab C file and set up temporary executable placeholder
c_file = sys.argv[1]
exe_file = "temp_exe" 


# Compile the C file
compilation = subprocess.run(["gcc", "-o", exe_file, c_file])
if compilation.returncode != 0:
	print("Compilation failed\n")
	sys.exit(1)


# TESTING SECTION
test_bytes = ["college##", "college+-", "college,,", "college,+2", "college++++"]

for test_byte in test_bytes:
	test = subprocess.run([f"./{exe_file}", test_byte], capture_output=True, text=True)

	if test.returncode != 0:
		print("Test failed to run\n")
		os.remove(exe_file)
		sys.exit(1)


	if test.stdout.strip() != "pwned":
		print("Test expected output failed\n")
		os.remove(exe_file)
		sys.exit(1)



os.remove(exe_file)
with open("/flag") as f:
    print(f.read())
