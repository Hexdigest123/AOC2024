import re
import numpy as np

FILE_CONTENT = []

counter = 0

with open("text.txt", "r", encoding="utf-8") as file:
    for line in file:
        FILE_CONTENT.append(line.strip())

for line in FILE_CONTENT:
    counter = counter + len(re.findall(r"XMAS", line))

print(counter)

for i in range(0, len(FILE_CONTENT)):
    line = ""
    for j in range(0, len(FILE_CONTENT[i])):
        line = line + FILE_CONTENT[j][i]
    counter = counter + len(re.findall(r"XMAS", line))

print(counter)

array = []
for line in FILE_CONTENT:
    char_arr = []
    for char in line:
        char_arr.append(char)
    array.append(char_arr)

array = np.array(array)

main_diagonal = np.diag(array)
upper_diagonals = [np.diag(array, k=i) for i in range(1, array.shape[1])]
lower_diagonals = [np.diag(array, k=-i) for i in range(1, array.shape[0])]

all_diagonals = [main_diagonal] + upper_diagonals + lower_diagonals

for i, diagonal in enumerate(all_diagonals):
    counter = counter + len(re.findall(r"XMAS", "".join(diagonal)))

print(counter)
