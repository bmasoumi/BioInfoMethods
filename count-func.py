def PatternCount(Text, Pattern):
    count = 0 # output variable
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

T='GCATGCAGGGTTAGATTTCGCCTCAGGGTTTGAATCATCTCAGGGTTGACAGGGTTCAGGGTTGCAGGGTTCCACAGGGTTCAGGGTTCGTTCAGGGTTGCAGGGTTACAGGGTTACAGGGTTCAGGGTTCCAGGGTTCAGGGTTCAGGGTTCAGGGTTCCAGGGTTTAACAGGGTTGCATGCAGGGTTTCAGGGTTTACAGGGTTGGAATTTCACGCAGGGTTACAGGGTTTCCAGGGTTCCATGTTCAGTTTCAGGGTTCAGGGTTTCAGGGTTTAATGGGCTGGTAGGGCCATCACCAGGGTTCTGCAGGGTTCAGGGTTGGATCAGGGTTTGCAGGGTTCAGGGTTGGAACAGGGTTCCCATCCAGGGTTTCGGACTCGGTCCAGGGTTACAAGAAACGTCTGCAGGGTTAACAGGGTTACCCGCAGGGTTTCAGGGTTCTTATGTGCAGGGTTTCACGGCAGGGTTATCAGGGTTATCAGGGTTCAGGGTTCAGGGTTGACAGGGTTTGCCAGGGTTAAGATGGCCAGGGTTCCAGGGTTTGCAGGGTTGTCAGGGTTACTCAGGGTTCAGGGTTCAGGGTTCTCAGGGTTAACAGGGTTACAGGGTTCTTACCCAATCAGGGTTGCAGGGTTGCCAGGGTTACAGGGTTAAACAGGGTTCAGGGTTCAGGGTTAAACCCTACACAGGGTTGTCAGGGTTACAGGGTTCAGGGTTTCAGGGTTCAGGGTTAGGCAGGGTTTGCAGGGTTCCTGTTCTATCTATCAGGGTTCGAGCAGGGTTACAGGGTTCAGGGTTGCAGGGTTCAGGGTTAAGCAGGGTTCCAGGGTTAGTTGCCAGGGTTACAGGGTTCAACAGGGTTTGTTGGACCAGGGTTGCAGGGTTACGGGTATTTGCCAGGGTTCACTAGGGTCCAGGGTTGGGTCAACCAGGGTTCCTCAGGGTTGACACCAGGGTT'
P='CAGGGTTCA'
#count=PatternCount(T, P)
print(PatternCount(T, P))