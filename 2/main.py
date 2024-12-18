left = []
right = []
similarity = []

with open("text.txt", "r", encoding="utf-8") as file:
    for line in file:
        lineFragments = line.strip().split(" ")
        left.append(lineFragments[0])
        right.append(lineFragments[1])

left.sort()
right.sort()

for value in left:
    similarity.append(int(value) * right.count(value))

print(sum(similarity))
