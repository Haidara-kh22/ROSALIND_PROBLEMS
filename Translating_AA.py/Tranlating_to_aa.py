# Define the RNA codon table
codon_table = {
    'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'UAU': 'Y',
    'UAC': 'Y', 'UGU': 'C', 'UGC': 'C', 'UGA': '',   # Stop codon
    'UGG': 'W', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L',
    'CUG': 'L', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P',
    'CCG': 'P', 'CAU': 'H', 'CAC': 'H', 'CAA': 'Q',
    'CAG': 'Q', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R',
    'CGG': 'R', 'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
    'AUG': 'M', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T',
    'ACG': 'T', 'AAU': 'N', 'AAC': 'N', 'AAA': 'K',
    'AAG': 'K', 'AGU': 'S', 'AGC': 'S', 'AGA': 'R',
    'AGG': 'R', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V',
    'GUG': 'V', 'GCU': 'A', 'GCC': 'A', 'GCA': 'A',
    'GCG': 'A', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E',
    'GAG': 'E', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G',
    'GGG': 'G'
}

def read_rna_from_file(file_path):
    with open(file_path, 'r') as file:
        rna_sequence = file.read().strip()
    return rna_sequence

def translate_rna_to_protein(rna_sequence):
    protein = []
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
        if codon in codon_table:
            amino_acid = codon_table[codon]
            if amino_acid == '':
                break  # Stop codon
            protein.append(amino_acid)
    return ''.join(protein)

# Main execution
file_path = r'D:\Rosalind\rosalind_prot.txt'  
rna_seq = read_rna_from_file(file_path)  
protein_string = translate_rna_to_protein(rna_seq)
print(protein_string)
