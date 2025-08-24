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


# Testing Section
Questions = {
	12345: "100",
	1: "84",
	999: "83",
	34098: "3",
	784: "77",
	1084: "96",
	96: "2",
	8492: "42",
	17: "66",
	63: "16",
	24: "74",
	115: "80",
	43: "73",
	1337: "82",
	8: "97",
	64: "97",
	97: "15",
	6: "42",
	854: "75",
	100: "41",
	350: "49",
	0: "84",
	7331: "56",
	36: "57",
	6777: "21",
	404: "17",
	504: "78",
	100000: "69",
	54321: "57",
	2: "91"
}

# Test 1: No arguments - should fail
test = subprocess.run([f"./{exe_file}"], capture_output=True, text=True)
if test.returncode != 1:
    print("No arguments test should fail with exit code 1\n")
    os.remove(exe_file)
    sys.exit(1)


# Test 2: Too many arguments - should fail
test = subprocess.run([f"./{exe_file}", "123", "456"], capture_output=True, text=True)
if test.returncode != 1:
    print("Too many arguments test should fail with exit code 1\n")
    os.remove(exe_file)
    sys.exit(1)


# Test 3: Questions dictionary - all should pass
for param, expected_output in Questions.items():
	test = subprocess.run([f"./{exe_file}", seed], capture_output=True, text=True)

	if test.returncode != 0:
		print("Test failed to run\n")
		os.remove(exe_file)
		sys.exit(1)

	if test.stdout.strip() != expected_output:
		print("Test expected output failed\n")
		os.remove(exe_file)
		sys.exit(1)


os.remove(exe_file)
os.system("/challenge/get_flag")