#N=input('enter name of sequence: ')
S=open("rosalind_rna.txt")
seq=S.read()
seq_list= list(seq)

for n in range (len(seq_list)):
    if seq_list[n]=='T':
        seq_list[n]='A'
    if seq_list[n]=='G':
        seq_list[n]='C'
    if seq_list[n]=='A':
        seq_list[n]='T'
    if seq_list[n]=='C':
        seq_list[n]='G'
reversed_seq=reversed(seq_list)
new_seq = ''.join(reversed_seq)

print(new_seq)