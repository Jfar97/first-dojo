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
test_strings = ["pwn}}", "pwnddd", "pwnWWXX", "pwnPPPPP", "pwnNNNNX"]

for test_string in test_strings:
	test = subprocess.run([f"./{exe_file}", test_string], capture_output=True, text=True)

	if test.returncode != 0:
		print("Test failed to run\n")
		os.remove(exe_file)
		sys.exit(1)


	if test.stdout.strip() != "flag":
		print("Test expected output failed\n")
		os.remove(exe_file)
		sys.exit(1)

# Failing Test Cases
fail_tests = [
	"pwn",           # Too short (length < 5)
	"abcdefg",       # Wrong prefix
	"pwnaa",         # Right prefix but wrong calculation (97+97)/5 = 38.8
	"pwn11",         # Right prefix but wrong calculation (49+49)/5 = 19.6
	"pwnbb"          # Right prefix but wrong calculation (98+98)/5 = 39.2
]
for test_string in fail_tests:
	test = subprocess.run([f"./{exe_file}", test_string], capture_output=True, text=True)
	if test.stdout.strip() == "flag":
		print("Test should have failed but passed\n")
		os.remove(exe_file)
		sys.exit(1)


os.remove(exe_file)
os.system("/challenge/get_flag")
