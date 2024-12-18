left = []
right = []
distances = []

with open("text.txt", "r", encoding="utf-8") as file:
    for line in file:
        lineFragments = line.strip().split(" ")
        left.append(lineFragments[0])
        right.append(lineFragments[1])

left.sort()
right.sort()

for i in range(0, len(left)):
    if int(left[i]) > int(right[i]):
        distances.append(int(left[i]) - int(right[i]))
    else:
        distances.append(int(right[i]) - int(left[i]))

print(sum(distances))
