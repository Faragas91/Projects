import numpy as np
import math

seq1 = "ATG"
seq2 = "AGTT"
seq1_split = list(seq1)
seq2_split = list(seq2)
max_number = []

gap = -2
mismatch = -1
match = 1

null_matrix = np.zeros((len(seq2) + 1, len(seq1) + 1), dtype=int)

# Gaps in der ersten Spalte und erste Zeile einfügen

x = 1 # Zeilen
while x < len(seq1) + 1:
    null_matrix[0][x] += gap * x
    x += 1

y = 1 # Spalten
while y < len(seq2) + 1:
    null_matrix[y][0] += gap * y
    y += 1

# Matrix gefüllen
i = 1 # Spalten
j = 1 # Zeilen

while j < len(seq2) + 1:
    while i < len(seq1)+ 1:
        max_number.append(null_matrix[j,i-1] + gap)
        max_number.append(null_matrix[j-1,i] + gap)
        if seq2_split[j-1] == seq1_split[i-1]:
            max_number.append(null_matrix[j-1,i-1] + match)
        if seq2_split[j-1] != seq1_split[i-1]:
            max_number.append(null_matrix[j-1, i-1] + mismatch)
        null_matrix[j][i] = max(max_number)
        max_number = []
        i += 1
    j += 1
    i = 1

print(null_matrix)

print("Der Score ist", null_matrix[len(seq2)][len(seq1)])



# Backtracking
aligned_seq1 = ""
aligned_seq2 = ""
i = len(seq1)
j = len(seq2)

while i > 0 and j > 0:
    current_score = null_matrix[j][i]
    left_score = null_matrix[j][i-1]
    top_score = null_matrix[j-1][i]
    diagonal_score = null_matrix[j-1][i-1]

    if current_score == diagonal_score + match and seq1[i-1] == seq2[j-1]:
        aligned_seq1 = seq1[i-1] + aligned_seq1
        aligned_seq2 = seq2[j-1] + aligned_seq2
        i -= 1
        j -= 1
    elif current_score == diagonal_score + mismatch and seq1[i-1] != seq2[j-1]:
        aligned_seq1 = seq1[i-1] + aligned_seq1
        aligned_seq2 = seq2[j-1] + aligned_seq2
        i -= 1
        j -= 1
    elif current_score == left_score + gap:
        aligned_seq1 = seq1[i-1] + aligned_seq1
        aligned_seq2 = "-" + aligned_seq2
        i -= 1
    elif current_score == top_score + gap:
        aligned_seq1 = "-" + aligned_seq1
        aligned_seq2 = seq2[j-1] + aligned_seq2
        j -= 1

while i > 0:
    aligned_seq1 = seq1[i-1] + aligned_seq1
    aligned_seq2 = "-" + aligned_seq2
    i -= 1

while j > 0:
    aligned_seq1 = "-" + aligned_seq1
    aligned_seq2 = seq2[j-1] + aligned_seq2
    j -= 1

print("Aligned Sequence 1:", aligned_seq1)
print("Aligned Sequence 2:", aligned_seq2)

