import re

sum = 0

# with open("formatted_text.txt", "w", encoding="utf-8") as foutput:
#   with open("text.txt", "r", encoding="utf-8") as finput:
#       for line in finput:
#           for result in re.findall(r"do\(\)|don't\(\)|mul\(\d*,\d*\)", line):
#               foutput.write(result + "\n")


MUL_STATE = True
with open("formatted_text.txt", "r", encoding="utf-8") as finput:
    for line in finput:
        if line.strip() == "don't()":
            MUL_STATE = False
        elif line.strip() == "do()":
            MUL_STATE = True
            print("CHANGED")

        for result in re.findall(r"\d*,\d*", line):
            splitted_result = result.split(",")
            if MUL_STATE:
                sum = sum + (int(splitted_result[0]) * int(splitted_result[1]))
print(sum)
