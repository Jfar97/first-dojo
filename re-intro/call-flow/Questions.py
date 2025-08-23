#!/usr/bin/exec-suid -- /usr/local/bin/python -I

import os
import random

Questions = [
	# 0 
	"How many functions call two other functions? (Enter answer as a number) ",
	# 1
	"What function is called second inside of main? ",
	# 2
	"Which function does not call any functions? ",
	# 3
	"Which function besides main calls func_a? ",
	# 4
	"What value does main return? (Enter answer as a number) ",
	# 5
	"What function does func_b call? ",
	# 6
	"What is the first function that func_c calls? ",
	# 7
	"Which function besides func_e calls func_h? ",
	# 8 
	"Which function does func_g call? ",
	# 9
	"Which function calls func_c? "
]

Answers = [
	# 0 
	"3",
	# 1
	"func_e",
	# 2
	"func_h",
	# 3
	"func_g",
	# 4
	"1337",
	# 5
	"func_c",
	# 6s
	"func_e",
	# 7
	"func_f",
	# 8 
	"func_a",
	# 9
	"func_b"
]


five_questions = random.sample(range(10), 5)

for i in five_questions:
	question = Questions[i]
	user_answer = input(question)
	if user_answer != Answers[i]:
		print("Incorrect, please try again")
		exit()

os.system("/challenge/get_flag")


