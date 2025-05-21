#!/bin/env python3

import sys
import subprocess
import os
from makerel.transformpath import TransformPath

def run_make(args: list[str]) -> subprocess.Popen:
    """
    Run the make command with the given arguments and capture its output.
    """
    process = subprocess.Popen(["make"] + args,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT,
                               text=True)
    return process



def main() -> None:
    # Run the make process and stream its output back to this script
    process = run_make(sys.argv[1:])

    # Scan through the lines and remap the paths
    trans = TransformPath(os.getcwd())
    type(process.stdout)
    for line in process.stdout:
        line = trans.transform_line(line)
        print(line, end='')

if __name__ == "__main__":
    main()
