#!/usr/bin/env python3

import sys
import subprocess
import os
import random


# SET UP SECTION
# Arugment check for file inputs
if len(sys.argv) != 2:
	print("This file must be run with your C file\n")
	sys.exit(1)


# Grab C file and set up temporary executable placeholder
c_file = sys.argv[1]
exe_file = "temp_exe" # Needs to have name for when subprocess runs it later for the tests, otherwise it will just attempt to run ./ file.c


# Compile the C file
compilation = subprocess.run(["/run/workspace/bin/gcc", "-o", exe_file, c_file])
if compilation.returncode != 0:
	print("Compilation failed\n")
	sys.exit(1)


# TESTING SECTION
# Create five random numbers between 1 and 100 to be tested
testing_nums = []
for i in range(5):
	random_num = random.randint(1, 100)
	testing_nums.append(random_num)


# Now check the output of the 
for num in testing_nums:
	# capture_output needs to for sure be true so the actual stdout of the executable for each test can be read
	# ALSO need text to be true so that stdout is a string instead of bytes
	test = subprocess.run([f"./{exe_file}", str(num)], capture_output=True, text=True)

	if test.returncode != 0:
		print("Test failed to run\n")
		os.remove(exe_file)
		sys.exit(1)


	if int(test.stdout.strip()) != num*num:	# Grab the stdout from the test and strip white space and new line chars so that just the outputted int can be compared to num*num
		print("Test expected output failed\n")
		os.remove(exe_file)
		sys.exit(1)


# All tests passed means user reverse engineered the file successfully so give flag
os.remove(exe_file)
#with open("/flag") as f:
    #print(f.read())
os.system("/challenge/get_flag")
