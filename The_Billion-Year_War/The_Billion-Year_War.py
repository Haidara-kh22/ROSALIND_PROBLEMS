def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(dna))

def parse_fasta(fasta_lines):
    # Assuming the input is in FASTA format
    return ''.join(line.strip() for line in fasta_lines if not line.startswith('>'))

def find_reverse_palindromes(dna):
    results = []
    length = len(dna)

    for start in range(length):
        for l in range(4, 13):  # Lengths from 4 to 12
            if start + l <= length:
                substring = dna[start:start + l]
                if substring == reverse_complement(substring):
                    results.append((start + 1, l))  # Store 1-based index

    return results

# Sample input in FASTA format
file_path = r"D:\Rosalind\The_Billion-Year_War\rosalind_revp.txt"
with open(file_path, 'r') as fasta_input:
    fasta_lines = fasta_input.readlines()

# Parse the input and find reverse palindromes
dna_string = parse_fasta(fasta_lines)  # Fixed this line
palindromes = find_reverse_palindromes(dna_string)

# Print the results
for position, length in palindromes:
    print(position, length)
