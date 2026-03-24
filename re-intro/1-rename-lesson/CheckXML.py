#!/usr/bin/exec-suid -- /usr/local/bin/python -I
import os

curr_dir = os.path.dirname(os.path.abspath(__file__))
addresses_file_path = os.path.join(curr_dir, "addresses.txt")

global_target_addr = ""
function_target_addr = ""

with open(addresses_file_path, "r") as f:
    global_target_addr = f.readline().strip()
    function_target_addr = f.readline().strip()

edited_global = f"SYMBOL ADDRESS=\"{global_target_addr}\" NAME=\"pwned_var\" NAMESPACE=\"\" TYPE=\"global\" SOURCE_TYPE=\"USER_DEFINED\" PRIMARY=\"y\""        
edited_function = f"SYMBOL ADDRESS=\"{function_target_addr}\" NAME=\"pwnedfunction\" NAMESPACE=\"\" TYPE=\"global\" SOURCE_TYPE=\"USER_DEFINED\" PRIMARY=\"y\""      
edited_param = "REGISTER_VAR NAME=\"pwned_param\" REGISTER=\"EDI\" DATATYPE=\"undefined4\" DATATYPE_NAMESPACE=\"/\""     

global_edited = False
function_edited = False
param_edited = False

with open("/tmp/rename_challenge_completed.xml", "r", encoding="UTF-8") as file:
    for line in file:
        if edited_global in line:
            if(not global_edited):
                print("Global variable renamed correctly!")
                global_edited = True
        if edited_function in line:
            if(not function_edited):
                print("Function renamed correctly!")
                function_edited = True
        if edited_param in line:
            if(not param_edited):
                print("Parameter renamed correctly!")
                param_edited = True
        if global_edited and function_edited and param_edited:
            break

#print("euid:", os.geteuid())
if global_edited and function_edited and param_edited:
    with open("/flag", "r") as flag:
        print(flag.read())
else:
    print("INCORRECT")
