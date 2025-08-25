#!/usr/bin/exec-suid -- /usr/local/bin/python -I

import os
import random

Questions = [
	#0
	"When you do 'file /challenge/challenge', at the end is the executable stripped or not stripped?",
	# 1
	"When you do 'readelf -h /challenge/challenge', what is the class?",
	# 2
	"When you do 'readelf -h /challenge/challenge', does the executable use little endian or big endian?",
	# 3
	"When you do 'readelf -h /challenge/challenge', what is the entry point address?",
	# 4
	"When you do 'readelf -h /challenge/challenge', how many bytes into the file does do the program headers start? (enter a number)",
	# 5
	"When you do 'readelf -h /challenge/challenge', what is the size in bytes of the program headers? (enter a number)",
	# 6
	"When you do 'objdump -x /challenge/challenge', what does it say next to the file format?",
	# 7
	"When you do 'objdump -x /challenge/challenge', what does it say after 'architecture:' (up to the comma before 'flags')?",
	# 8
	"When you do 'objdump -x /challenge/challenge', what is after the 'Program Header:' portion and before the 'Version References:' portion?",
	# 9
	"When you do 'objdump -x /challenge/challenge', how many rows are there in the 'Sections:' portion? (enter a number)",
	# 10
	"When you do 'strings /challenge/challenge', what is the first string listed?",
	# 11
	"When you do 'strings /challenge/challenge', what is the fifth string listed?",
	# 12
	"When you do 'hexdump -C -n 64 /challenge/challenge', what are the first four hex values making up the magic number? (put a space between them)",
	# 13 
	"When you do 'hexdump -C -n 64 /challenge/challenge', what are the last four hex values on the address line 00000030? (put a space between them)"

]

Answers = [
	#0
	"not stripped",
	# 1
	"ELF64",
	# 2 
	"little endian",
	# 3
	"0x1080",
	# 4
	"64", 
	# 5
	"56", 
	# 6
	"elf64-x86-64", 
	# 7
	"i386:x86-64", 
	# 8
	"Dynamic Section",
	# 9
	"27",
	# 10
	"/lib64/ld-linux-x86-64.so.2",
	# 11
	"__libc_start_main",
	# 12
	"7f 45 4c 46",
	# 13
	"1f 00 1e 00"
]


i = 0
while i < 14:
	question = Questions[i]
	user_answer = input(question)
	if user_answer != Answers[i]:
		print("Incorrect, please try again\n")
	else:
		i += 1;


with open("/flag") as f:
    print(f.read())