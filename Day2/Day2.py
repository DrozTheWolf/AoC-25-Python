from turtledemo.sorting_animate import partition


def part1():
    final_code = 0
    with open("input.txt") as file:
        line = file.readline().strip()
        ranges = line.split(",")
        for num_range in ranges:
            split_range = num_range.split("-")
            lower = int(split_range[0])
            upper = int(split_range[1])
            for i in range(lower, upper+1):
                if len(str(i)) % 2 == 0:
                    if is_invalid_2(i):
                        final_code += i

        print(f"Final Code: {final_code}")

def part2():
    final_code = 0
    with open("input.txt") as file:
        line = file.readline().strip()
        ranges = line.split(",")
        for num_range in ranges:
            split_range = num_range.split("-")
            lower = int(split_range[0])
            upper = int(split_range[1])
            for i in range(lower, upper+1):
                if is_invalid_2(i):
                    final_code += i

        print(f"Final Code: {final_code}")



def is_invalid(number):
    str_num = str(number)
    left = str_num[:len(str_num)//2]
    right = str_num[len(str_num)//2:]

    if left == right:
        print(f"Found repeat number: {number}")
        return True
    return False

def is_invalid_2(number):
    str_num = str(number)

    for div_len in possible_divisions(len(str_num)):
        div = str_num[:div_len]
        if div * (len(str_num) // div_len) == str_num:
            print(f"Found repeat number: {number}")
            return True

    return False

def possible_divisions(length):
    divisions = []

    max_div = length // 2

    for div_len in range(1, max_div +1):
        if length % div_len == 0:
            divisions.append(div_len)

    return divisions


if __name__ == '__main__':
    part2()