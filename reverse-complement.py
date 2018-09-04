seq = "ATCG"
answer = []
complement = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}

for nucleotide in seq:
    answer.append(complement[nucleotide])

print (''.join(answer[::-1]))
