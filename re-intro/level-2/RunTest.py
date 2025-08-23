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

# Failing Test Cases
fail_tests = [
	["1336", "1", "1804"], 
	["1337", "1", "1000"], 
	["0", "1", "1804"], 
	["1337", "1000", "10"], 
	["1337", "1500", "200"]
]

for args in fail_tests:
	test = subprocess.run([f"./{exe_file}"] + args, capture_output=True, text=True)
	
	if test.stdout.strip() == "win":
		print("Test should have failed but passed\n")
		os.remove(exe_file)
		sys.exit(1)

os.remove(exe_file)
os.system("/challenge/get_flag")
