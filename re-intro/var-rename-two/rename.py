#@runtime Jython
from ghidra.framework.model import DomainObjectListener
from java.lang import Thread

# Globals
VAR_TARGET_ADDR = toAddr(0x00104018)
FUNC_TARGET_ADDR = toAddr(0x00101139)

VAR_EXPECTED_NAME = "pwned_var"
PARAM_EXPECTED_NAME = "pwned_param"
FUNC_EXPECTED_NAME = "pwnedfunction"

done_var = False
done_parameter = False
done_function = False

print("In this challenge, you will have to rename several parts of the binary in order to get the flag.")
print("The first portion of the executable you should rename is the variable 'target'. Locate this variable inside of main and rename it to 'pwned_var'.")

    
class ProgListener(DomainObjectListener):
    def domainObjectChanged(self, ev):
        global done_var
        global done_parameter
        global done_function

        #print("change detected")

        if not done_var:
            sym = currentProgram.getSymbolTable().getPrimarySymbol(VAR_TARGET_ADDR)
            if sym and sym.getName() == VAR_EXPECTED_NAME:
                print("Correct change: %s -> %s" % (VAR_TARGET_ADDR, VAR_EXPECTED_NAME))
                print("Correct! You can also rename functionsjust like with variables. Locate the function named 'functiontarget' and rename it to 'pwnedfunction'.")
                done_var = True

        if done_var and not done_function:
            sym = currentProgram.getSymbolTable().getPrimarySymbol(FUNC_TARGET_ADDR)
            if sym and sym.getName() == FUNC_EXPECTED_NAME:
                print("Correct change: %s -> %s" % (FUNC_TARGET_ADDR, FUNC_EXPECTED_NAME))
                print("Correct! Finally, just like with variables declared outside of functions, you can also rename function parameters. Locate the parameter named 'parameter_target' in 'pwnedfunction' and rename it to 'pwned_param'.")
                done_function = True

        if done_function and not done_parameter:
            func = currentProgram.getFunctionManager().getFunctionAt(FUNC_TARGET_ADDR)
            if func:
                params = func.getParameters()
                if params and params[0].getName() == PARAM_EXPECTED_NAME:
                    print("Correct change: parameter -> %s" % (PARAM_EXPECTED_NAME))
                    done_parameter = True
    
listener = ProgListener()
currentProgram.addListener(listener)
#print("Monitoring: " + currentProgram.getName())
    
while not monitor.isCancelled() and not (done_var and done_parameter and done_function):
    Thread.sleep(1000)
    
currentProgram.removeListener(listener)
print("Monitoring stopped")
