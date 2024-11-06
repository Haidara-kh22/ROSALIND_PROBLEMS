def calculate_gc_content(dna):
    g_count = dna.count('G')
    c_count = dna.count('C')
    total_length = len(dna)
    if total_length == 0:
        return 0
    return (g_count + c_count) / total_length * 100

def parse_fasta(fasta_lines):
    fasta_dict = {}
    current_label = ""
    current_sequence = []

    for line in fasta_lines:
        line = line.strip()
        if line.startswith('>'):
            if current_label:  # Save the previous entry
                fasta_dict[current_label] = ''.join(current_sequence)
            current_label = line[1:]  # Get the label without '>'
            current_sequence = []  # Reset for new sequence
        else:
            current_sequence.append(line)  # Append sequence lines

    if current_label:  # Save the last entry
        fasta_dict[current_label] = ''.join(current_sequence)

    return fasta_dict

def find_highest_gc_content(fasta_lines):
    fasta_dict = parse_fasta(fasta_lines)
    max_gc_content = 0
    max_gc_label = ""

    for label, sequence in fasta_dict.items():
        gc_content = calculate_gc_content(sequence)
        if gc_content > max_gc_content:
            max_gc_content = gc_content
            max_gc_label = label

    return max_gc_label, max_gc_content

# Example input
file_path = r"D:\Rosalind\Computing GC Content\rosalind_gc.txt"
with open(file_path, 'r') as fasta_input:
    fasta_lines = fasta_input.readlines()

# Run the function and print results
label, gc_content = find_highest_gc_content(fasta_lines)
print(label)
print(f"{gc_content:.6f}")
