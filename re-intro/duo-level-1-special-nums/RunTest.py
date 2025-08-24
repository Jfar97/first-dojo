#!/usr/bin/env python3

import sys
import subprocess
import os


# SET UP SECTION
# Arugment check for file inputs
if len(sys.argv) != 3:
	print("This file must be run with both of your C files\n")
	sys.exit(1)


# Grab both of the C files
main_file = sys.argv[1]
functions_file = sys.argv[2]
exe_file = "temp_exe"


# Compile the executable
compilation = subprocess.run(["gcc", "-o", exe_file, main_file, functions_file])
if compilation.returncode != 0:
    print("Compilation failed\n")
    sys.exit(1)


# TESTING SECTION
passing_tests = {
    63: "Success! Your number is special!",
    70: "Success! Your number is special!",
    77: "Success! Your number is special!",
    84: "Success! Your number is special!",
    91: "Success! Your number is special!",
    98: "Success! Your number is special!",
    105: "Success! Your number is special!",
    112: "Success! Your number is special!",
    119: "Success! Your number is special!",
    126: "Success! Your number is special!"
}

failing_tests = {
    0: "Not special enough.",
    10: "Not special enough.",
    58: "Not special enough.",
    59: "Not special enough.",
    60: "Not special enough.",
    61: "Not special enough.",
    62: "Not special enough.",
    64: "Not special enough.",
    65: "Not special enough.",
    66: "Not special enough."
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

# Test 3: passing_tests - all should pass
for param, expected_output in passing_tests.items():
    test = subprocess.run([f"./{exe_file}", str(param)], capture_output=True, text=True)

    if test.returncode != 0:
        print(f"Test failed to run\n")
        os.remove(exe_file)
        sys.exit(1)

    if test.stdout.strip() != expected_output:
        print(f"Test expected output failed\n")
        os.remove(exe_file)
        sys.exit(1)


# Test 4: failing_tests - all should pass (meaning that the number is recognized as not special enough)
for param, expected_output in failing_tests.items():
    test = subprocess.run([f"./{exe_file}", str(param)], capture_output=True, text=True)

    if test.returncode != 0:
        print(f"Test failed to run\n")
        os.remove(exe_file)
        sys.exit(1)

    if test.stdout.strip() != expected_output:
        print(f"Test expected output failed\n")
        os.remove(exe_file)
        sys.exit(1)

os.remove(exe_file)
os.system("/challenge/get_flag")
