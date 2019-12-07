import re

MIN = 128392
MAX = 643281

def check_monotonous_increase(number):
    num = str(number)

    for i in range(len(num) -1):
        if int(num[i+1]) < int(num[i]):
            return False
    
    return True

def check_doubles(number):
    num = str(number)

    for i in range(len(num) -1):
        if num[i] == num[i+1]:
            return True

    return False

def check_exact_two_doubles(number):
    num = str(number)

    matches = re.findall("11+|22+|33+|44+|55+|66+|77+|88+|99+", num)

    if matches and min([len(match) for match in matches]) == 2:
        return True

    return False


if __name__ == "__main__":
    test_cases = [11,22,33,44,55,66,77,88,99,112,211,121, 1111,11112, 1111222344]

    for case in test_cases:
        print(f"{case}: {check_exact_two_doubles(case)}")

    increasing = [num for num in range(MIN, MAX + 1) if check_monotonous_increase(num)]
    increasing_with_doubles = [num for num in increasing if check_doubles(num)]
    print(len(increasing_with_doubles))

    
    increasing = [num for num in range(MIN, MAX + 1) if check_monotonous_increase(num)]
    increasing_with_doubles = [num for num in increasing if check_exact_two_doubles(num)]
    print(len(increasing_with_doubles))