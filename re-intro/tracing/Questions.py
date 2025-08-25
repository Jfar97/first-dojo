#!/usr/bin/exec-suid -- /usr/local/bin/python -I

import os
import random

Questions = [
	# 0
	"When you do 'run 1' in gdb and it crashes, what are the three rightmost characters of the address it crashes at?",
	# 1
	"When you do 'run 1' in gdb and it crashes, what are the three rightmost characters of the address it crashes at?",
	# 2
	"When you do 'run 3' in gdb and it crahses, what are the three rightmost characters of the address it crashes at?",
	# 3
	"When you do 'run 1 2' in gdb and it crahses, what is the exit code (exited with code _)?",
	# 4
	"When you do 'run abc' in gdb and it crahses, what is the exit code (exited with code _)?",
	# 5
	"When you do 'break func_a', what are the three rightmost characters of the address of the breakpoint?",
	# 6
	"When you do 'break func_b', what are the three rightmost characters of the address of the breakpoint?",
	# 7
	"When you do 'break func_c', what are the three rightmost characters of the address of the breakpoint?",
	# 8
	"When you do 'break func_d', what are the three rightmost characters of the address of the breakpoint?",
	# 9
	"When you do 'break func_e', what are the three rightmost characters of the address of the breakpoint?",
	# 10
	"When you do 'break main', what are the three rightmost characters of the address of the breakpoint?",
	# 11
	"When you have breakpoints at all five functions and main (six total), what is the first breakpoint hit when you do 'run 1' (enter the number)?",
	# 12
	"When you have breakpoints at all five functions and main (six total), what is the second breakpoint hit when you do 'run 1' (enter the number)?",
	# 13
	"When you have breakpoints at all five functions and main (six total), what is the second breakpoint hit when you do 'run 2' (enter the number)?",
	# 14
	"When you have breakpoints at all five functions and main (six total), what is the fifth breakpoint hit when you do 'run 2' (enter the number)?",
	# 15
	"When you have breakpoints at all five functions and main (six total), when you do 'run 2' how many times is breakpoint 3 hit (enter the number)?",
	# 16
	"When you do 'run 1' and it crashes, what is the signal and crash type (Program terminated with signal _, _ _)?",
	#17
	"When you do 'run 2' and it crashes, what is the signal and crash type (Program terminated with signal _, _ _)?",
	# 18
	"When you do 'run 2' and it crashes, what is the signal and crash type (Program terminated with signal _, _)?"
]

Answers = [
	# 0
	"1fa",
	# 1
	"1e2",
	# 2
	"ebc",
	# 3
	"01",
	# 4
	"071",
	# 5
	"16d",
	# 6
	"17e",
	# 7
	"1b0",
	# 8
	"1d7",
	# 9
	"1ee",
	# 10
	"207",
	# 11
	"6",
	# 12
	"5",
	# 13
	"1",
	# 14
	"3",
	# 15
	"5",
	#16
	"SIGSEGV, Segmentation fault",
	#17
	"SIGFPE, Arithmetic exception",
	# 18
	"SIGABRT, Aborted"
]

i = 0
while i < 19:
	question = Questions[i]
	user_answer = input(question)
	if user_answer != Answers[i]:
		print("Incorrect, please try again\n")
	else:
		i += 1;


with open("/flag") as f:
    print(f.read())
