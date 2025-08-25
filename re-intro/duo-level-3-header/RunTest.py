#!/usr/bin/env python3
import sys
import subprocess
import os

# SET UP SECTION
# Arugment check for file inputs
if len(sys.argv) != 4:
    print("This file must be run with your main.c, math_utils.c, and header file\n")
    sys.exit(1)

# Grab both C files and header file
main_file = sys.argv[1]
functions_file = sys.argv[2]
header_file = sys.argv[3]
exe_file = "temp_exe"

# Rename header to math_utils.h for consistency
if header_file != "math_utils.h":
    subprocess.run(["cp", header_file, "math_utils.h"])

# Compile the executable
compilation = subprocess.run(["gcc", "-o", exe_file, main_file, functions_file])
if compilation.returncode != 0:
    print("Compilation failed\n")
    if os.path.exists("math_utils.h") and header_file != "math_utils.h":
        os.remove("math_utils.h")
    sys.exit(1)

# TESTING
passing_tests = {
    5: "Square of 5 is 25\nAdding ten: 15\nFirst digit: 5\nYour number is odd!",
    6: "Square of 6 is 36\nAdding ten: 16\nFirst digit: 6\nYour number is even!",
    12: "Square of 12 is 144\nAdding ten: 22\nFirst digit: 1\nYour number is even!",
    1234: "Square of 1234 is 1522756\nAdding ten: 1244\nFirst digit: 1\nYour number is even!",
    0: "Square of 0 is 0\nAdding ten: 10\nFirst digit: 0\nYour number is even!",
    7: "Square of 7 is 49\nAdding ten: 17\nFirst digit: 7\nYour number is odd!",
    89: "Square of 89 is 7921\nAdding ten: 99\nFirst digit: 8\nYour number is odd!",
    333: "Square of 333 is 110889\nAdding ten: 343\nFirst digit: 3\nYour number is odd!",
    9: "Square of 9 is 81\nAdding ten: 19\nFirst digit: 9\nYour number is odd!",
    20: "Square of 20 is 400\nAdding ten: 30\nFirst digit: 2\nYour number is even!"
}

failing_tests = {
    1: "Square of 1 is 1\nAdding ten: 11\nFirst digit: 1\nYour number is odd!",
    2: "Square of 2 is 4\nAdding ten: 12\nFirst digit: 2\nYour number is even!",
    3: "Square of 3 is 9\nAdding ten: 13\nFirst digit: 3\nYour number is odd!",
    4: "Square of 4 is 16\nAdding ten: 14\nFirst digit: 4\nYour number is even!",
    8: "Square of 8 is 64\nAdding ten: 18\nFirst digit: 8\nYour number is even!",
    10: "Square of 10 is 100\nAdding ten: 20\nFirst digit: 1\nYour number is even!",
    11: "Square of 11 is 121\nAdding ten: 21\nFirst digit: 1\nYour number is odd!",
    13: "Square of 13 is 169\nAdding ten: 23\nFirst digit: 1\nYour number is odd!",
    15: "Square of 15 is 225\nAdding ten: 25\nFirst digit: 1\nYour number is odd!",
    100: "Square of 100 is 10000\nAdding ten: 110\nFirst digit: 1\nYour number is even!"
}

# Test 1: passing tests
for num, expected_output in passing_tests.items():
    test = subprocess.run([f"./{exe_file}", str(num)], capture_output=True, text=True)
    if test.returncode != 0:
        print("Test failed to run\n")
        os.remove(exe_file)
        if os.path.exists("math_utils.h") and header_file != "math_utils.h":
            os.remove("math_utils.h")
        sys.exit(1)
    if test.stdout.strip() != expected_output:
        print("Test expected output failed\n")
        os.remove(exe_file)
        if os.path.exists("math_utils.h") and header_file != "math_utils.h":
            os.remove("math_utils.h")
        sys.exit(1)

# Test 2: failing tests
for num, expected_output in failing_tests.items():
    test = subprocess.run([f"./{exe_file}", str(num)], capture_output=True, text=True)
    if test.returncode != 0:
        print("Test failed to run\n")
        os.remove(exe_file)
        if os.path.exists("math_utils.h") and header_file != "math_utils.h":
            os.remove("math_utils.h")
        sys.exit(1)
    if test.stdout.strip() != expected_output:
        print("Test expected output failed\n")
        os.remove(exe_file)
        if os.path.exists("math_utils.h") and header_file != "math_utils.h":
            os.remove("math_utils.h")
        sys.exit(1)

# Test 3: no arguments - should fail
test = subprocess.run([f"./{exe_file}"], capture_output=True, text=True)
if test.returncode != 1:
    print("No arguments test should fail with exit code 1\n")
    os.remove(exe_file)
    if os.path.exists("math_utils.h") and header_file != "math_utils.h":
        os.remove("math_utils.h")
    sys.exit(1)

# Test 4: invalid arguments - should fail
test = subprocess.run([f"./{exe_file}", "123", "456"], capture_output=True, text=True)
if test.returncode != 1:
    print("Too many arguments test should fail with exit code 1\n")
    os.remove(exe_file)
    if os.path.exists("math_utils.h") and header_file != "math_utils.h":
        os.remove("math_utils.h")
    sys.exit(1)

os.remove(exe_file)
if os.path.exists("math_utils.h") and header_file != "math_utils.h":
    os.remove("math_utils.h")
os.system("/challenge/get_flag")
