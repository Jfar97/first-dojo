#!/usr/bin/exec-suid -- /usr/local/bin/python -I

import os

Questions = [
    # 0
    "When you do 'file' on both the executables, it can be seen that 'gen-environment' has elevated priveleges. What indicates this is the case? ",
    # 1
    "Which of the two is a position independent executable (pie)? ",
    # 2
    "The 'gen-environment' executable uses the interpreter found in lib64, but where is the interpreter that the 'pwn-environment' executable uses? ",
    # 3
    "The 'gen-environment' executable is for GNU/Linux 3.2.0, while the 'pwn-college' executable is for GNU/Linux _?" ,
    # 4
    "Do these executables contain the same number of strings?",
    # 5
    "The first four hex of the 'pwn-environment' magic number are '7f 45 4c 46', and the first four hex of 'gen-environment' are _? ",
    # 6
    "'gen-environment' has _ strings in it, and 'pwn-environment' has _ strings in it? (enter two number seperated by a comma and space)? ",
    # 7
    "Using readelf on both executables, you can see that one has an additional section in its header called 'Type:'. What is the type of this executable? (Enter three letters) ",
    # 8
    "The entry point address for 'pwn-environment' is, and the entry point address for 'gen-environment' is? (seperate both addresses by a comma and a space) ",
    # 9
    "'pwn-environment' has _ program headers, and 'gen-environment' has _ program headers? (enter numbers seperated by a comma and space) ",
    # 10
    "For 'pwn-environment' the size of the program headers is _ bytes, and for 'gen-environment' the size of the program headers is _ bytes? (enter numbers seperated by a comma and space) ",
    # 11
    "In 'pwn-environment' there are _ columns in the 'Sections:' portion, and in 'gen-environment' there are _ columns in the 'Sections:' portion? (enter numbers seperated by a comma and space) ",
    # 12
    "From objdump the 'flags' value for 'pwn-environment' is _, and for 'gen-environment' the 'flags' value is _? (enter answers seperated by comma and a space) ",
    # 13
    "What are the three flags in 'pwn-environment' after 'flags 0x00000112: _ _ _'? (enter three strings seperated each seperated by a comma and a space) ",
    # 14
    "What are the three flags in 'gen-environment' after 'flags 0x00000150: _ _ _'? (enter three strings seperated each seperated by a comma and a space) ",


]


Answers = [
    # 0
    "setuid",
    # 1
    "gen-environment",
    # 2
    "nix",
    # 3
    "3.10.0",
    # 4
    "No",
    # 5
    "7f 45 4c 46",
    # 6
    "69, 62",
    # 7
    "DYN",
    # 8
    "0x401020, 0x1040",
    # 9
    "13, 14",
    # 10
    "56, 56",
    # 11
    "24, 26",
    # 12
    "0x00000112, 0x00000150",
    # 13
    "EXEC_P, HAS_SYMS, D_PAGED",
    # 14
    "HAS-SYMS, DYNAMIC, D_PAGED",
]


i = 0
while i < 15:
	question = Questions[i]
	user_answer = input(question)
	if user_answer != Answers[i]:
		print("Incorrect, please try again\n")
	else:
		i += 1;


with open("/flag") as f:
    print(f.read())
