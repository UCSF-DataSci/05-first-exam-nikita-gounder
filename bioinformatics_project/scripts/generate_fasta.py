#!/usr/bin/env python3
"""
Generate Random FASTA Data 

# Command Line run:
# python3 generate_fasta.py
"""

import random

def random_fasta(seqlen=1000000):
    bases = ['A', 'C', 'G', 'T']
    sequence = "".join(random.choices(bases, k=seqlen))

    with open('/workspaces/05-first-exam-nikita-gounder/bioinformatics_project/data/random_sequence.fasta', 'w') as file:
        for base in range(0, len(sequence), 80):
            line = sequence[base:base+80]
            file.write(line + '\n') 

    print(f"Random DNA sequence generated and saved to bioinformatics_project/data/random_sequence.fasta")
 
           
      

if __name__ == "__main__":
    random_fasta()



