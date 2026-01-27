#@runtime Jython
from ghidra.framework.model import DomainObjectListener
from java.lang import Thread

# Globals
TARGET_ADDR = toAddr(0x00104018)
EXPECTED_NAME = "secret"

done = False
    
class MyListener(DomainObjectListener):
    def domainObjectChanged(self, ev):
        global done
        print("change detected")

        sym = currentProgram.getSymbolTable().getPrimarySymbol(TARGET_ADDR)
        if sym and sym.getName() == EXPECTED_NAME:
            print("Correct change: %s -> %s" % (TARGET_ADDR, EXPECTED_NAME))
            done = True
    
listener = MyListener()
currentProgram.addListener(listener)
print("Monitoring: " + currentProgram.getName())
    
while not monitor.isCancelled() and not done:
    Thread.sleep(1000)
    
currentProgram.removeListener(listener)
print("Monitoring stopped")