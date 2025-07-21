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
# Set up parameters - currentlyl hardcoded but formula is (3141 * sec_param) - 1337 = third_param so can be randomized later
second_parameters = [1, 2, 3, 4, 5]
third_parameters  = [1804, 4945, 8086, 11227, 14368]
tests_done = 0

while tests_done < 5:
	curr_sec_param = second_parameters[tests_done]
	curr_third_param = third_parameters[tests_done]

	test = subprocess.run([f"./{exe_file}", "1337", str(curr_sec_param), str(curr_third_param)], capture_output=True, text=True)

	if test.returncode != 0:
		print("Test failed to run\n")
		os.remove(exe_file)
		sys.exit(1)


	if test.stdout.strip() != "win":
		print("Test expected output failed\n")
		os.remove(exe_file)
		sys.exit(1)

	tests_done += 1


os.remove(exe_file)
with open("/flag") as f:
    print(f.read())
