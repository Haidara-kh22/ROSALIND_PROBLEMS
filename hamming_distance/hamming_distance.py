def hamming_distance(s, t):
    # Ensure the strings are of equal length
    if len(s) != len(t):
        return "Strings must be of equal length"
    
    # Count the number of differing positions
    return sum(a != b for a, b in zip(s, t))

# Sample DNA strings
s = "ACGGAGTCACGTCATCCACGTGAACGTTTACTATTGCATAGAACTCGAGGCAGCCCTATAAAGTGCATAGACAAGCTGCCGTTACCCCAGGCTTTGCTCCAGATGATACTATCGTAGCGGGATTCTAAATTTACCGAGCTTGTCTAAGGCCTTGGGGGATACCGCGTTACTAGATTTGGGCTGATCCTTGCTCTATTAATACGGACTGGTGTGTTCCTGCCGTATTCAACCGGCTGGCATTTAGGCAGCTCGGCCATTACAGTAGCTACCTCGCCATCATTTTAGCCTGCTCGTACTACCCGTCATCGTTTTGTGCGCCTAGTCGTCGACGAGCACACTCATTTCGCACAGAGGGGCATCTGCGACTCGATGCTCAATCACAGCTTAAGAAGTGGGAGATTTGACTTGGGGGAGGCGGTGCAAAAAACGCGAGTGTCTTCTATTTCGGTGCGCAAAGTGAAAGATTTTCGTGCAGGTCAAGCTCGGTCTAAACCAGTCGGTGAGGCCTTTTGCTAGTAAAATACCGTCTTCATTAATCTCAAAAGTTACGTTCAGGCGTACCAATGAGCGGTGGGGTTCAAAGGAAAGATTAAGTCTAAACTAATTATTGACGATGCATGCGTGTGTACTGTATGTGTCTAAACGTATACAAACCATTATACTCGAAAGAAGACGAAAGGTAAAAGGGCCACGTTAGCCTGTACCCCGCTCGCAGTACTACTGCCCGCAATAGTCGGGATTGCTTTCTCACTAGCCCTGCAAAAACCACGGAATTTGTCGTCGTTGGAATGGTGTATTGGTGGGAATTAGTCCCAGTCATGCTCCCATATGGGCAGGTAAGTGCCGAGGGTAGTGTAAGCGGAAGAACAGATAGTACCCAGAATGAAGCTGGGGAAAAATGCAATCCTATTAGGTCTCGAAAAAAGGACCATTACGTTTAGGTGCTAAGCAGAGACGCG"
t = "CCACACAATATTAATAAACTTAACCCATTCGTCTTGCATAAGACCCGAAGCAGGGCACTCAAGCTCTAGTACAAGCCGCCCCTCCGGGGGACTATCCGTTATACAATACGGCGGAAGGTGGCTTCTTAATTTTGCGTGATCATCCGCGGGATTTCGAGGGTCTGCTACAGATGGTTTCTGCGTTGGCTTTTAACATCATTTGTTTCCGATGTGTAAGTCGAGTACTTAACGATCGCGCTTCATTGCGGATGTGGCGCTAAGGTAAATCCCGCGAGATTATTTCTCGTTGATCGTCGATCGCGTCATGTTTTCGTGAGCCAAGTCGTCGGTCTCCATAAACATTTTGCAATTCTGGGGAGCTTGGTCTCCACACTCGACCCCGGTCCGACAGGCAACATATTTACTTCGGGGGAGGCGGGGAAGAAAACGGTTGTGCCTGTTAAAACTGTGCGCAAAGGGAGATATACTATCGTCGCTCGAGCGCGACCTAGAAGGGATAGTAATTGCATGGTCAAAAGTTTTTTCCTGTGTGAAAGTCTCATTATTTACTAGTACGTGTCTCCAGTAATAGGCGGGGCGTTAAGAAAGTTCATGTCCAATGCAATATTTGATATGGTATCTGGCTGAAGTCAATGTGTGAAATTTTAGCCTTACGAGTGTACTGCAAAGCTGCCTAATCGGAAAGATTGGCTAGTAGCCTGTACGCCATTCCGAAGAGCATTGCCACTCACACTCTACGTCGGTTACAAACTCCCCAGATATAAGCCTTGGGAACAGAGGACGATCGATTCGTTTCTCGGTGGGCAACCCGATTCGTCAAACTCACGTATGCGCAGGTAAGGACCCGGGGGAGTGTGAGCGGAAGAGGCGCTGATCGACTCTAAGAAGGTGGGAGGGTATCCCCTCCGTCAGTAGAAGTATCAAGAAAACGTATAGTCGAGATGCTGAACCCAGAAGTA"

# Calculate and print the Hamming distance
distance = hamming_distance(s, t)
print("Hamming Distance:", distance)