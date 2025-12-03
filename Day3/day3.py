
def part1():
    final_code = 0
    with open("input.txt") as file:
        for line in file:
            volt = highest_voltage(line.strip())
            final_code += volt

    print(f"Final Code: {final_code}")

def part2():
    final_code = 0
    with open("input.txt") as file:
        for line in file:
            volt = highest_voltage2(line.strip())
            final_code += volt

    print(f"Final Code: {final_code}")

def highest_voltage(bank):
    highest = 0
    for i in range(0, len(bank)):
        for j in range(i+1, len(bank)):
            num = bank[i] + bank[j]
            if int(num) > highest:
                highest = int(num)

    print(f"Highest Combo Found: {highest}")
    return highest

def highest_voltage2(bank):
    highest = []
    index = 0

    while len(highest) < 12:
        remaining = 12 - len(highest)
        end = len(bank) - remaining + 1
        max_num = '0'
        max_index = index

        for i in range(index, end):
            if bank[i] > max_num:
                max_num = bank[i]
                max_index = i

        highest.append(max_num)
        index = max_index + 1

    result = int(''.join(highest))
    print(f"Highest Value in Bank: {result}")

    return result



if __name__ == '__main__':
    part2()