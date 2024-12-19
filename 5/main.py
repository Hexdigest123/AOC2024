import re

sum = 0

# with open("formatted_text.txt", "w", encoding="utf-8") as foutput:
#   with open("text.txt", "r", encoding="utf-8") as finput:
#       for line in finput:
#           for result in re.findall(r"mul\(\d*,\d*\)", line):
#               foutput.write(result + "\n")

with open("formatted_text.txt", "r", encoding="utf-8") as finput:
    for line in finput:
        for result in re.findall(r"\d*,\d*", line):
            splitted_result = result.split(",")
            sum = sum + (int(splitted_result[0]) * int(splitted_result[1]))
print(sum)
