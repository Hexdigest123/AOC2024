SAFE_REPORTS = 0


def check_safe(number_list):
    difference = int(number_list[1]) - int(number_list[0])
    if difference == 0 or difference > 3 or difference < -3:
        return False

    for index, number in enumerate(number_list):
        number = int(number)
        if index + 1 == len(number_list):
            continue

        if difference > 0 and (int(number_list[index + 1]) - number) < 0:
            return False

        if difference < 0 and (int(number_list[index + 1]) - number) > 0:
            return False

        if (
            int(number_list[index + 1]) - number == 0
            or int(number_list[index + 1]) - number > 3
            or int(number_list[index + 1]) - number < -3
        ):
            return False
    return True


def check_sector(number_list):
    global SAFE_REPORTS

    if check_safe(number_list):
        SAFE_REPORTS = SAFE_REPORTS + 1
        return

    for i in range(len(number_list)):
        result = number_list[:i] + number_list[i + 1 :]
        if check_safe(result):
            SAFE_REPORTS = SAFE_REPORTS + 1
            return


with open("text.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        numbers = line.split(" ")
        check_sector(numbers)
    print(SAFE_REPORTS)
