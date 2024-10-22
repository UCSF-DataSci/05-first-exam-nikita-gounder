#!/bin/bash

mkdir -p bioinformatics_project/{data,scripts,results}
touch bioinformatics_project/README.md
echo "Project structure is a main project directory: bioinformatics_project with 3 subdirectories." > bioinformatics_project/README.md
echo "Each subdirectory has corresponding python, text, and fasta files." >> bioinformatics_project/README.md

cd bioinformatics_project/scripts
touch generate_fasta.py dna_operations.py find_cutsites.py

cd /workspaces/05-first-exam-nikita-gounder/bioinformatics_project/results
touch cutsite_summary.txt

cd /workspaces/05-first-exam-nikita-gounder/bioinformatics_project/data
touch random_sequence.fasta

#make script executable with: chmod +x setup_project.sh
#run script: bash setup_project.sh