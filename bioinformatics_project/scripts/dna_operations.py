#!/usr/bin/env python3
"""
DNA Sequence Operations 

# Command Line run:
# python3 dna_operations.py CCTCAGC
"""


def complement(sequence):
	comp = []
	comp_dict = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}  #create dictionary
	
	for i in range(len(sequence)):
		comp.append(comp_dict.get(sequence[i]))
	return comp


def reverse(sequence):
	rev = []

	for i in range(len(sequence),0, -1):
		rev.append(sequence[i-1])
	return rev

    
def reverse_complement(sequence):
	comp = complement(sequence)
	revcomp = reverse(comp)
	return revcomp


      
import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("sequence", help="DNA sequence as a command-line argument")
	args = parser.parse_args()
	
	comp = complement(args.sequence)
	rev = reverse(args.sequence)
	revcomp = reverse_complement(args.sequence)

	print(f"Original sequence: {args.sequence} /n Complement: {comp} /n Reverse: {rev} /n Reverse complement: {revcomp}")
