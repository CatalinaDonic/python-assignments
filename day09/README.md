# Sequence Analysis Tool

This Python script provides tools to analyze genomic sequences. It supports two main analyses:

1. **Finding the longest repeated subsequence** in a sequence.
2. **Searching for a specific motif** (default: "CCCTC") within the sequence.

## Requirements

- `biopython`

## Usage

Run the script using the following format:

```bash
python analyze.py FILE [--duplicate] [--motif]
```

- `FILE`: Path to the input file in Fasta or GeneBank format.
- `--duplicate`: Finds the longest repeated subsequence in the sequence.
- `--motif`: Searches for the "CCCTC" motif within the sequence.

## Output

- For the `--duplicate` option, the script prints the longest repeated subsequence.
- For the `--motif` option, the script prints the positions of the motif occurrences, if found.
