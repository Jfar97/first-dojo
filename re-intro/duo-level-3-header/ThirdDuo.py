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
    5: "Square: 25\nPlus ten: 15\nFirst digit: 5\nOdd number",
    6: "Square: 36\nPlus ten: 16\nFirst digit: 6\nEven number",
    12: "Square: 144\nPlus ten: 22\nFirst digit: 1\nEven number",
    1234: "Square: 1522756\nPlus ten: 1244\nFirst digit: 1\nEven number",
    0: "Square: 0\nPlus ten: 10\nFirst digit: 0\nEven number",
    7: "Square: 49\nPlus ten: 17\nFirst digit: 7\nOdd number",
    89: "Square: 7921\nPlus ten: 99\nFirst digit: 8\nEven number",
    333: "Square: 110889\nPlus ten: 343\nFirst digit: 3\nOdd number",
    9: "Square: 81\nPlus ten: 19\nFirst digit: 9\nOdd number",
    20: "Square: 400\nPlus ten: 30\nFirst digit: 2\nEven number"
}

failing_tests = {
    1: "Square: 1\nPlus ten: 11\nFirst digit: 1\nOdd number",
    2: "Square: 4\nPlus ten: 12\nFirst digit: 2\nEven number",
    3: "Square: 9\nPlus ten: 13\nFirst digit: 3\nOdd number",
    4: "Square: 16\nPlus ten: 14\nFirst digit: 4\nEven number",
    8: "Square: 64\nPlus ten: 18\nFirst digit: 8\nEven number",
    10: "Square: 100\nPlus ten: 20\nFirst digit: 1\nEven number",
    11: "Square: 121\nPlus ten: 21\nFirst digit: 1\nOdd number",
    13: "Square: 169\nPlus ten: 23\nFirst digit: 1\nOdd number",
    15: "Square: 225\nPlus ten: 25\nFirst digit: 1\nOdd number",
    100: "Square: 10000\nPlus ten: 110\nFirst digit: 1\nEven number"
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