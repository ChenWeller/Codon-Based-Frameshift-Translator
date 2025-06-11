# Codon-Based-Frameshift-Translator
This Python project provides a tool to generate frameshifted protein sequences based on coding DNA sequences (CDS) from any organism. The user can select one or more specific codons where frameshifting should occur and define additional translation parameters

This Python project provides a tool to generate frameshifted protein sequences based on coding DNA sequences (CDS) from any organism. The user can select one or more specific codons where frameshifting should occur and define parameters such as:

Frameshift direction (+1, -1, -2)

Whether the shifted amino acid is included in the new sequence

How much of the upstream sequence is retained

Whether translation stops at a specific amino acid

Whether to trim based on enzymatic digestion sites (e.g., for proteomics)

This tool can help researchers or lab members simulate out-of-frame translation events or generate peptide databases for ribosome profiling, proteomics, or immunopeptidomics studies.

Why is this project useful?
Frameshifting is a biological process that can result in novel peptides, with relevance in viral infections, cancer, and translational regulation. This script automates what would otherwise be a manual and error-prone task: generating and curating potential out-of-frame peptides from genomic sequences.

This project is particularly useful for:

Researchers exploring non-canonical translation events

Bioinformaticians analyzing ribosome profiling data

Immunologists identifying potential cryptic epitopes

Peptidomics/proteomics labs needing custom peptide libraries

What kind of input and output does it expect?
Input
A FASTA file containing coding DNA sequences (CDS)

A codon of interest (e.g., CGA)

Optional: a CSV file listing specific genes to include

Output
A FASTA file containing translated peptides with the frameshift applied

Optionally, a non-redundant version of the file processed using cd-hit

Each output sequence is labeled with metadata including the codon position, direction of frameshift, site of shift, and truncated in-frame/out-of-frame sequences.

Example use cases
bash
Copy
Edit
python3 codon_frameshift.py \
  -f input_sequences.fasta \
  -c CGA \
  -s Asite \
  -di P1 \
  -da Peptidomics \
  -u 13 \
  -l chimeras \
  -st \
  -o output/frameshifted
This command shifts sequences at codon CGA, at the A-site, using a +1 frameshift, stops at the next codon matching the selected one, and writes output files to the output/ folder.

Technical setup
Requirements
Python 3.6+

Biopython

pandas

cd-hit (must be installed and accessible in system PATH)

Installation
bash
Copy
Edit
pip install biopython pandas
Install cd-hit via your package manager (e.g., apt, brew) or from source:
https://github.com/weizhongli/cdhit

Running the script
To run the script:

bash
Copy
Edit
python3 codon_frameshift.py -h
This will show all configurable options including codon, shift direction, translation length, and trimming behavior.

Notes
The tool removes sequences that are too short, contain ambiguous nucleotides (N), or do not start with a canonical start codon (ATG).

Duplicate sequences are automatically removed using cd-hit after processing.

The script supports both general and digestion-specific trimming logic (e.g., tryptic peptides for proteomics).

Known limitations
Only supports standard codon tables

Only FASTA inputs are supported (no GTF/GFF parsing for now)

Memory usage may increase with very large genomes

Future directions
GUI interface for codon selection and parameter tuning

Support for non-standard genetic codes

Integration with Ensembl REST API for automated genome fetching

This project was developed as part of a Python programming course project.
[[Course Repository → Insert Link Here]](https://github.com/Code-Maven/wis-python-course-2025-03)
