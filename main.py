#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import functions

if __name__ == "__main__":
	if len(sys.argv) > 1:
		if sys.argv[1] == "-h" or sys.argv[1] == "--help":
			functions.help()
			sys.exit(0)
	import gui.main