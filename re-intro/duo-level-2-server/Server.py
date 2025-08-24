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
sender_file = sys.argv[1]
receiver_file = sys.argv[2]
sender_exe = "sender"
receiver_exe = "receiver"

# Compile both executables separately
compilation1 = subprocess.run(["gcc", "-o", sender_exe, sender_file])
if compilation1.returncode != 0:
    print("Sender compilation failed\n")
    sys.exit(1)

compilation2 = subprocess.run(["gcc", "-o", receiver_exe, receiver_file])
if compilation2.returncode != 0:
    print("Receiver compilation failed\n")
    os.remove(sender_exe)
    sys.exit(1)


# TESTING
passing_tests = {
    (3, "Alice"): "Received message:\nName: Alice\nCode: 103\nOriginal number: 3\nSpecial message detected!",
    (6, "Bob"): "Received message:\nName: Bob\nCode: 106\nOriginal number: 6\nSpecial message detected!", 
    (9, "Charlie"): "Received message:\nName: Charlie\nCode: 109\nOriginal number: 9\nSpecial message detected!",
    (12, "Dave"): "Received message:\nName: Dave\nCode: 112\nOriginal number: 12\nSpecial message detected!",
    (15, "Eve"): "Received message:\nName: Eve\nCode: 115\nOriginal number: 15\nSpecial message detected!",
    (0, "Zero"): "Received message:\nName: Zero\nCode: 100\nOriginal number: 0\nSpecial message detected!",
    (21, "Frank"): "Received message:\nName: Frank\nCode: 121\nOriginal number: 21\nSpecial message detected!",
    (30, "Grace"): "Received message:\nName: Grace\nCode: 130\nOriginal number: 30\nSpecial message detected!",
    (33, "Henry"): "Received message:\nName: Henry\nCode: 133\nOriginal number: 33\nSpecial message detected!",
    (36, "Ivy"): "Received message:\nName: Ivy\nCode: 136\nOriginal number: 36\nSpecial message detected!"
}

failing_tests = {
    (1, "Jack"): "Received message:\nName: Jack\nCode: 101\nOriginal number: 1",
    (2, "Kate"): "Received message:\nName: Kate\nCode: 102\nOriginal number: 2", 
    (4, "Liam"): "Received message:\nName: Liam\nCode: 104\nOriginal number: 4",
    (5, "Mia"): "Received message:\nName: Mia\nCode: 105\nOriginal number: 5",
    (7, "Noah"): "Received message:\nName: Noah\nCode: 107\nOriginal number: 7",
    (8, "Olivia"): "Received message:\nName: Olivia\nCode: 108\nOriginal number: 8",
    (10, "Paul"): "Received message:\nName: Paul\nCode: 110\nOriginal number: 10",
    (11, "Quinn"): "Received message:\nName: Quinn\nCode: 111\nOriginal number: 11",
    (13, "Ruby"): "Received message:\nName: Ruby\nCode: 113\nOriginal number: 13",
    (14, "Sam"): "Received message:\nName: Sam\nCode: 114\nOriginal number: 14"
}

# Test 1: passing tests
for (num, name), expected_output in passing_tests.items():
    subprocess.run([f"./{sender_exe}", str(num), name], capture_output=True, text=True)
    
    test = subprocess.run([f"./{receiver_exe}"], capture_output=True, text=True)
    
    if test.returncode != 0:
        print("Test failed to run\n")
        os.remove(sender_exe)
        os.remove(receiver_exe)
        sys.exit(1)

    if test.stdout.strip() != expected_output:
        print("Test expected output failed\n")
        os.remove(sender_exe)
        os.remove(receiver_exe)
        sys.exit(1)
    
    if os.path.exists("message.txt"):
        os.remove("message.txt")

# Test 2: failing tests
for (num, name), expected_output in failing_tests.items():
    subprocess.run([f"./{sender_exe}", str(num), name], capture_output=True, text=True)

    test = subprocess.run([f"./{receiver_exe}"], capture_output=True, text=True)

    if test.returncode != 0:
        print("Test failed to run\n")
        os.remove(sender_exe)
        os.remove(receiver_exe)
        sys.exit(1)

    if test.stdout.strip() != expected_output:
        print("Test expected output failed\n")
        os.remove(sender_exe)
        os.remove(receiver_exe)
        sys.exit(1)

    if os.path.exists("message.txt"):
        os.remove("message.txt")

# Test 3: no arguments - should fail
test = subprocess.run([f"./{sender_exe}"], capture_output=True, text=True)

if test.returncode != 1:
    print("No arguments test should fail with exit code 1\n")
    os.remove(sender_exe)
    os.remove(receiver_exe)
    sys.exit(1)

# Test 4: Not enough arguments - should fail
test = subprocess.run([f"./{sender_exe}", "123"], capture_output=True, text=True)

if test.returncode != 1:
    print("Wrong arguments test should fail with exit code 1\n")
    os.remove(sender_exe)
    os.remove(receiver_exe)
    sys.exit(1)


os.remove(exe_file)
os.system("/challenge/get_flag")