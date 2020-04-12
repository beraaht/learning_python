#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

dna = 'ATGGCCTTT'

# len(dna) = returns of number of characters in the object dna, which are 9 base pairs
# position = i + f
# f = frame

# Single loop
for i in range(0, len(dna)): # range is from positions 0 to 8
	print(i, i % 3, dna[i]) # modulus operator i % 3 returns the remainder of the division, which is the frame

# Nested loops
for i in range(0, len(dna), 3): # from 0 to 8 in increments of 3 only, frame goes in order of 0, 1, 2
	for f in range(3):
		position = i + f  # positions 0 - 8 
		print(position, f, dna[position]) # letter of DNA = dna[position] instead of dna[i] because this is a nested loop 

"""
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T

0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""
