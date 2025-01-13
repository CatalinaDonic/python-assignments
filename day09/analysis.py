import argparse
from Bio import SeqIO

# Function that finds the longest repeated subsequence
def find_longest_repeated_subsequence(sequence):
    print(f"Processing sequence: {sequence[:50]}...")  # Show the first 50 characters of the sequence
    n = len(sequence)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    result = ""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if sequence[i - 1] == sequence[j - 1] and i != j:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > len(result):
                    result = sequence[i - dp[i][j]:i]
            else:
                dp[i][j] = 0
    
    return result

# Function to search for a CTCF binding site in the sequence
def find_motif(sequence, motif="CCCTC"):
    indices = []
    start = 0
    while True:
        pos = sequence.find(motif, start)
        if pos == -1:
            break
        indices.append(pos)
        start = pos + 1
    return indices

# Main function to handle user input
def main():

    parser = argparse.ArgumentParser(description="Analyze genomic sequence.")
    parser.add_argument("file", help="Path to the input file in Fasta or GeneBank format.")
    parser.add_argument("--duplicate", action="store_true", help="Find the longest repeated subsequence.")
    parser.add_argument("--motif", action="store_true", help="Search for the CCCTC motif.")
    args = parser.parse_args()



    try:
        for record in SeqIO.parse(args.file, "fasta"):
            sequence = str(record.seq)

            if args.duplicate:
                lrs = find_longest_repeated_subsequence(sequence)
                print(f"Longest repeated subsequence: {lrs}")

            if args.motif:
                motif_positions = find_motif(sequence)
                if motif_positions:
                    print(f"Motif CCCTC found at positions: {motif_positions}")
                else:
                    print("Motif CCCTC not found.")

    except Exception as e:
        print(f"Error reading file: {e}")


if __name__ == "__main__":
    main()