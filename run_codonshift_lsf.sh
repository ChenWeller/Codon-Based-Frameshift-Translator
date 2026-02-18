#!/bin/bash

# LSF submission script for Codon-Based-Frameshift-Translator
# Submits a job that runs `codon_translation.py` on the mice FASTA in `input/`
# Settings: convert U->T (UCU -> TCT), site = emptyA, direction = P1, run OOF (translate until stop codon)

project='CodonShift_mice'
queue='gsla-cpu'
threads=20
mem_per_thread=10000

# Paths (relative to this script location)
PIPELINE_DIR="$(dirname "$0")"
INPUT_FASTA="${PIPELINE_DIR}/input/Mus_musculus.GRCm39.cds.all.fa"

# Convert RNA-style codon UCU to DNA-style TCT
TARGET_CODON="TCT"
SITE="emptyA"
DIRECTION="P1"
UPSTREAM=13
LENGTH="OOF"       # translate until stop codon
# Do not pass -st (stop_aa) since we want to run until stop codon

# Output: create a timestamped subfolder under pipeline `output/`
OUT_DIR="${PIPELINE_DIR}/output/codonshift_$(date +%Y%m%d_%H%M%S)"
mkdir -p "${OUT_DIR}"
OUT_PREFIX="${OUT_DIR}/CodonShift_mice"

# Logs
mkdir -p "${PIPELINE_DIR}/logs"

# Load modules (adjust if your cluster uses different module names)
module load HTSlib/1.19.1-GCC-13.2.0 || true

# Submit job
bsub -q "${queue}" \
     -J "${project}" \
     -oo "${PIPELINE_DIR}/logs/${project}.out" \
     -eo "${PIPELINE_DIR}/logs/${project}.err" \
     -n "${threads}" \
     -R "rusage[mem=${mem_per_thread}] span[ptile=${threads}]" \
     "bash -lc 'cd \"${PIPELINE_DIR}\" && python3 codon_translation.py -f \"${INPUT_FASTA}\" -c ${TARGET_CODON} -s ${SITE} -di ${DIRECTION} -u ${UPSTREAM} -l ${LENGTH} -o \"${OUT_PREFIX}\"'"

echo "Submitted job ${project} to queue ${queue}. Output will be placed under ${OUT_DIR} (final file: ${OUT_PREFIX}*.fasta)"
