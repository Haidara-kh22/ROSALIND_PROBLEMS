S='TCTTTGGAGGCTGGTTAGAAAAACAGTACTGTACTGCGGCTTAGTCATAGCTGCAGCGCTCGATTCCCGCTCGCCTACTTACCCCACTAAGGTCGAGAGCGGAAGTTGCCGTGCGGCTTTGTGAGCGGATTACCGTGCGTGGTTTACCGGAATAGGGTTATAATGCACATGGTTCTTCCTGCTTTATAGTACCTAGAGCTAACATGACTGCTTCCCTAAGCCGCGAGATTTGGTCGCACGGCATCGAACATATAAGAGGAGGGTCCCAGAAGGGTACTTGAACGTAATGCTTGTAGACCGATTCCAAATGGCTCGCTCGCGAGTTCCGATCTCATCACTGACCATTTAGCAACAGGGAAATGGCCGCAAAGTTATTTACTCGGGCACCACATAGACATCTATGGTTCCATCTGTGCATAACTAGGTCACTGCGTCGTCGGATCGATTCTTAATCGTCGTATTTGGGATTCTTATACCGCGTAATATCGGTTTGCCCTTGCGGCATGAATCGATTCCCTTCACCCGAAAGCGCCCAATACCCCGCTAAGGGGGCGAAATAGTGACTCAGTTTCTGTCCTCTACAAGTGGGCAGCCAACCAGCAAGCTGTTCATCCGGTTTGCCCAATGATACGCGGGGCACGCTATAGTCGGCCCTTGCAACCTGTGAGAGCTAGGTCAGGCGGTCACCCACTAATGTGATGCCCACAAGTCCATAACGTCTGTATCAGAAGCGCCAGAAGGAATCTACTCCCGGCAGCAAGTGACATGTGAGGGTAAACGCCAAGGTTCTCATTCTCCTGAGCGGTCGGGCTCCTTCAGAACTCCGTCATTGTATTCTTGACGCCTCATATGCCAGTCACCGGCTCGATGGCCGTATGGTAGCTGAGACCAAGCATACCGTTACGAACCCTCCTCTACGAACGTGC'
#_or
""" N=input('enter name of sequence: ')
S=open(N)
seq=S.read()
 """
seq_dict={'A':'T','T':'A','C':'G','G':'C'}
reversed_seq = ''.join(seq_dict.get(base, base) for base in reversed(S))

print(reversed_seq)

