#!/usr/bin/python3
import sys
sys.path.insert(0, '/challenge/pylibs')

import os
os.environ.setdefault("PYHIDRA_GHIDRA_PATH", "/run/dojo/bin/ghidra")

import pyghidra as pgh
pgh.start()
with pgh.open_project(sys.argv[1]) as proj:
    pdata = proj.getProjectData()
    root = pdata.getRootFolder()
    df = [f for f in root.getFiles() if f.getFileType() == "Program"][0]
    program = proj.openProgram(df)
    mem = program.getMemory()
    start = mem.getMinAddress()
    was = mem.findBytes(start, bytearray(b"absent"), 0, None)
    now = mem.findBytes(start, bytearray(b"present"), 0, None)
    if was is None and now is not None:
        print("flag{present_detected}")
    proj.close(program)
pgh.shutdown()
