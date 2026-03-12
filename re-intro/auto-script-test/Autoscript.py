#@runtime Jython
from ghidra.framework.model import DomainObjectListener

class MyListener(DomainObjectListener):
    def domainObjectChanged(self, ev):
        print("change detected")

listener = MyListener()
currentProgram.addListener(listener)
print("Monitoring: " + currentProgram.getName())
