N=input('enter name of sequence: ')
S=open(N)
seq=S.read()
seq_list= list(seq)

for n in range (len(seq_list)):
    if seq_list[n]=='T':
        seq_list[n]='U'
new_seq = ''.join(seq_list)

print(new_seq)
