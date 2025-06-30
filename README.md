# Codon-Based Frameshift Translator

### The key to run the pipeline is to modify the config.py according to the user needs and research question. ###
## We strongly recommend to run the test data, read the README and documentation files before proceeding ##

[![Python version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Table of Contents
- [What does this project do?](#what-does-this-project-do)
- [Why is this project useful?](#why-is-this-project-useful)
- [What kind of input and output does it expect?](#what-kind-of-input-and-output-does-it-expect)
- [Test Data](#test-data)
- [Technical setup](#technical-setup)
- [Installation](#installation)
- [Usage](#usage)
- [Example use cases](#example-use-cases)
- [config.py: Explanation and Parameters](#configpy-explanation-and-parameters)
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
- **Bioinformaticians** analyzing proteomic data.
- **Immunologists** identifying cryptic epitopes.
- **Peptidomics/proteomics labs** needing custom peptide libraries.

## What kind of input and output does it expect?

### Input
- The key to run the pipeline is to modify the config.py according to the user needs and research question.
- A **FASTA file** containing coding DNA sequences (CDS).
- A **codon of interest** (e.g., `CGA`).
- Optional: a **CSV file** listing specific genes to include in the processing.

### Output
- A **FASTA file** containing translated peptides with the frameshift applied.
- A detailed **FASTA header** for each query (see documentation)

Each output sequence is labeled with metadata including:
- The **codon position** where the frameshift occurred.
- The **direction of the frameshift** (e.g., `+1`, `-1`, `-2`).
- The **site of the shift** (e.g., A-site, P-site).
- **Truncated in-frame/out-of-frame sequences** for downstream analysis.

## Test Data

To test the tool, you can use the provided **test data** included in the `test_data` folder. This folder contains:
1. **input_sequences.fasta**: A sample FASTA file with some coding DNA sequences (CDS).
2. **expected_output.fasta**: The expected output file after running the tool with the test data, showing frameshifted peptides.

To run the pipeline with the test data:
1. Place the test FASTA file in the `test_data/input/` folder.
2. Run the pipeline with the following command:

    ```plaintext
    python3 config.py
    ```

3. Check the output file in the `test_data/output/` folder.

## Technical setup

### Requirements
Before running the script, make sure you have the following installed:

- Python 3.6 or higher
- Required Python libraries:
  ```bash
  pip install biopython pandas


### Installation
Clone this repository:
git clone https://github.com/ChenWeller/Codon-Based-Frameshift-Translator.git
cd Codon-Based-Frameshift-Translator

Install Python dependencies:
pip install -r requirements.txt

### Running the Script
To run the frameshift translation script:
Format the config.py file to match your needs.
Then run python3 config.py

This will generate frameshifted sequences for the provided input file.

## config.py: Explanation and Parameters

### What does config.py do?
The config.py file is the main entry point for running the pipeline. It manages two key steps:

1. **Redundancy Removal**: Removes any redundant sequences from the input FASTA file.
2. **Codon Translation**: Runs the frameshift translation script (`codon_translation.py`) to generate the frameshifted peptide sequences.

### Parameters in config.py:

#### Paths:
- **input_fasta**: Path to the input FASTA file containing CDS sequences.
- **output_fasta**: Path to save the frameshifted peptides output.
- **deduplicated_fasta**: Path to save the deduplicated sequences.
- **codon_translation_script**: Path to the script that generates frameshifted peptides (`codon_translation.py`).
- **redundancy_removal_script**: Path to the redundancy removal script (`rm_redundant.py`).

#### Functions:
- **ensure_output_directory_exists(output_file)**: Ensures the output directory exists.
- **run_rm_redundant(input_file, output_file)**: Calls the redundancy removal script.
- **run_codon_translation(input_file, output_file, stop_aa_flag=False)**: Calls the codon translation script.
- **delete_deduplicated_file()**: Deletes the temporary deduplicated file after translation.
- **run_project()**: The main function that runs the entire pipeline.

To customize the behavior, you can adjust the paths and parameters in this file.

### Troubleshooting

If you encounter errors related to biopython or pandas, ensure all dependencies are correctly installed via pip.

## Known limitations
- Only supports standard codon tables.
- Only FASTA inputs are supported (no GTF/GFF parsing for now).
- Memory usage may increase with very large genomes.

## Future directions
- GUI interface for codon selection and parameter tuning.
- Support for non-standard genetic codes.
- Integration with Ensembl REST API for automated genome fetching.


## This project was developed as part of the Python programming course at the Weizmann Institute of Science  
https://github.com/Code-Maven/wis-python-course-2025-03
