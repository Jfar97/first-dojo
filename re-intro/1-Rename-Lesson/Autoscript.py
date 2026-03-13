#@runtime Jython

from ghidra.framework.model import DomainObjectListener
from ghidra.app.util.exporter import XmlExporter
from java.io import File
import subprocess

addresses_file_path = "/challenge/addresses.txt"

with open(addresses_file_path, "r") as f:
    VAR_TARGET_ADDR = toAddr(int(f.readline().strip(), 16))
    FUNC_TARGET_ADDR = toAddr(int(f.readline().strip(), 16))

VAR_EXPECTED_NAME = "pwned_var"
PARAM_EXPECTED_NAME = "pwned_param"
FUNC_EXPECTED_NAME = "pwnedfunction"

done_var = False
done_parameter = False
done_function = False

print("In this challenge, you will have to rename several parts of the binary in order to get the flag.")
print("The first portion of the executable you should rename is the variable 'global_target'. Locate this variable inside of main and rename it to 'pwned_var'.")

class ProgListener(DomainObjectListener):
    def domainObjectChanged(self, ev):
        global done_var
        global done_parameter
        global done_function
        global listener

        if not done_var:
            sym = currentProgram.getSymbolTable().getPrimarySymbol(VAR_TARGET_ADDR)
            if sym and sym.getName() == VAR_EXPECTED_NAME:
                print("Correct! You can also rename functions just like with variables. Locate the function named 'functiontarget' and rename it to 'pwnedfunction'.")
                done_var = True
            return

        if done_var and not done_function:
            sym = currentProgram.getSymbolTable().getPrimarySymbol(FUNC_TARGET_ADDR)
            if sym and sym.getName() == FUNC_EXPECTED_NAME:
                print("Correct! Finally, just like with variables declared outside of functions, you can also rename function parameters. Locate the parameter of 'pwnedfunction' and rename it to 'pwned_param'.")
                done_function = True
            return

        if done_function and not done_parameter:
            func = currentProgram.getFunctionManager().getFunctionAt(FUNC_TARGET_ADDR)
            if func:
                params = func.getParameters()
                if params and params[0].getName() == PARAM_EXPECTED_NAME:
                    print("Correct! You have successfully completed the rename challenge")
                    done_parameter = True

                    currentProgram.removeListener(listener)

                    program = getCurrentProgram()
                    exporter = XmlExporter()
                    output_file = File("/tmp/rename_challenge_completed.xml")
                    exporter.export(output_file, program, None, getMonitor())

                    result = subprocess.Popen(
                        ['/challenge/CheckXML.py'],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE
                    )
                    out, err = result.communicate()

                    print(out)
                    print(err)
            return

listener = ProgListener()
currentProgram.addListener(listener)
print("Monitoring: " + currentProgram.getName())
