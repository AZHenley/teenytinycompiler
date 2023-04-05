import os
import subprocess
import sys

PYTHON = "python3"
COMPILER = "teenytiny.py"
CC = "gcc"


def comp(filename):
    bn = os.path.splitext(os.path.basename(filename))[0]
    tt_output = subprocess.run(
        [PYTHON, COMPILER, filename], capture_output=True, text=True)
    if tt_output.returncode != 0:
        print(tt_output.stderr)
    else:
        os.rename("out.c", f"{bn}.c")
        cc_output = subprocess.run(
            [CC, "-o", bn, f"{bn}.c"], capture_output=True, text=True)
        if cc_output.returncode != 0:
            print(cc_output.stderr)
        else:
            print(tt_output.stdout)


if len(sys.argv) == 1:
    for filename in os.listdir("examples"):
        if filename.endswith(".teeny"):
            comp(os.path.join("examples", filename))
else:
    comp(sys.argv[1])
