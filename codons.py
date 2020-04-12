#!/usr/bin/env python3

# Print out all the codons for the sequence below in reading frame 1
# Use a 'for' loop

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'

"""
print(dna[0:3])
print(dna[3:6])
print(dna[6:9])
print(dna[9:12])
"""
# For loop prints out all codons in increments of 3 
#for i in range(0, 27, 3): # 27 total characters, in increments of 3
#	print(dna[i:i+3])

# Nested loop
for f in range(3):
	print('frame', f)
	for i in range(0, len(dna) -2, 3):
		codon = dna[i:i+3]
		print(codon)

"""
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""
