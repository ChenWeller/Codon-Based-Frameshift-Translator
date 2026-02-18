# Changelog

All notable changes to this project are documented in this file.

## 2026-02-18
- Added output filtering: peptides shorter than 8 amino acids are removed from final FASTA output. The script prints a summary (how many removed and how many written).
- Updated `codon_translation.py` to collect generated peptides, apply the 8‑AA filter, and report warnings when no peptides pass the threshold.
- Clarified `-u/--upstream` units in documentation: the code treats the upstream value as an amino‑acid count.
- Updated `documentation.txt` with notes about upstream units and the new filtering behavior.
- Added `run_codonshift_lsf.sh` — an example LSF submission script to run the pipeline on the cluster (creates timestamped output folder and writes logs).

## Notes
- If you prefer a different minimum peptide length, edit the `min_len` variable in `codon_translation.py`.
- The `-u/--upstream` parameter currently functions as an AA count; to supply nucleotides divide by 3 before passing.
