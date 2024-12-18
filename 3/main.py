SAFE_REPORTS = 0


def check_safe(number_list):
    global SAFE_REPORTS

    difference = int(number_list[1]) - int(number_list[0])
    if difference == 0 or difference > 3 or difference < -3:
        return

    for index, number in enumerate(number_list):
        number = int(number)
        if index + 1 == len(number_list):
            continue

        if difference > 0 and (int(number_list[index + 1]) - number) < 0:
            return

        if difference < 0 and (int(number_list[index + 1]) - number) > 0:
            return

        if (
            int(number_list[index + 1]) - number == 0
            or int(number_list[index + 1]) - number > 3
            or int(number_list[index + 1]) - number < -3
        ):
            return
    SAFE_REPORTS = SAFE_REPORTS + 1


with open("text.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        numbers = line.split(" ")
        check_safe(numbers)
    print(SAFE_REPORTS)
