import subprocess
import sys
import os

# Paths to the input and output directories (adjust these paths as needed)
input_fasta = "test_data/input/test.fasta"
output_fasta = "test_data/output/frameshifted.fasta"
deduplicated_fasta = "test_data/output/deduplicated_sequences.fasta"

# Path to the Python scripts (adjust the paths if needed)
codon_translation_script = 'codon_translation.py'
redundancy_removal_script = 'rm_redundant.py'

# Function to ensure output directory exists
def ensure_output_directory_exists(output_file):
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        print(f"Creating output directory: {output_dir}")
        os.makedirs(output_dir)

# Function to call rm_redundant.py to remove redundant sequences
def run_rm_redundant(input_file, output_file):
    try:
        print("Running redundancy removal...")
        subprocess.run(['python', redundancy_removal_script, input_file, output_file], check=True)
        print("Redundancy removal completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error during redundancy removal: {e}")
        sys.exit(1)

# Function to call the main codon_translation.py script
def run_codon_translation(input_file, output_file, stop_aa_flag=False):
    try:
        print("Running codon translation...")
        
        # Update the command to exclude -da (Peptidomics/Proteomics argument)
        cmd = [
            'python', codon_translation_script, 
            '-f', input_file, 
            '-c', 'TTC',  # Example codon
            '-s', 'Asite', 
            '-di', 'P1', 
            '-u', '13', #13 sugegsted to Class-I, 24 to class-II
            '-l', 'chimeras', 
            '-o', output_file
        ]
        
        # Add '-st' to the command line only if stop_aa_flag is True
        if stop_aa_flag:
            cmd.append('-st')

        subprocess.run(cmd, check=True)
        print("Codon translation completed successfully!")
        
    except subprocess.CalledProcessError as e:
        print(f"Error during codon translation: {e}")
        sys.exit(1)

# Function to delete the deduplicated file after translation
def delete_deduplicated_file():
    if os.path.exists(deduplicated_fasta):
        os.remove(deduplicated_fasta)
        print(f"Deleted {deduplicated_fasta} after processing.")

# Main function to handle the entire pipeline
def run_project():
    # Ensure output directory exists before starting
    ensure_output_directory_exists(output_fasta)

    # First, run redundancy removal (remove duplicates)
    run_rm_redundant(input_fasta, deduplicated_fasta)

    # Then, call the codon translation script on the deduplicated file
    run_codon_translation(deduplicated_fasta, output_fasta)

    # After translation is done, delete the deduplicated file
    delete_deduplicated_file()

if __name__ == "__main__":
    run_project()
