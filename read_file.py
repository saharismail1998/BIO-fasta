a_count = 0
t_count = 0
g_count = 0
c_count = 0
n_count = 0

with open("GCA_000001405.29.fasta", 'r') as fasta:
    for line in fasta:
        if line.startswith('>'):
            continue

        for dna_char in line:
            if dna_char == "C":
                c_count += 1
            elif dna_char == "G":
                g_count += 1
            elif dna_char == "A":
                a_count += 1
            elif dna_char == "T":
                t_count += 1
            elif dna_char == "N":
                n_count += 1

print('A:', a_count)
print('C:', c_count)
print('G:', g_count)
print('T:', t_count)
print('N:', n_count)

counts = [a_count, t_count, c_count, g_count, n_count]
