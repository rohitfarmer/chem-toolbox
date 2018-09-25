#!/usr/bin/env python

'''
Purpose: To extract a subset of mols from a long SDF file.
extract_sdf.py -h for usage.
'''

# Standard Library.
import argparse

def extract_sdf(i, o, n):
	'''
	Extract a subset of mols from a long SDF file.
	extract_sdf <input file name> <output file name> <number>
	'''
	count = 0

	# Open an outfile.
	outfile = open(o, 'w')

	# Read and write n number of molecules from the input file.
	with open(i, 'r') as file:
		for line in file:
			outfile.write(line)
			if line.rstrip() == '$$$$':
				count += 1
			if count == n:
				break

	# Close the output file handle.
	outfile.close()

if __name__ == '__main__':
	# Argument parser.
	parser = argparse.ArgumentParser(description="Extract a subset of mols from a long SDF file.")
	parser.add_argument("i", help="Input file name.")
	parser.add_argument("o", help="Output file name.")
	parser.add_argument("n", help="Number of molecules to return.", type=int)
	args = parser.parse_args()

	extract_sdf(args.i, args.o, args.n)

