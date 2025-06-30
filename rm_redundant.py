from Bio import SeqIO
import sys

def remove_redundant_sequences(input_file, output_file, identity_threshold=0.9):
    """
    Remove redundant sequences based on sequence identity threshold.
    Sequences with >= identity_threshold similarity will be considered duplicates and removed.

    :param input_file: Input FASTA file path.
    :param output_file: Output FASTA file path for writing the deduplicated sequences.
    :param identity_threshold: The identity threshold (default: 0.9 for 90% similarity).
    """
    sequences = list(SeqIO.parse(input_file, "fasta"))
    unique_sequences = []
    seen = set()

    # Compare all sequences pairwise
    for i, seq1 in enumerate(sequences):
        is_unique = True
        for seq2 in unique_sequences:
            if calculate_identity(seq1.seq, seq2.seq) >= identity_threshold:
                is_unique = False
                break
        if is_unique:
            unique_sequences.append(seq1)

    # Write the unique sequences to the output file
    with open(output_file, "w") as out_file:
        SeqIO.write(unique_sequences, out_file, "fasta")

    print(f"Deduplicated sequences written to {output_file}")

def calculate_identity(seq1, seq2):
    """
    Calculate the sequence identity between two sequences.
    The identity is calculated as the percentage of matching positions.
    
    :param seq1: The first sequence (BioPython Seq object).
    :param seq2: The second sequence (BioPython Seq object).
    :return: Identity percentage (0 to 1).
    """
    matches = sum(1 for a, b in zip(seq1, seq2) if a == b)
    return matches / max(len(seq1), len(seq2))

# Get input and output files from arguments
if __name__ == "__main__":
    input_file = sys.argv[1]  # Input file path
    output_file = sys.argv[2]  # Output file path
    remove_redundant_sequences(input_file, output_file)
