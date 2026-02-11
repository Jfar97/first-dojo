#!/usr/bin/exec-suid -- /usr/local/bin/python -I

edited_global = "SYMBOL ADDRESS=\"00104018\" NAME=\"pwned_var\" NAMESPACE=\"\" TYPE=\"global\" SOURCE_TYPE=\"USER_DEFINED\" PRIMARY=\"y\""        
edited_function = "SYMBOL ADDRESS=\"00101139\" NAME=\"pwnedfunction\" NAMESPACE=\"\" TYPE=\"global\" SOURCE_TYPE=\"USER_DEFINED\" PRIMARY=\"y\""      
edited_param = "REGISTER_VAR NAME=\"pwned_param\" REGISTER=\"EDI\" DATATYPE=\"undefined4\" DATATYPE_NAMESPACE=\"/\""     

global_edited = False
function_edited = False
param_edited = False

with open("/tmp/rename_challenge_completed.xml", "r", encoding="UTF-8") as file:
    for line in file:
        if edited_global in line:
            global_edited = True
        if edited_function in line:
            function_edited = True
        if edited_param in line:
            param_edited = True
        if global_edited and function_edited and param_edited:
            break


with open("/flag") as flag:
    print(flag.read())
#print("flag achieved")
