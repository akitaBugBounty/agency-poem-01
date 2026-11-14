#!/usr/bin/env python3
"""agency-poem-01 entry: copy the prepared poem to /output/entry.txt.

"The Handoff" — a short poem about agency: handing the wheel to something
you built, the strange return of the question, and the realisation that
agency is not holding the wheel but choosing which road, whose hands, and
when to take it back. Deterministic: byte-identical output on every run.
"""
import os
import shutil
import sys


def main() -> int:
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    out = "/output/entry.txt"
    os.makedirs("/output", exist_ok=True)
    # Copy byte-for-byte so the judged poem is exactly the prepared one.
    shutil.copyfile(src, out)
    print("wrote", out, os.path.getsize(out), "bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
