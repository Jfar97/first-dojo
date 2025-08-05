#!/usr/bin/exec-suid -- /usr/local/bin/python -I
import os
import subprocess

# Debug: what can we see?
print("=== DEBUG INFO ===")
print("Current working directory:", os.getcwd())
print("PATH:", os.environ.get('PATH', 'NOT SET'))

# Try to find gcc
for path in ['/usr/bin/gcc', '/bin/gcc', '/usr/local/bin/gcc', '/run/workspace/bin/gcc']:
    if os.path.exists(path):
        print(f"Found gcc at: {path}")
    else:
        print(f"NOT found: {path}")

# Try to list some directories
try:
    print("/usr/bin contents:", os.listdir('/usr/bin')[:10])
except:
    print("Can't list /usr/bin")

try:
    print("/run/workspace/bin contents:", os.listdir('/run/workspace/bin')[:10])
except:
    print("Can't list /run/workspace/bin - IT DOESN'T EXIST IN EXEC-SUID!")
