#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import functions
import classes.image as imgcls

if __name__ == "__main__":
	if len(sys.argv) > 1:
		file_path = ""
		output_path = ""
		radius = 8

		# You're about to see an abomination that should not exist, 
		# but since I didn't have enough time to finish this properly,
		# here is it anyway.
		
		if "-h" in sys.argv or "--help" in sys.argv:
			functions.help()
			sys.exit(0)

		if "-i" in sys.argv or "--input" in sys.argv:
			try:
				i = sys.argv.index('-i')
			except ValueError:
				i = sys.argv.index('--input')

			try:
				file_path = sys.argv[i + 1]
				print("Using file", file_path)
			except IndexError:
				sys.exit('Please provide a file path to the input parameter!')

			if "-o" in sys.argv or "--output" in sys.argv:
				try:
					i = sys.argv.index('-o')
				except ValueError:
					i = sys.argv.index('--output')

				try:
					output_path = sys.argv[i + 1]
					print("Output file is", output_path)
				except IndexError:
					sys.exit('Please provide a file path to the output parameter!')

			if "-r" in sys.argv or "--radius" in sys.argv:
				try:
					i = sys.argv.index('-r')
				except ValueError:
					i = sys.argv.index('--radius')

				try:
					radius = int(sys.argv[i + 1])
					print("Radius is", radius)
				except IndexError:
					sys.exit('Please provide a value to the radius parameter!')
		else:
			sys.exit('Please provide an input file!')

		if output_path == "":
			import pathlib
			output_path = file_path.replace(pathlib.Path(file_path).suffix, "_out" + pathlib.Path(file_path).suffix)

		out = imgcls.CustomImage(file_path, radius)

		if "-f" in sys.argv or "--full" in sys.argv:
			out.full_blur().save(output_path)
		elif "-a" in sys.argv or "--area" in sys.argv:
			try:
				i = sys.argv.index('-a')
			except ValueError:
				i = sys.argv.index('--area')

			try:
				out.region_blur((int(sys.argv[i + 1]), int(sys.argv[i + 2]), int(sys.argv[i + 3]), int(sys.argv[i + 4]))).save(output_path)
			except Exception as e:
				sys.exit('Please provide valid area parameters!')

	else:
		import gui.main