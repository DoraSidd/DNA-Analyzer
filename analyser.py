dna = "ATGGCCATTTAAGTAGCC"

# LIBRARIES
complement = {"A":"T", "T":"A", "G":"C", "C":"G"}
genetic_code = {"ATG":"M","GCC":"A","ATT":"I","GTA":"V","TAA":"STOP","TAG":"STOP","TGA":"STOP"}

# DNA LENGTH
def sequence_length(dna):
    for i in dna:
        return seq
seq = sequence_length(dna)

# COUNT BASES
def count_bases(dna):
    a = 0
    t = 0
    g = 0
    c = 0
    for base in dna:
        if base == "A":
            a += 1 
        elif base == "T":
            t += 1
        elif base == "G":
            g += 1
        elif base == "C":
            c += 1
    return a , t , g , c 

a,t,g,c = count_bases(dna)


# GC CONTENT
def gc_content(dna):
    g = 0
    c = 0
    for base in dna:
        if base == "G":
            g += 1
        if base == "C":
            c += 1
    gc = ((g+c) / len(dna))*100
    return gc
gc = gc_content(dna)

# COMPLEMENT DNA
def complement_dna(dna):
    comp = " "
    for base in dna:
        comp += complement[base]
    return comp
comp = complement_dna(dna)

# TRANSLATION
def translate(dna):
    codon = " "
    amino_acid = " "
    protein = " "
    for i in range(0,len(dna),3):
        codon = dna[i:i+3]
        amino_acid = genetic_code[codon]
        if amino_acid == "STOP":
            break
        protein += amino_acid
    return protein
protein = translate(dna)

# DNA ANALYSIS
def print_analysis(dna):
    print("Length:",seq)
    print("A:",a)
    print("T:",t)
    print("G:",g)
    print("C:",c)
    print(f"gc_content:{gc:.2f}%")
    print("Complementary:",comp)
    print("Protein:",protein)

print_analysis(dna)