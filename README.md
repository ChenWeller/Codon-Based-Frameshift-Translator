# Codon-Based Frameshift Translator

[![Python version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Table of Contents
- [What does this project do?](#what-does-this-project-do)
- [Why is this project useful?](#why-is-this-project-useful)
- [What kind of input and output does it expect?](#what-kind-of-input-and-output-does-it-expect)
- [Technical setup](#technical-setup)
- [Installation](#installation)
- [Usage](#usage)
- [Example use cases](#example-use-cases)
- [Known limitations](#known-limitations)
- [Future directions](#future-directions)
- [This project was developed as part of the Python programming course](#this-project-was-developed-as-part-of-the-python-programming-course)

## What does this project do?

This Python project provides a tool to generate frameshifted protein sequences based on coding DNA sequences (CDS) from any organism. The user can select one or more specific codons where frameshifting should occur and define parameters such as:

- Frameshift direction (`+1`, `-1`, `-2`)
- Whether the shifted amino acid is included in the new sequence
- How much of the upstream sequence is retained
- Whether translation stops at a specific amino acid
- Whether to trim based on enzymatic digestion sites (e.g., for proteomics)

The tool is primarily designed for generating peptide databases that simulate out-of-frame translation events, which can be valuable in ribosome profiling, proteomics, or immunopeptidomics studies.

## Why is this project useful?

Frameshifting is a biological process that can result in novel peptides, which are highly relevant in various biological contexts such as viral infections, cancer, and translational regulation. This script automates the generation of potential out-of-frame peptides, a task that would otherwise be manual and error-prone. The tool saves time and ensures accuracy when analyzing coding sequences.

This project is particularly useful for:
- **Researchers** exploring non-canonical translation events.
- **Bioinformaticians** analyzing ribosome profiling data.
- **Immunologists** identifying cryptic epitopes.
- **Peptidomics/proteomics labs** needing custom peptide libraries.

## What kind of input and output does it expect?

### Input
- A **FASTA file** containing coding DNA sequences (CDS).
- A **codon of interest** (e.g., `CGA`).
- Optional: a **CSV file** listing specific genes to include in the processing.

### Output
- A **FASTA file** containing translated peptides with the frameshift applied.
- Optionally, a **non-redundant version** of the file processed using `cd-hit`.

Each output sequence is labeled with metadata including:
- The **codon position** where the frameshift occurred.
- The **direction of the frameshift** (e.g., `+1`, `-1`, `-2`).
- The **site of the shift** (e.g., A-site, P-site).
- **Truncated in-frame/out-of-frame sequences** for downstream analysis.

## Example use cases

### Command-line Example

#Python 3 codon_frameshift.py -f input_sequences.fasta -c CGA -s Asite -di P1 -da Peptidomics -u 13 -l chimeras -st -o output/frameshifted

## Testing the Script
To verify if everything is set up properly, run:

python3 codon_frameshift.py -h

This will display the help message and available parameters.

## Technical setup

### Requirements
Before running the script, make sure you have the following installed:

- Python 3.6 or higher
- Required Python libraries:
  pip install biopython pandas

The cd-hit program must be installed and accessible in your system's PATH.

### Installation
Clone this repository:
git clone https://github.com/ChenWeller/Codon-Based-Frameshift-Translator.git
cd Codon-Based-Frameshift-Translator

Install Python dependencies:
pip install -r requirements.txt

Install cd-hit:
Ensure cd-hit is installed on your system. You can install it using the package manager on Linux or via brew on macOS:

#### Ubuntu/Debian:
sudo apt install cd-hit

### Running the Script
To run the frameshift translation script, use the following command:
#python3 codon_frameshift.py \
  -f input_sequences.fasta \
  -c CGA \
  -s Asite \
  -di P1 \
  -da Peptidomics \
  -u 13 \
  -l chimeras \
  -st \
  -o output/frameshifted

This will generate frameshifted sequences for the provided input file.

### Troubleshooting
If you face issues with cd-hit, ensure it is correctly installed and available in the system’s PATH. You can check this by running:
cd-hit -v

If you encounter errors related to biopython or pandas, ensure all dependencies are correctly installed via pip.

## Known limitations
- Only supports standard codon tables.
- Only FASTA inputs are supported (no GTF/GFF parsing for now).
- Memory usage may increase with very large genomes.

## Future directions
- GUI interface for codon selection and parameter tuning.
- Support for non-standard genetic codes.
- Integration with Ensembl REST API for automated genome fetching.

## License
MIT License.

## This project was developed as part of the Python programming course at the Weizmann Institute of Science  
https://github.com/Code-Maven/wis-python-course-2025-03
