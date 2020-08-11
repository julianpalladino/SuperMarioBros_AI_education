#! /usr/bin/env python

from gamelib import main
import sys
from pdb import set_trace as st


assert  len(sys.argv) <= 2, "Too many arguments"

if len(sys.argv) == 1:
	lvl = int(input("Input number of level:"))
else:
	lvl = int(sys.argv[1])

sys.path.append("gamelib/")
main.main(lvl)
