#!/usr/bin/env python3
"""
Find Distant Cutsites in FASTA Data 

# Command Line run:
# python3 find_cutsites.py "/workspaces/05-first-exam-nikita-gounder/bioinformatics_project/data/random_sequence.fasta" "G|GATCC"
"""

import re
import argparse


def fasta_cutsites(fasta_path, cut_seq):

    with open(fasta_path, 'r') as ff:
        dna_sequence = ''.join(line.strip() for line in ff) #make all dna seq lines into one string

    cut_clean = cut_seq.replace('|', '')
    cut_occurrences = [match.start() for match in re.finditer(cut_clean, dna_sequence)] #find start indexes of matches

    cut_pairs = []
    for i in range(len(cut_occurrences)): #compare 1st value
        for j in range(i + 1, len(cut_occurrences)): #to 2nd value
            dist = cut_occurrences[j] - cut_occurrences[i] #calculate distance between the two start indexes
        
            if 80000 <= dist <= 120000:
                cut_pairs.append((cut_occurrences[i], cut_occurrences[j])) #append index values/positions to variable

    
    print(f"Analyzing cut site: {cut_seq}")
    print(f"Total cut sites found: {len(cut_occurrences)}")        
    print(f"Cut site pairs 80-120 kbp apart: {len(cut_pairs)}")
    print(f"First 5 pairs: {cut_pairs[:5]}")

    with open('/workspaces/05-first-exam-nikita-gounder/bioinformatics_project/results/cutsite_summary.txt', 'w') as file:
        file.write(f"Analyzing cut site: {cut_seq} \n")
        file.write(f"Total cut sites found: {len(cut_occurrences)} \n")
        file.write(f"Cut site pairs 80-120 kbp apart: {len(cut_pairs)} \n")
        file.write(f"First 5 pairs: {cut_pairs[:5]}")
        #add to txt summary file




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fasta_path", type=str, help="FASTA file path as a command-line argument")
    parser.add_argument("cut_seq", type=str, help="cut site sequence")
    arg = parser.parse_args()
    
    fasta_cutsites(arg.fasta_path, arg.cut_seq)



   