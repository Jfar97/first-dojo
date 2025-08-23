#!/usr/bin/exec-suid -- /usr/local/bin/python -I

import os
import random

Answers = [
	#String 1
	"Make sure to get the checkpoints",
	#String 2
	"SenseAI is a really helpful tool",
	#String 3
	"Don't forget to do the surveys",
	#String 4
	"Be sure to check the discord",
	#STring 5
	"Sleep is key to success",
	#String 6
	"Be sure to eat before exams",
	#String 7
	"Help classmates for EC",
	#String 8
	"Quick breaks can be helpful",
	#String 9
	"I need another message",
	#String 10
	"and then one more too"
]

five_questions = random.sample(range(10), 5)

for i in five_questions:
	question = "What is the " + str(i+1) + " string declared in main? "
	user_answer = input(question)
	if user_answer != Answers[i]:
		print("Incorrect string")
		exit()

with open("/flag") as f:
    print(f.read())
		
